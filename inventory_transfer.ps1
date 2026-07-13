<#
.SYNOPSIS
    Generate path, local-data, repository, and skill inventories for transfer.
#>

[CmdletBinding()]
param(
    [string]$OutputDirectory = "",
    [switch]$IncludeGitMetadata
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$root = [IO.Path]::GetFullPath($PSScriptRoot)
if (-not $OutputDirectory) {
    $stamp = Get-Date -Format "yyyyMMdd-HHmmss"
    $OutputDirectory = Join-Path $root "Personal\TransferManifests\$stamp"
}
$output = [IO.Path]::GetFullPath($OutputDirectory)

if (-not $output.StartsWith($root.TrimEnd('\') + [IO.Path]::DirectorySeparatorChar,
        [StringComparison]::OrdinalIgnoreCase)) {
    throw "Inventory output must stay inside the workspace: $output"
}

New-Item -ItemType Directory -Path $output -Force | Out-Null

$rg = Get-Command rg -ErrorAction Stop
Push-Location $root
try {
    $rgArguments = @("--files", "-uu")
    if (-not $IncludeGitMetadata) {
        $rgArguments += @("-g", "!**/.git/**")
    }
    $rgArguments += @("-g", "!Research/MemOTRO/codes/.pytest_cache/**")
    $rgArguments += @("-g", "!Personal/TransferManifests/**")
    $savedErrorAction = $ErrorActionPreference
    $ErrorActionPreference = "SilentlyContinue"
    try {
        $rawFilePaths = @(& $rg.Source @rgArguments 2>$null)
    } finally {
        $ErrorActionPreference = $savedErrorAction
    }
    $filePaths = @($rawFilePaths |
        ForEach-Object { $_.Replace('/', '\') } |
        Sort-Object -Unique)
} finally {
    Pop-Location
}

$outputRelative = $output.Substring($root.Length + 1)
$inventoryOutputNames = @(
    "all-files.txt",
    "all-directories.txt",
    "codex-user-skills.csv",
    "ignored-files-by-repository.csv",
    "inventory-summary.json",
    "manual-copy-roots.csv",
    "manual-data-files.csv"
)
$filePaths = @(
    $filePaths + @($inventoryOutputNames | ForEach-Object {
        Join-Path $outputRelative $_
    }) | Sort-Object -Unique
)

$utf8NoBom = New-Object Text.UTF8Encoding($false)
[IO.File]::WriteAllLines((Join-Path $output "all-files.txt"), $filePaths, $utf8NoBom)

$directorySet = New-Object 'Collections.Generic.HashSet[string]' ([StringComparer]::OrdinalIgnoreCase)
foreach ($path in $filePaths) {
    $directory = Split-Path -Parent $path
    while ($directory) {
        [void]$directorySet.Add($directory)
        $parent = Split-Path -Parent $directory
        if ($parent -eq $directory) { break }
        $directory = $parent
    }
}
$directoryPaths = @($directorySet) | Sort-Object
[IO.File]::WriteAllLines((Join-Path $output "all-directories.txt"), $directoryPaths, $utf8NoBom)

$inventory = Get-Content -Raw -LiteralPath (Join-Path $root "workspace-repos.json") | ConvertFrom-Json
$repoEntries = @([pscustomobject]@{ path = "." }) + @($inventory.repositories)
$ignoredRecords = New-Object Collections.Generic.List[object]
$manualDataRecords = New-Object Collections.Generic.List[object]
$regenerablePattern = '(?i)(^|[\\/])(\.git|\.venv|venv|node_modules|\.lake|__pycache__|\.pytest_cache|\.mypy_cache|\.ruff_cache|\.codex_tmp)([\\/]|$)|\.(pyc|pyo|aux|fls|fdb_latexmk|synctex\.gz|xdv)$|(^|[\\/])(Thumbs\.db|\.DS_Store)$'

foreach ($repo in $repoEntries) {
    if ($repo.path -eq ".") { continue }
    $repoPath = Join-Path $root $repo.path.Replace('/', '\')
    if (-not (Test-Path -LiteralPath (Join-Path $repoPath ".git"))) { continue }

    $savedErrorAction = $ErrorActionPreference
    $ErrorActionPreference = "SilentlyContinue"
    try {
        $ignored = @(
            git -c core.quotePath=false -C $repoPath ls-files --others --ignored --exclude-standard 2>$null
        )
    } finally {
        $ErrorActionPreference = $savedErrorAction
    }

    foreach ($relative in $ignored) {
        if (-not $relative) { continue }
        $workspaceRelative = ($repo.path.TrimEnd('/') + '/' + $relative.Replace('\', '/'))
        $fullPath = Join-Path $root $workspaceRelative.Replace('/', '\')
        $length = if (Test-Path -LiteralPath $fullPath -PathType Leaf) {
            (Get-Item -LiteralPath $fullPath -Force).Length
        } else { $null }
        $record = [pscustomobject]@{
            repository = $repo.path
            path = $workspaceRelative
            sizeBytes = $length
        }
        $ignoredRecords.Add($record)
        if ($workspaceRelative -notmatch $regenerablePattern) {
            $manualDataRecords.Add($record)
        }
    }
}

$ignoredRecords | Export-Csv -LiteralPath (Join-Path $output "ignored-files-by-repository.csv") -NoTypeInformation -Encoding UTF8
$manualDataRecords | Export-Csv -LiteralPath (Join-Path $output "manual-data-files.csv") -NoTypeInformation -Encoding UTF8

$manualRoots = @(
    [pscustomobject]@{ path="Personal/PrivateDocuments"; policy="required-private"; reason="Sensitive documents; trusted encrypted drive only." },
    [pscustomobject]@{ path="Personal/AIContext"; policy="required-private"; reason="Local personal research context." },
    [pscustomobject]@{ path="Personal/SkillBackups"; policy="required-codex-profile"; reason="Dated backup of user-installed Codex skills." },
    [pscustomobject]@{ path="Archive"; policy="optional-archive"; reason="Historical snapshots and generated artifacts." },
    [pscustomobject]@{ path="Experimental/MetricizedMuonP0"; policy="required-local-project"; reason="Local P0 project without an authorized remote." },
    [pscustomobject]@{ path="Experimental/lean-libraries"; policy="optional-offline-dependencies"; reason="External Lean checkouts, toolchains, and caches." }
)
$manualRoots | Export-Csv -LiteralPath (Join-Path $output "manual-copy-roots.csv") -NoTypeInformation -Encoding UTF8

$globalSkills = Join-Path ([Environment]::GetFolderPath("UserProfile")) ".codex\skills"
$skillRecords = if (Test-Path -LiteralPath $globalSkills -PathType Container) {
    Get-ChildItem -LiteralPath $globalSkills -Force -Directory |
        Sort-Object Name |
        ForEach-Object {
            [pscustomobject]@{
                name = $_.Name
                systemManaged = ($_.Name -eq ".system")
                hasSkillFile = Test-Path -LiteralPath (Join-Path $_.FullName "SKILL.md")
                sourcePath = $_.FullName
            }
        }
} else { @() }
$skillRecords | Export-Csv -LiteralPath (Join-Path $output "codex-user-skills.csv") -NoTypeInformation -Encoding UTF8

$summary = [ordered]@{
    generatedAt = (Get-Date).ToUniversalTime().ToString("o")
    workspace = $root
    includesGitMetadata = [bool]$IncludeGitMetadata
    fileCount = $filePaths.Count
    directoryCount = $directoryPaths.Count
    ignoredFileCount = $ignoredRecords.Count
    manualDataFileCount = $manualDataRecords.Count
    globalSkillDirectoryCount = @($skillRecords).Count
    output = $output
}
$summary | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath (Join-Path $output "inventory-summary.json") -Encoding UTF8

Write-Host "Transfer inventory created: $output" -ForegroundColor Green
$summary | Format-List
