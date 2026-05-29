# Workspace Sync Guide

Complete instructions for replicating the `huwei-research` workspace on any machine.

## Prerequisites

| Tool | Version | Install (Windows) |
|------|---------|-------------------|
| Git | 2.40+ | `winget install Git.Git` |
| Python | 3.10+ | `winget install Python.Python.3.12` |
| GitHub CLI | 2.40+ | `winget install GitHub.cli` |
| TeX Live | 2024+ | Manual install from tug.org |
| Cursor | Latest | cursor.com |

## Quick Start

```bash
# 1. Authenticate
gh auth login
gh auth setup-git

# 2. Create workspace
mkdir -p ~/2026Projects/{Research,Publish,Public,Experimental,Personal}
cd ~/2026Projects

# 3. Clone everything
ORG=huwei-research

for repo in BUPTR MATRO STARTRO RITRO MemOTRO BARN RSSM; do
  git clone https://github.com/$ORG/$repo.git Research/$repo
done

git clone https://github.com/$ORG/DisGRem-paper.git Publish/DisGRem-paper
git clone https://github.com/$ORG/ArXiv.git Publish/ArXiv
git clone https://github.com/$ORG/DisGRem.git Public/DisGRem

for repo in QuasiNewton SelfCorrecting; do
  git clone https://github.com/$ORG/$repo.git Experimental/$repo
done

git clone https://github.com/$ORG/Weihu-resume.git Personal/Weihu-resume

# 4. Install Python environments
find . -path "*/codes/requirements.txt" -exec sh -c '
  dir=$(dirname "{}"); cd "$dir" && python -m venv .venv &&
  . .venv/bin/activate && pip install -r requirements.txt && deactivate
' \;

# 5. Regenerate figures
cd Research/BUPTR/codes && python scripts/replot_from_csv.py && cd -
cd Public/DisGRem/codes && python scripts/replot.py && cd -
```

## Windows PowerShell Equivalent

```powershell
$org = "huwei-research"
$root = "D:\Desktop\2026Projects"

# Create structure
"Research","Publish","Public","Experimental","Personal" | ForEach-Object {
    New-Item -ItemType Directory -Force -Path "$root\$_"
}

Set-Location $root

# Clone Research
@('BUPTR','MATRO','STARTRO','RITRO','MemOTRO','BARN','RSSM') | ForEach-Object {
    git clone "https://github.com/$org/$_.git" "Research\$_"
}

# Clone Publish
git clone "https://github.com/$org/DisGRem-paper.git" "Publish\DisGRem-paper"
git clone "https://github.com/$org/ArXiv.git" "Publish\ArXiv"

# Clone Public
git clone "https://github.com/$org/DisGRem.git" "Public\DisGRem"

# Clone Experimental
@('QuasiNewton','SelfCorrecting') | ForEach-Object {
    git clone "https://github.com/$org/$_.git" "Experimental\$_"
}

# Clone Personal
git clone "https://github.com/$org/Weihu-resume.git" "Personal\Weihu-resume"
```

## Proxy Configuration

For networks requiring proxy (common in China):

```bash
git config --global http.proxy  socks5h://127.0.0.1:7897
git config --global https.proxy socks5h://127.0.0.1:7897
```

Temporary bypass: `git -c http.proxy= -c https.proxy= clone/pull/push ...`

## Daily Workflow

```bash
# Pull all repos
for dir in Research/* Publish/* Public/* Experimental/* Personal/*; do
  [ -d "$dir/.git" ] && git -C "$dir" pull --ff-only
done
```

## Conventions

See `CONVENTIONS.md` at the workspace root for all naming, structure, and style rules.
See `.cursor/rules/project-conventions.mdc` for the Cursor AI rule summary.
See `.cursor/skills/project-sync/SKILL.md` for the detailed sync skill.

## Repository Inventory

| Category | Repo | Status | Description |
|----------|------|--------|-------------|
| Research | BUPTR | Active | Bayesian Uncertainty-Penalized Trust-Region for DFO |
| Research | MATRO | Active | Matrix-Adaptive Trust-Region Optimizer |
| Research | STARTRO | Active | Subspace Trust-Region with Adaptive Random Directions |
| Research | RITRO | Active | Riemannian Interpolation Trust-Region Optimizer |
| Research | MemOTRO | Active | Memory-enhanced Optimization via Trust-Region |
| Research | BARN | Active | Boundary-Aware Regularized Newton |
| Research | RSSM | Active | Random Subspace Second-order Methods |
| Publish | DisGRem-paper | Submitted | DisGRem SIOPT submission + poster |
| Publish | ArXiv | Archive | ArXiv submission packages |
| Public | DisGRem | Published | Distributed Gradient-Regularized Newton (MIT) |
| Experimental | QuasiNewton | Exploratory | Quasi-Newton and curvature compression |
| Experimental | SelfCorrecting | Exploratory | Self-correcting optimization methods |
| Personal | Weihu-resume | Maintained | Personal CV/resume |
