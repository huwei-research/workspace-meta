<#
.SYNOPSIS
    Copy the complete workspace and optional user skills to a trusted drive.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$Destination,

    [ValidateSet("Exact", "Portable")]
    [string]$Mode = "Exact",

    [switch]$IncludeGlobalSkills,
    [switch]$UpdateExisting
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$sourceRoot = [IO.Path]::GetFullPath($PSScriptRoot)
$destinationRoot = [IO.Path]::GetFullPath($Destination)
$workspaceDestination = Join-Path $destinationRoot "2026Projects"
$sourcePrefix = $sourceRoot.TrimEnd('\') + [IO.Path]::DirectorySeparatorChar

if ($destinationRoot -eq $sourceRoot -or
    $destinationRoot.StartsWith($sourcePrefix, [StringComparison]::OrdinalIgnoreCase)) {
    throw "Destination must be outside the workspace: $destinationRoot"
}

if ((Test-Path -LiteralPath $workspaceDestination) -and -not $UpdateExisting) {
    $existing = @(Get-ChildItem -LiteralPath $workspaceDestination -Force -ErrorAction SilentlyContinue)
    if ($existing.Count -gt 0) {
        throw "Destination already contains a workspace. Use -UpdateExisting to refresh it."
    }
}

New-Item -ItemType Directory -Path $destinationRoot -Force | Out-Null

function Invoke-CheckedRobocopy {
    param([string[]]$Arguments, [string]$Label)

    Write-Host "=== $Label ===" -ForegroundColor Cyan
    & robocopy @Arguments
    $code = $LASTEXITCODE
    if ($code -ge 8) {
        throw "Robocopy failed for $Label with exit code $code."
    }
    Write-Host "$Label completed with robocopy exit code $code." -ForegroundColor Green
}

$workspaceArguments = @(
    $sourceRoot,
    $workspaceDestination,
    "/E",
    "/COPY:DAT",
    "/DCOPY:DAT",
    "/R:2",
    "/W:1",
    "/XJ",
    "/SL",
    "/FFT",
    "/MT:8",
    "/NP",
    "/NFL",
    "/NDL"
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

Invoke-CheckedRobocopy -Arguments $workspaceArguments -Label "Workspace $Mode export"

$skillsDestination = $null
if ($IncludeGlobalSkills) {
    $globalSkills = Join-Path ([Environment]::GetFolderPath("UserProfile")) ".codex\skills"
    if (-not (Test-Path -LiteralPath $globalSkills -PathType Container)) {
        throw "Global skills directory is missing: $globalSkills"
    }

    $skillsDestination = Join-Path $destinationRoot "CodexProfile\user-skills"
    $skillsArguments = @(
        $globalSkills,
        $skillsDestination,
        "/E",
        "/COPY:DAT",
        "/DCOPY:DAT",
        "/R:2",
        "/W:1",
        "/XJ",
        "/SL",
        "/FFT",
        "/MT:8",
        "/NP",
        "/NFL",
        "/NDL",
        "/XD",
        ".system",
        ".git",
        "__pycache__",
        ".pytest_cache"
    )
    Invoke-CheckedRobocopy -Arguments $skillsArguments -Label "Codex user-skills export"
}

$head = git -C $sourceRoot rev-parse HEAD 2>$null
if ($LASTEXITCODE -ne 0) { $head = $null }

$metadata = [ordered]@{
    generatedAt = (Get-Date).ToUniversalTime().ToString("o")
    source = $sourceRoot
    workspaceDestination = $workspaceDestination
    mode = $Mode
    workspaceHead = $head
    includedGlobalSkills = [bool]$IncludeGlobalSkills
    globalSkillsDestination = $skillsDestination
    excludesCredentials = $true
}

$metadataPath = Join-Path $destinationRoot "TRANSFER_METADATA.json"
$metadata | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $metadataPath -Encoding UTF8

Write-Host "Transfer export complete: $destinationRoot" -ForegroundColor Green
Write-Host "Run verify_transfer.ps1 with the same mode before removing any source files."
