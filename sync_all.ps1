#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Audit, fetch, fast-forward, or push every managed repository.
.DESCRIPTION
    Status is the safe default. Pull and Push skip dirty repositories and never
    create commits. The exact local/remote branch mapping comes from
    workspace-repos.json, which is required for split research/release repos.
.EXAMPLE
    ./sync_all.ps1 -Action Status
    ./sync_all.ps1 -Action Fetch
    ./sync_all.ps1 -Action Pull
    ./sync_all.ps1 -Action Push
#>

[CmdletBinding()]
param(
    [ValidateSet("Status", "Fetch", "Pull", "Push")]
    [string]$Action = "Status",
    [string]$Manifest = "",
    [switch]$IncludePending,
    [switch]$UseConfiguredProxy
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Invoke-RepoGit {
    param(
        [Parameter(Mandatory)] [string]$RepoPath,
        [Parameter(Mandatory)] [string[]]$GitArguments
    )

    $safePath = $RepoPath.Replace('\', '/')
    $arguments = @("-c", "safe.directory=$safePath")
    if (-not $UseConfiguredProxy) {
        $arguments += @("-c", "http.proxy=", "-c", "https.proxy=")
    }
    $arguments += @("-C", $RepoPath)
    $arguments += $GitArguments

    $previousErrorAction = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    try {
        $output = @(& git @arguments 2>&1)
        $exitCode = $LASTEXITCODE
    } finally {
        $ErrorActionPreference = $previousErrorAction
    }
    [PSCustomObject]@{
        ExitCode = $exitCode
        Output = $output
        Text = ($output -join "`n")
    }
}

function Normalize-RemoteUrl {
    param([string]$Url)
    if (-not $Url) { return "" }
    return (($Url.Trim() -replace '\\', '/') -replace '\.git/?$', '').TrimEnd('/')
}

$root = $PSScriptRoot
if (-not $Manifest) {
    $Manifest = Join-Path $root "workspace-repos.json"
}
if (-not (Test-Path -LiteralPath $Manifest -PathType Leaf)) {
    throw "Workspace manifest not found: $Manifest"
}

$inventory = Get-Content -Raw -LiteralPath $Manifest | ConvertFrom-Json
$entries = @(
    [PSCustomObject]@{
        path = "."
        remote = $inventory.workspace.remote
        localBranch = $inventory.workspace.localBranch
        remoteBranch = $inventory.workspace.remoteBranch
        syncEnabled = $true
        blocker = ""
    }
) + @($inventory.repositories)

$failures = 0
$warnings = 0
$clean = 0
$dirty = 0
$pending = 0

Write-Host "=== Workspace Git $Action ===" -ForegroundColor Cyan

foreach ($repo in $entries) {
    if (-not $repo.syncEnabled -and -not $IncludePending) {
        Write-Host "[PENDING] $($repo.path): $($repo.blocker)" -ForegroundColor Yellow
        $pending++
        continue
    }

    $repoPath = if ($repo.path -eq ".") {
        $root
    } else {
        Join-Path $root $repo.path.Replace('/', [IO.Path]::DirectorySeparatorChar)
    }

    if (-not (Test-Path -LiteralPath (Join-Path $repoPath ".git"))) {
        Write-Host "[MISSING] $($repo.path)" -ForegroundColor Red
        $failures++
        continue
    }

    $remoteResult = Invoke-RepoGit -RepoPath $repoPath -GitArguments @("remote", "get-url", "origin")
    if ($remoteResult.ExitCode -ne 0) {
        Write-Host "[NO ORIGIN] $($repo.path)" -ForegroundColor Red
        $failures++
        continue
    }
    $actualRemote = $remoteResult.Text.Trim()
    $remoteMismatch = (Normalize-RemoteUrl $actualRemote) -ne (Normalize-RemoteUrl $repo.remote)

    $branchResult = Invoke-RepoGit -RepoPath $repoPath -GitArguments @("branch", "--show-current")
    $branch = $branchResult.Text.Trim()
    if (-not $branch) { $branch = "(detached)" }
    $branchMismatch = $branch -ne $repo.localBranch

    $trackedResult = Invoke-RepoGit -RepoPath $repoPath -GitArguments @("status", "--porcelain=v1", "-uno")
    $trackedChanges = @($trackedResult.Output | Where-Object { $_ }).Count
    $untrackedResult = Invoke-RepoGit -RepoPath $repoPath -GitArguments @(
        "-c", "core.quotePath=false", "ls-files", "--others", "--exclude-standard"
    )
    $untrackedFiles = @($untrackedResult.Output | Where-Object { $_ }).Count
    $isDirty = ($trackedChanges + $untrackedFiles) -gt 0

    if ($Action -ne "Status") {
        $fetchResult = Invoke-RepoGit -RepoPath $repoPath -GitArguments @("fetch", "--prune", "--tags", "origin")
        if ($fetchResult.ExitCode -ne 0) {
            Write-Host "[FETCH FAILED] $($repo.path): $($fetchResult.Text)" -ForegroundColor Red
            $failures++
            continue
        }
    }

    $remoteRef = "refs/remotes/origin/$($repo.remoteBranch)"
    $refResult = Invoke-RepoGit -RepoPath $repoPath -GitArguments @("show-ref", "--verify", "--quiet", $remoteRef)
    $ahead = "?"
    $behind = "?"
    if ($refResult.ExitCode -eq 0) {
        $countsResult = Invoke-RepoGit -RepoPath $repoPath -GitArguments @(
            "rev-list", "--left-right", "--count", "HEAD...origin/$($repo.remoteBranch)"
        )
        if ($countsResult.ExitCode -eq 0) {
            $counts = $countsResult.Text.Trim() -split '\s+'
            if ($counts.Count -ge 2) {
                $ahead = $counts[0]
                $behind = $counts[1]
            }
        }
    }

    $problems = @()
    if ($remoteMismatch) { $problems += "remote-mismatch" }
    if ($branchMismatch) { $problems += "branch-mismatch" }
    if ($isDirty) { $problems += "dirty" }
    if ($refResult.ExitCode -ne 0) { $problems += "missing-remote-branch" }

    if ($Action -eq "Pull") {
        if ($remoteMismatch -or $branchMismatch -or $isDirty -or $refResult.ExitCode -ne 0) {
            Write-Host "[SKIP PULL] $($repo.path): $($problems -join ', ')" -ForegroundColor Yellow
            $warnings++
            continue
        }
        $mergeResult = Invoke-RepoGit -RepoPath $repoPath -GitArguments @(
            "merge", "--ff-only", "origin/$($repo.remoteBranch)"
        )
        if ($mergeResult.ExitCode -ne 0) {
            Write-Host "[PULL FAILED] $($repo.path): $($mergeResult.Text)" -ForegroundColor Red
            $failures++
            continue
        }
    } elseif ($Action -eq "Push") {
        if ($remoteMismatch -or $branchMismatch -or $isDirty -or $refResult.ExitCode -ne 0) {
            Write-Host "[SKIP PUSH] $($repo.path): $($problems -join ', ')" -ForegroundColor Yellow
            $warnings++
            continue
        }
        if ([int]$behind -gt 0) {
            Write-Host "[SKIP PUSH] $($repo.path): behind $behind" -ForegroundColor Yellow
            $warnings++
            continue
        }
        if ([int]$ahead -gt 0) {
            $pushResult = Invoke-RepoGit -RepoPath $repoPath -GitArguments @(
                "push", "origin", "HEAD:refs/heads/$($repo.remoteBranch)"
            )
            if ($pushResult.ExitCode -ne 0) {
                Write-Host "[PUSH FAILED] $($repo.path): $($pushResult.Text)" -ForegroundColor Red
                $failures++
                continue
            }
            $ahead = 0
        }
    }

    if ($problems.Count -eq 0 -and [int]$ahead -eq 0 -and [int]$behind -eq 0) {
        Write-Host "[CLEAN] $($repo.path) ($branch -> origin/$($repo.remoteBranch))" -ForegroundColor DarkGray
        $clean++
    } else {
        $label = if ($isDirty) { "DIRTY" } else { "CHECK" }
        Write-Host ("[{0}] {1} branch={2} upstream=origin/{3} ahead={4} behind={5} tracked={6} untracked={7} {8}" -f
            $label, $repo.path, $branch, $repo.remoteBranch, $ahead, $behind,
            $trackedChanges, $untrackedFiles, ($problems -join ',')) -ForegroundColor Yellow
        if ($isDirty) { $dirty++ } else { $warnings++ }
    }
}

Write-Host ""
Write-Host "Clean: $clean; dirty: $dirty; pending: $pending; warnings: $warnings; failures: $failures"
if ($failures -gt 0) {
    exit 1
}
