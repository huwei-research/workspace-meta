#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Recreate the complete managed workspace from workspace-repos.json.
.DESCRIPTION
    Clone workspace-meta first, then run this script from the workspace root.
    Repositories that share a GitHub remote can still use distinct local and
    remote branches. Entries with syncEnabled=false are reported and skipped
    unless -IncludePending is supplied.
.EXAMPLE
    git clone https://github.com/huwei-research/workspace-meta.git 2026Projects
    Set-Location 2026Projects
    ./setup.ps1 -SkipVenv
#>

[CmdletBinding()]
param(
    [string]$Manifest = "",
    [string[]]$RepoFilter = @(),
    [switch]$IncludePending,
    [switch]$SkipVenv,
    [switch]$SkipLfs,
    [switch]$SkipPrivateSkills
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$root = $PSScriptRoot
if (-not $Manifest) {
    $Manifest = Join-Path $root "workspace-repos.json"
}
if (-not (Test-Path -LiteralPath $Manifest -PathType Leaf)) {
    throw "Workspace manifest not found: $Manifest"
}

$inventory = Get-Content -Raw -LiteralPath $Manifest | ConvertFrom-Json
if ($inventory.schemaVersion -ne 1) {
    throw "Unsupported workspace manifest schema: $($inventory.schemaVersion)"
}
$repositories = @($inventory.repositories)
if ($RepoFilter.Count -gt 0) {
    $repositories = @($repositories | Where-Object {
        $candidate = $_.path
        @($RepoFilter | Where-Object { $candidate -like $_ }).Count -gt 0
    })
}

Write-Host "=== Workspace Setup ===" -ForegroundColor Cyan
Write-Host "Root: $root"
Write-Host "Manifest: $Manifest"

$failures = 0
$cloned = 0
$skipped = 0

foreach ($repo in $repositories) {
    $relativePath = $repo.path.Replace('/', [IO.Path]::DirectorySeparatorChar)
    $repoDir = Join-Path $root $relativePath
    $parentDir = Split-Path -Parent $repoDir

    if (-not $repo.syncEnabled -and -not $IncludePending) {
        Write-Host "[PENDING] $($repo.path): $($repo.blocker)" -ForegroundColor Yellow
        $skipped++
        continue
    }

    if (Test-Path -LiteralPath (Join-Path $repoDir ".git")) {
        $safePath = $repoDir.Replace('\', '/')
        $actualRemote = git -c "safe.directory=$safePath" -C $repoDir remote get-url origin 2>$null
        $actualBranch = git -c "safe.directory=$safePath" -C $repoDir branch --show-current 2>$null
        if ($actualRemote -and ($actualRemote.TrimEnd('/') -replace '\.git$', '') -ne
            ($repo.remote.TrimEnd('/') -replace '\.git$', '')) {
            Write-Host "[WARN] $($repo.path): origin is $actualRemote" -ForegroundColor Yellow
            $failures++
        } elseif ($actualBranch -ne $repo.localBranch) {
            Write-Host "[WARN] $($repo.path): branch $actualBranch, expected $($repo.localBranch)" -ForegroundColor Yellow
            $failures++
        } else {
            Write-Host "[OK] $($repo.path)" -ForegroundColor DarkGray
        }
        $skipped++
        continue
    }

    if (Test-Path -LiteralPath $repoDir) {
        $contents = @(Get-ChildItem -LiteralPath $repoDir -Force -ErrorAction SilentlyContinue)
        if ($contents.Count -gt 0) {
            Write-Host "[FAIL] $($repo.path): non-empty directory is not a Git repository" -ForegroundColor Red
            $failures++
            continue
        }
    }

    New-Item -ItemType Directory -Path $parentDir -Force | Out-Null
    Write-Host "[CLONE] $($repo.path) <- $($repo.remote)#$($repo.remoteBranch)" -ForegroundColor Cyan
    git clone --no-checkout $repo.remote $repoDir
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[FAIL] clone $($repo.path)" -ForegroundColor Red
        $failures++
        continue
    }

    git -C $repoDir checkout -b $repo.localBranch --track "origin/$($repo.remoteBranch)"
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[FAIL] checkout $($repo.localBranch) from origin/$($repo.remoteBranch)" -ForegroundColor Red
        $failures++
        continue
    }

    if (-not $SkipLfs -and (Test-Path -LiteralPath (Join-Path $repoDir ".gitattributes"))) {
        $attributes = Get-Content -Raw -LiteralPath (Join-Path $repoDir ".gitattributes")
        if ($attributes -match "filter=lfs") {
            git -C $repoDir lfs pull
            if ($LASTEXITCODE -ne 0) {
                Write-Host "[WARN] Git LFS pull failed for $($repo.path)" -ForegroundColor Yellow
                $failures++
            }
        }
    }

    $cloned++
}

if (-not $SkipPrivateSkills) {
    $privateSkillSource = Join-Path $root "Personal/Weihu-resume/.agents/skills/weihu-resume-writer"
    $privateSkillTarget = Join-Path $root ".agents/skills/weihu-resume-writer"
    if (Test-Path -LiteralPath $privateSkillSource -PathType Container) {
        New-Item -ItemType Directory -Path $privateSkillTarget -Force | Out-Null
        Get-ChildItem -LiteralPath $privateSkillSource -Force | Copy-Item -Destination $privateSkillTarget -Recurse -Force
        Write-Host "[SKILL] Installed private weihu-resume-writer copy" -ForegroundColor DarkGray
    } else {
        Write-Host "[WARN] Private resume skill source is unavailable" -ForegroundColor Yellow
        $failures++
    }
}

if (-not $SkipVenv) {
    Write-Host ""
    Write-Host "=== Python Environments ===" -ForegroundColor Cyan
    foreach ($repo in $repositories | Where-Object { $_.syncEnabled -or $IncludePending }) {
        $relativePath = $repo.path.Replace('/', [IO.Path]::DirectorySeparatorChar)
        $codesDir = Join-Path (Join-Path $root $relativePath) "codes"
        $requirements = Join-Path $codesDir "requirements.txt"
        $venvDir = Join-Path $codesDir ".venv"
        if (-not (Test-Path -LiteralPath $requirements -PathType Leaf)) { continue }
        if (Test-Path -LiteralPath $venvDir) {
            Write-Host "[OK] $($repo.path)/codes/.venv" -ForegroundColor DarkGray
            continue
        }

        Write-Host "[VENV] $($repo.path)" -ForegroundColor Cyan
        python -m venv $venvDir
        if ($LASTEXITCODE -ne 0) {
            Write-Host "[FAIL] create venv for $($repo.path)" -ForegroundColor Red
            $failures++
            continue
        }
        & (Join-Path $venvDir "Scripts/pip.exe") install -r $requirements
        if ($LASTEXITCODE -ne 0) {
            Write-Host "[FAIL] install requirements for $($repo.path)" -ForegroundColor Red
            $failures++
        }
    }
}

Write-Host ""
Write-Host "Cloned: $cloned; skipped/existing: $skipped; failures: $failures"
if ($failures -gt 0) {
    exit 1
}

Write-Host "Workspace setup complete." -ForegroundColor Green
Write-Host "Run ./sync_all.ps1 -Action Status before starting work."
