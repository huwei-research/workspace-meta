# Workspace Sync Skill

## Purpose

This skill guides the setup of a fresh machine to fully replicate the `huwei-research`
workspace. The workspace structure is stored in the `workspace-meta` repository.

## Architecture

```
2026Projects/              <- workspace-meta git repo (this repo)
+-- .cursor/rules/         <- Cursor AI rules (auto-applied)
+-- .cursor/skills/        <- Cursor skills (including this file)
+-- .agents/skills/        <- Project-local agent skills
+-- AGENTS.md              <- Workspace agent instructions
+-- CONVENTIONS.md         <- Workspace-wide coding conventions
+-- SYNC_GUIDE.md          <- Human-readable setup guide
+-- setup.ps1              <- One-click setup script
+-- sync_all.ps1           <- Daily pull script
+-- Research/              <- (gitignored) 7 active research repos
+-- Publish/               <- (gitignored) 2 publication repos
+-- Public/                <- (gitignored) 1 open-source repo
+-- Experimental/          <- (gitignored) 2 exploratory repos
+-- Personal/              <- (gitignored) 1 personal repo
```

## New Machine Setup (3 commands)

```powershell
# 1. Clone the meta repo (contains scripts, rules, conventions)
git clone https://github.com/huwei-research/workspace-meta.git D:\Desktop\2026Projects
cd D:\Desktop\2026Projects

# 2. Run setup (creates directories, clones all 13 repos, sets up venvs)
.\setup.ps1

# 3. Open in Cursor - rules and skills activate automatically
```

## Prerequisites

- Git 2.40+ (`winget install Git.Git`)
- Python 3.10+ (`winget install Python.Python.3.12`)
- GitHub CLI (`gh`) 2.40+ (`winget install GitHub.cli`)
- TeX Live 2024+ (for paper compilation)
- Network access to GitHub (proxy if needed: `socks5h://127.0.0.1:7897`)
- Authenticate first: `gh auth login && gh auth setup-git`

## Daily Sync

```powershell
cd D:\Desktop\2026Projects
.\sync_all.ps1
```

## Proxy Setup (China network)

```powershell
git config --global http.proxy  socks5h://127.0.0.1:7897
git config --global https.proxy socks5h://127.0.0.1:7897
```

Temporary bypass: `git -c http.proxy= -c https.proxy= pull`

## Adding a New Project

1. Create repo on GitHub under `huwei-research`
2. Add entry to `setup.ps1` in the correct category
3. Add entry to `SYNC_GUIDE.md` inventory table
4. Update this skill's inventory below
5. Clone locally: `git clone ... {Category}/{RepoName}`
6. Create `{Category}/{RepoName}/AGENTS.md` from
   `.agents/templates/project_agents_template.md` and specialize it
7. Commit the project-local `AGENTS.md` in the child repository
8. Commit workspace inventory/setup changes to `workspace-meta` and push

## Inventory (as of 2026-05)

| Category | Repo | Description |
|----------|------|-------------|
| Research | BUPTR | Bayesian Uncertainty-Penalized Trust-Region for DFO |
| Research | MATRO | Matrix-Adaptive Trust-Region Optimizer |
| Research | STARTRO | Subspace Trust-Region with Adaptive Random Directions |
| Research | RITRO | Riemannian Interpolation Trust-Region Optimizer |
| Research | MemOTRO | Memory-enhanced Optimization via Trust-Region |
| Research | BARN | Boundary-Aware Regularized Newton |
| Research | RSSM | Random Subspace Second-order Methods |
| Publish | DisGRem-paper | DisGRem SIOPT submission, poster, ArXiv sources |
| Publish | ArXiv | ArXiv submission packages for all projects |
| Public | DisGRem | Distributed Gradient-Regularized Newton (open-source) |
| Experimental | QuasiNewton | Quasi-Newton and curvature compression explorations |
| Experimental | SelfCorrecting | Self-correcting optimization methods |
| Personal | Weihu-resume | Personal CV/resume LaTeX sources |
