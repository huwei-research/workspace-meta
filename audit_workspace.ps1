#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Audit repository metadata, required files, Git state, and naming hazards.
.DESCRIPTION
    This script is read-only. It checks the manifest against the local tree,
    reports dirty repositories and oversized tracked blobs, and flags case
    collisions or non-canonical paper-figure names that can fail cross-platform.
#>

[CmdletBinding()]
param(
    [string]$Manifest = "",
    [string]$ReportPath = "",
    [string[]]$RepoFilter = @(),
    [switch]$DeepNaming
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Invoke-RepoGit {
    param(
        [Parameter(Mandatory)] [string]$RepoPath,
        [Parameter(Mandatory)] [string[]]$GitArguments
    )

    $safePath = $RepoPath.Replace('\', '/')
    $arguments = @("-c", "safe.directory=$safePath", "-C", $RepoPath) + $GitArguments
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
$inventory = Get-Content -Raw -LiteralPath $Manifest | ConvertFrom-Json

$findings = New-Object System.Collections.Generic.List[object]
function Add-Finding {
    param([string]$Severity, [string]$Repo, [string]$Check, [string]$Detail)
    $findings.Add([PSCustomObject]@{
        Severity = $Severity
        Repo = $Repo
        Check = $Check
        Detail = $Detail
    })
}

$manifestPaths = @($inventory.repositories | ForEach-Object { $_.path.ToLowerInvariant() })
$duplicates = $manifestPaths | Group-Object | Where-Object { $_.Count -gt 1 }
foreach ($duplicate in $duplicates) {
    Add-Finding "ERROR" "." "manifest" "Duplicate path: $($duplicate.Name)"
}

$entries = @(
    [PSCustomObject]@{
        path = "."
        repo = $inventory.workspace.repo
        remote = $inventory.workspace.remote
        localBranch = $inventory.workspace.localBranch
        remoteBranch = $inventory.workspace.remoteBranch
        syncEnabled = $true
        blocker = ""
    }
) + @($inventory.repositories)

if ($RepoFilter.Count -gt 0) {
    $entries = @($entries | Where-Object {
        $candidate = $_.path
        @($RepoFilter | Where-Object { $candidate -like $_ }).Count -gt 0
    })
}

foreach ($repo in $entries) {
    Write-Host "[AUDIT] $($repo.path)" -ForegroundColor DarkGray
    $repoPath = if ($repo.path -eq ".") {
        $root
    } else {
        Join-Path $root $repo.path.Replace('/', [IO.Path]::DirectorySeparatorChar)
    }

    if (-not $repo.syncEnabled) {
        Add-Finding "BLOCKED" $repo.path "sync" $repo.blocker
    }
    if (-not (Test-Path -LiteralPath (Join-Path $repoPath ".git"))) {
        Add-Finding "ERROR" $repo.path "repository" "Missing Git repository"
        continue
    }

    $required = if ($repo.path -eq ".") {
        @("README.md", "AGENTS.md", "CONVENTIONS.md", ".gitignore", ".gitattributes")
    } else {
        @("README.md", "AGENTS.md", ".gitignore", ".gitattributes")
    }
    foreach ($name in $required) {
        if (-not (Test-Path -LiteralPath (Join-Path $repoPath $name) -PathType Leaf)) {
            Add-Finding "ERROR" $repo.path "required-file" "Missing $name"
        }
    }

    if ($repo.path -ne ".") {
        $leaf = Split-Path -Leaf $repoPath
        if ($leaf -cne $repo.repo) {
            Add-Finding "WARN" $repo.path "repo-name" "Folder '$leaf' differs from manifest repo '$($repo.repo)'"
        }
    }

    $remote = Invoke-RepoGit -RepoPath $repoPath -GitArguments @("remote", "get-url", "origin")
    if ($remote.ExitCode -ne 0) {
        Add-Finding "ERROR" $repo.path "remote" "origin is missing"
    } elseif ((Normalize-RemoteUrl $remote.Text) -ne (Normalize-RemoteUrl $repo.remote)) {
        Add-Finding "ERROR" $repo.path "remote" "origin is '$($remote.Text.Trim())', expected '$($repo.remote)'"
    }

    $branch = Invoke-RepoGit -RepoPath $repoPath -GitArguments @("branch", "--show-current")
    $branchName = $branch.Text.Trim()
    if ($branchName -ne $repo.localBranch) {
        Add-Finding "ERROR" $repo.path "branch" "local '$branchName', expected '$($repo.localBranch)'"
    }

    $trackedChanges = Invoke-RepoGit -RepoPath $repoPath -GitArguments @("status", "--porcelain=v1", "-uno")
    $trackedCount = @($trackedChanges.Output | Where-Object { $_ }).Count
    $untracked = Invoke-RepoGit -RepoPath $repoPath -GitArguments @(
        "-c", "core.quotePath=false", "ls-files", "--others", "--exclude-standard"
    )
    $untrackedPaths = @($untracked.Output | Where-Object { $_ })
    Write-Verbose "$($repo.path): status collected"
    if ($trackedCount -gt 0 -or $untrackedPaths.Count -gt 0) {
        Add-Finding "WARN" $repo.path "dirty" "tracked changes: $trackedCount; untracked files: $($untrackedPaths.Count)"
    }

    if ($DeepNaming) {
        $trackedPathsResult = Invoke-RepoGit -RepoPath $repoPath -GitArguments @(
            "-c", "core.quotePath=false", "ls-files"
        )
        $trackedPaths = @($trackedPathsResult.Output | Where-Object { $_ })
        Write-Verbose "$($repo.path): tracked paths collected"
        if ($untrackedPaths.Count -gt 10000) {
            Add-Finding "WARN" $repo.path "naming-scan" "Skipped untracked naming scan for $($untrackedPaths.Count) files; reduce generated/untracked output first"
            $allPaths = @($trackedPaths)
        } else {
            $allPaths = @($trackedPaths + $untrackedPaths)
        }

        $caseCollisions = @($allPaths | Group-Object { $_.ToLowerInvariant() } | Where-Object {
            @($_.Group | Select-Object -Unique).Count -gt 1
        })
        foreach ($collision in $caseCollisions | Select-Object -First 20) {
            Add-Finding "ERROR" $repo.path "case-collision" (($collision.Group | Select-Object -Unique) -join " | ")
        }
        Write-Verbose "$($repo.path): case collisions checked"

        $badFigures = @($allPaths | Where-Object {
            $_ -match '(^|/)paper/figures/' -and
            $_ -match '\.(pdf|png|jpe?g)$' -and
            ($_ -split '/')[-1] -notmatch '^[a-z0-9][a-z0-9_.-]*$'
        })
        if ($badFigures.Count -gt 0) {
            $sample = ($badFigures | Select-Object -First 5) -join "; "
            Add-Finding "WARN" $repo.path "figure-name" "$($badFigures.Count) non-canonical paper figure names; sample: $sample"
        }
        Write-Verbose "$($repo.path): figure names checked"
    }

    $largeTracked = Invoke-RepoGit -RepoPath $repoPath -GitArguments @(
        "ls-tree", "-r", "-l", "HEAD"
    )
    if ($largeTracked.ExitCode -eq 0) {
        foreach ($line in $largeTracked.Output) {
            if ($line -match '^\d+\s+\w+\s+[0-9a-f]+\s+(\d+)\s+(.+)$') {
                $size = [int64]$Matches[1]
                if ($size -ge 95MB) {
                    Add-Finding "ERROR" $repo.path "large-tracked-file" "$($Matches[2]) is $([math]::Round($size / 1MB, 1)) MiB"
                }
            }
        }
    }
    Write-Verbose "$($repo.path): tracked blob sizes checked"
}

foreach ($category in @("Research", "Publish", "Public", "Experimental", "Personal")) {
    $categoryPath = Join-Path $root $category
    if (-not (Test-Path -LiteralPath $categoryPath)) { continue }
    foreach ($directory in Get-ChildItem -LiteralPath $categoryPath -Force -Directory) {
        if (-not (Test-Path -LiteralPath (Join-Path $directory.FullName ".git"))) { continue }
        $relative = "$category/$($directory.Name)".ToLowerInvariant()
        if ($manifestPaths -notcontains $relative) {
            Add-Finding "ERROR" $relative "manifest" "Git repository is not declared in workspace-repos.json"
        }
    }
}

$severityOrder = @{ "ERROR" = 0; "BLOCKED" = 1; "WARN" = 2; "INFO" = 3 }
$ordered = $findings | Sort-Object @{ Expression = { $severityOrder[$_.Severity] } }, Repo, Check

Write-Host "=== Workspace Audit ===" -ForegroundColor Cyan
$ordered | Format-Table -AutoSize -Wrap

$counts = $findings | Group-Object Severity | ForEach-Object {
    "$($_.Name)=$($_.Count)"
}
Write-Host (($counts | Sort-Object) -join "; ")

if ($ReportPath) {
    $report = New-Object System.Collections.Generic.List[string]
    $report.Add("# Workspace Audit")
    $report.Add("")
    $report.Add("Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')")
    $report.Add("")
    $report.Add("| Severity | Repository | Check | Detail |")
    $report.Add("|---|---|---|---|")
    foreach ($finding in $ordered) {
        $detail = $finding.Detail.Replace('|', '\|').Replace("`r", ' ').Replace("`n", ' ')
        $report.Add("| $($finding.Severity) | $($finding.Repo) | $($finding.Check) | $detail |")
    }
    $absoluteReport = if ([IO.Path]::IsPathRooted($ReportPath)) {
        $ReportPath
    } else {
        Join-Path $root $ReportPath
    }
    $reportDir = Split-Path -Parent $absoluteReport
    if ($reportDir) { New-Item -ItemType Directory -Path $reportDir -Force | Out-Null }
    [IO.File]::WriteAllLines($absoluteReport, $report, (New-Object Text.UTF8Encoding($false)))
    Write-Host "Report: $absoluteReport"
}

if (@($findings | Where-Object { $_.Severity -eq "ERROR" }).Count -gt 0) {
    exit 1
}
