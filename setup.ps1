#!/usr/bin/env pwsh
<#
.SYNOPSIS
    One-click workspace setup. Clone this repo first, then run this script.
.DESCRIPTION
    Creates category directories and clones all repos from huwei-research org
    into the correct local folder structure.
.EXAMPLE
    git clone https://github.com/huwei-research/workspace-meta.git 2026Projects
    cd 2026Projects
    .\setup.ps1
#>

param(
    [string]$Org = "huwei-research",
    [switch]$SkipVenv
)

$ErrorActionPreference = "Stop"
$root = $PSScriptRoot

Write-Host "=== Workspace Setup ===" -ForegroundColor Cyan
Write-Host "Root: $root"
Write-Host "Organization: $Org"
Write-Host ""

# Category -> Repo mapping
$repos = @{
    "Research" = @("BUPTR", "MATRO", "STARTRO", "RITRO", "MemOTRO", "BARN", "RSSM")
    "Publish" = @("DisGRem-paper", "ArXiv")
    "Public" = @("DisGRem")
    "Experimental" = @("QuasiNewton", "SelfCorrecting")
    "Personal" = @("Weihu-resume")
}

# Create directories and clone
foreach ($category in $repos.Keys) {
    $categoryDir = Join-Path $root $category
    if (-not (Test-Path $categoryDir)) {
        New-Item -ItemType Directory -Path $categoryDir -Force | Out-Null
        Write-Host "[DIR] Created $category/" -ForegroundColor Green
    }

    foreach ($repo in $repos[$category]) {
        $repoDir = Join-Path $categoryDir $repo
        if (Test-Path (Join-Path $repoDir ".git")) {
            Write-Host "[SKIP] $category/$repo (already cloned)" -ForegroundColor Yellow
        } else {
            Write-Host "[CLONE] $category/$repo" -ForegroundColor Cyan
            git clone "https://github.com/$Org/$repo.git" $repoDir
            if ($LASTEXITCODE -ne 0) {
                Write-Host "[FAIL] $category/$repo" -ForegroundColor Red
            }
        }
    }
}

# Python environments
if (-not $SkipVenv) {
    Write-Host ""
    Write-Host "=== Setting up Python environments ===" -ForegroundColor Cyan

    $reqFiles = Get-ChildItem -Path $root -Recurse -Filter "requirements.txt" |
        Where-Object { $_.DirectoryName -match "\\codes$" }

    foreach ($req in $reqFiles) {
        $codesDir = $req.DirectoryName
        $venvDir = Join-Path $codesDir ".venv"
        if (Test-Path $venvDir) {
            Write-Host "[SKIP] $($req.Directory.Parent.Parent.Name) (venv exists)" -ForegroundColor Yellow
            continue
        }
        Write-Host "[VENV] $($req.Directory.Parent.Parent.Name)" -ForegroundColor Cyan
        Push-Location $codesDir
        python -m venv .venv
        & "$venvDir\Scripts\pip" install -q -r requirements.txt
        Pop-Location
    }
}

Write-Host ""
Write-Host "=== Setup Complete ===" -ForegroundColor Green
Write-Host "Open this folder in Cursor to activate workspace rules."
Write-Host "Run .\sync_all.ps1 for daily pull."
