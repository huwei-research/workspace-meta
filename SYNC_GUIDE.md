# Workspace Sync Guide

This guide reproduces the `2026Projects` workspace without mixing independent
repositories or accidentally publishing local data.

## Source of truth

`workspace-repos.json` is the only repository inventory. It records each local
path, remote URL, local branch, remote branch, visibility, and whether the entry
is currently safe to synchronize.

This matters because some paths intentionally share a remote:

| Local path | Remote branch | Purpose |
|---|---|---|
| `Research/BUPTR` | `research/master` | private research and manuscript history |
| `Public/BUPTR` | `master` | release-facing history |
| `Research/MATRO` | `research/master` | private research history |
| `Public/MATRO` | `master` | release-facing history |

Do not replace the manifest with category wildcards or a hand-written clone
loop. Those approaches clone the wrong branch for split-history projects and
miss newly added repositories.

## Prerequisites

- Git 2.40 or newer
- Windows PowerShell 5.1 or PowerShell 7
- GitHub CLI authenticated for private repositories
- Git LFS 3.x
- Python and TeX only when a target project's verification requires them

```powershell
gh auth login
gh auth setup-git
git lfs install
```

## New machine

```powershell
git clone https://github.com/huwei-research/workspace-meta.git 2026Projects
Set-Location 2026Projects
powershell -NoProfile -ExecutionPolicy Bypass -File ./setup.ps1 -SkipVenv
powershell -NoProfile -ExecutionPolicy Bypass -File ./sync_all.ps1 -Action Status
```

Omit `-SkipVenv` to create environments for repositories that have
`codes/requirements.txt`. `setup.ps1` also pulls declared Git LFS objects and
installs the personalized resume skill from the private `Personal/Weihu-resume`
repository into the ignored workspace skill directory. Use `-SkipPrivateSkills`
only when that private skill must not be installed on the target machine.

Entries marked `syncEnabled=false` are reported as `PENDING` and skipped. Use
`-IncludePending` only after the remote repository or branch has deliberately
been created.

## Daily workflow

Start with a local audit:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ./sync_all.ps1 -Action Status
```

Refresh remote references and fast-forward clean repositories:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ./sync_all.ps1 -Action Fetch
powershell -NoProfile -ExecutionPolicy Bypass -File ./sync_all.ps1 -Action Pull
```

Commit work inside each child repository. Never commit child-project changes
from the workspace root. After repositories are clean, push existing commits:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ./sync_all.ps1 -Action Push
```

The sync script never stages or commits files. Pull and push skip repositories
that are dirty, on the wrong branch, pointed at the wrong remote, missing their
declared remote branch, or not fast-forwardable.

Use `-RepoFilter 'Research/*'` or an exact path such as
`-RepoFilter 'Research/MATRO'` for a targeted setup or synchronization pass.

For a deeper read-only metadata and naming audit:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ./audit_workspace.ps1
```

Add `-DeepNaming` to scan tracked and manageable untracked path sets for case
collisions and non-canonical paper-figure names. Use `-RepoFilter 'Research/*'`
to audit one category at a time.

## Current synchronization status

As of 2026-07-13, all 23 managed Git worktrees have an enabled remote mapping.
The repositories created during the full-workspace synchronization pass are:

| Path | Default remote branch | Visibility |
|---|---|---|
| `Research/FoRN` | `master` | private |
| `Research/FROST` | `codex/frost-scaffold` | private |
| `Research/SQZO` | `codex/amortized-minimax-revision` | private |
| `Public/MathResearchHarness` | `master` | public |

Do not point `Research/MATRO` at `origin/master`: that branch is the distinct
release-facing history used by `Public/MATRO`.

## Intentionally excluded local material

- `Experimental/lean-libraries/`: third-party Lean checkouts and `.lake`
  packages; restore them from the owning Lean project's manifest.
- `Personal/AIContext/`: local-only personal context.
- workspace-root `.tmp*`, `tmp/`, review renders, application-form exports, and
  transfer packages: local artifacts, never `workspace-meta` content.
- `.agents/skills/weihu-resume-writer/` at the workspace root: ignored installed
  copy; its synchronized source belongs to the private resume repository.
- bulk raw experiment outputs that a project marks as scratch or generated:
  keep them local; synchronize curated data, reports, code, and regeneration
  commands according to the project `AGENTS.md` and `REPORT.md`.

## Proxy handling

By default the scripts bypass configured Git HTTP proxies for each network
command. To use the global Git proxy configuration, pass `-UseConfiguredProxy`
to `setup.ps1` or `sync_all.ps1`.

Example global proxy configuration:

```powershell
git config --global http.proxy socks5h://127.0.0.1:7897
git config --global https.proxy socks5h://127.0.0.1:7897
```

## Troubleshooting

- `running scripts is disabled`: invoke the script with
  `powershell -ExecutionPolicy Bypass -File ...` as shown above.
- `dubious ownership`: the sync script supplies a scoped `safe.directory` for
  each command. A fresh clone on another computer should not have this issue.
- `DIRTY`: review and commit or ignore files inside that repository; the script
  will not guess.
- `missing-remote-branch`: verify the manifest branch mapping before creating
  or pushing a branch.
- Git LFS pointer text instead of file content: run `git lfs pull` in that
  repository.
