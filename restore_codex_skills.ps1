<#
.SYNOPSIS
    Restore user-installed Codex skills from a trusted drive backup.
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$BackupPath
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$source = [IO.Path]::GetFullPath($BackupPath)
$destination = Join-Path ([Environment]::GetFolderPath("UserProfile")) ".codex\skills"

if (-not (Test-Path -LiteralPath $source -PathType Container)) {
    throw "Skill backup is missing: $source"
}

New-Item -ItemType Directory -Path $destination -Force | Out-Null

& robocopy $source $destination /E /COPY:DAT /DCOPY:DAT /R:2 /W:1 /XJ /SL /FFT /MT:8 /NP /NFL /NDL /XD .system .git __pycache__ .pytest_cache
$code = $LASTEXITCODE
if ($code -ge 8) {
    throw "Skill restore failed with robocopy exit code $code."
}

Write-Host "User skills restored to $destination" -ForegroundColor Green
Write-Host "The .system directory was not replaced. Restart Codex before using restored skills."
