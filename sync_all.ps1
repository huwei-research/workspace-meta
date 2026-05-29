#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Pull all repos (fast-forward only). Run from workspace root.
#>

$root = $PSScriptRoot
$categories = @("Research", "Publish", "Public", "Experimental", "Personal")

foreach ($cat in $categories) {
    $catDir = Join-Path $root $cat
    if (-not (Test-Path $catDir)) { continue }

    Get-ChildItem -Path $catDir -Directory | Where-Object {
        Test-Path (Join-Path $_.FullName ".git")
    } | ForEach-Object {
        $name = "$cat/$($_.Name)"
        $result = git -C $_.FullName -c http.proxy="" -c https.proxy="" pull --ff-only 2>&1
        if ($LASTEXITCODE -eq 0) {
            if ($result -match "Already up to date") {
                Write-Host "  $name" -ForegroundColor DarkGray
            } else {
                Write-Host "  $name (updated)" -ForegroundColor Green
            }
        } else {
            Write-Host "  $name FAILED" -ForegroundColor Red
        }
    }
}
