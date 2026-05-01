param(
    [switch] $Check
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$source = Join-Path $repoRoot "xskill"

$targets = @(
    "install/codex/.agents/skills/xskill/references/xskill",
    "install/claude-code/.claude/skills/xskill/references/xskill",
    "install/gemini-cli/xskill/xskill",
    "install/github-copilot-cli/xskill"
)

function Get-RelativePath {
    param([string] $Path)
    return $Path.Substring($repoRoot.Length + 1)
}

function Compare-Directory {
    param(
        [string] $Left,
        [string] $Right
    )

    $leftFiles = Get-ChildItem -Path $Left -Recurse -File | ForEach-Object {
        $_.FullName.Substring($Left.Length + 1)
    } | Sort-Object

    $rightFiles = Get-ChildItem -Path $Right -Recurse -File | ForEach-Object {
        $_.FullName.Substring($Right.Length + 1)
    } | Sort-Object

    $leftList = [string]::Join("`n", $leftFiles)
    $rightList = [string]::Join("`n", $rightFiles)
    if ($leftList -ne $rightList) {
        return $false
    }

    foreach ($relative in $leftFiles) {
        $leftPath = Join-Path $Left $relative
        $rightPath = Join-Path $Right $relative
        if ((Get-FileHash -Algorithm SHA256 -Path $leftPath).Hash -ne (Get-FileHash -Algorithm SHA256 -Path $rightPath).Hash) {
            return $false
        }
    }

    return $true
}

if (-not (Test-Path -LiteralPath $source)) {
    throw "Missing source directory: $source"
}

foreach ($targetRelative in $targets) {
    $target = Join-Path $repoRoot $targetRelative

    if ($Check) {
        if (-not (Test-Path -LiteralPath $target)) {
            throw "Missing generated install-pack copy: $targetRelative"
        }
        if (-not (Compare-Directory -Left $source -Right $target)) {
            throw "Generated install-pack copy is out of sync: $targetRelative"
        }
        Write-Host "ok: $(Get-RelativePath -Path $target)"
        continue
    }

    if (Test-Path -LiteralPath $target) {
        Remove-Item -LiteralPath $target -Recurse -Force
    }

    $parent = Split-Path -Parent $target
    New-Item -ItemType Directory -Path $parent -Force | Out-Null
    Copy-Item -Path $source -Destination $parent -Recurse -Force
    Write-Host "synced: $(Get-RelativePath -Path $target)"
}

$copyPasteSource = Join-Path $repoRoot "xskill-copy-paste.md"
$copyPasteTarget = Join-Path $repoRoot "dist/xskill-copy-paste.md"

if ($Check) {
    if (-not (Test-Path -LiteralPath $copyPasteTarget)) {
        throw "Missing generated copy-paste fallback: dist/xskill-copy-paste.md"
    }
    if ((Get-FileHash -Algorithm SHA256 -Path $copyPasteSource).Hash -ne (Get-FileHash -Algorithm SHA256 -Path $copyPasteTarget).Hash) {
        throw "Generated copy-paste fallback is out of sync: dist/xskill-copy-paste.md"
    }
    Write-Host "ok: dist/xskill-copy-paste.md"
} else {
    New-Item -ItemType Directory -Path (Split-Path -Parent $copyPasteTarget) -Force | Out-Null
    Copy-Item -Path $copyPasteSource -Destination $copyPasteTarget -Force
    Write-Host "synced: dist/xskill-copy-paste.md"
}
