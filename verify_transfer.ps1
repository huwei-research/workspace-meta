<#
.SYNOPSIS
    Compare a drive export against the current workspace without changing it.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$Destination,

    [ValidateSet("Exact", "Portable")]
    [string]$Mode = "Exact",

    [switch]$IncludeGlobalSkills
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$sourceRoot = [IO.Path]::GetFullPath($PSScriptRoot)
$destinationRoot = [IO.Path]::GetFullPath($Destination)
$workspaceDestination = Join-Path $destinationRoot "2026Projects"

if (-not (Test-Path -LiteralPath $workspaceDestination -PathType Container)) {
    throw "Transferred workspace is missing: $workspaceDestination"
}

function Test-RobocopyParity {
    param([string[]]$Arguments, [string]$Label)

    Write-Host "=== $Label ===" -ForegroundColor Cyan
    & robocopy @Arguments
    $code = $LASTEXITCODE
    $sourceDifferences = (($code -band 1) -ne 0) -or (($code -band 4) -ne 0)
    if ($code -ge 8 -or $sourceDifferences) {
        throw "$Label failed parity verification with robocopy exit code $code."
    }
    if (($code -band 2) -ne 0) {
        Write-Host "$Label contains extra destination files; source files still match." -ForegroundColor Yellow
    } else {
        Write-Host "$Label matches the source." -ForegroundColor Green
    }
}

$workspaceArguments = @(
    $sourceRoot,
    $workspaceDestination,
    "/L",
    "/E",
    "/COPY:DAT",
    "/DCOPY:DAT",
    "/R:0",
    "/W:0",
    "/XJ",
    "/SL",
    "/FFT",
    "/NP",
    "/NFL",
    "/NDL",
    "/NJH"
)

$excludedDirectories = @(
    (Join-Path $sourceRoot "Research\MemOTRO\codes\.pytest_cache")
)
if ($Mode -eq "Portable") {
    $excludedDirectories += @(
        ".venv",
        "venv",
        "node_modules",
        ".lake",
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        ".ruff_cache",
        ".codex_tmp"
    )
    $workspaceArguments += @(
        "/XF",
        "*.pyc",
        "*.pyo",
        "Thumbs.db",
        ".DS_Store"
    )
}
$workspaceArguments += @("/XD")
$workspaceArguments += $excludedDirectories

Test-RobocopyParity -Arguments $workspaceArguments -Label "Workspace $Mode transfer"

if ($IncludeGlobalSkills) {
    $globalSkills = Join-Path ([Environment]::GetFolderPath("UserProfile")) ".codex\skills"
    $skillsDestination = Join-Path $destinationRoot "CodexProfile\user-skills"
    if (-not (Test-Path -LiteralPath $skillsDestination -PathType Container)) {
        throw "Transferred user skills are missing: $skillsDestination"
    }

    $skillsArguments = @(
        $globalSkills,
        $skillsDestination,
        "/L",
        "/E",
        "/COPY:DAT",
        "/DCOPY:DAT",
        "/R:0",
        "/W:0",
        "/XJ",
        "/SL",
        "/FFT",
        "/NP",
        "/NFL",
        "/NDL",
        "/NJH",
        "/XD",
        ".system",
        ".git",
        "__pycache__",
        ".pytest_cache"
    )
    Test-RobocopyParity -Arguments $skillsArguments -Label "Codex user-skills transfer"
}

Write-Host "Transfer verification complete." -ForegroundColor Green
