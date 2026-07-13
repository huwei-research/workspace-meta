# 2026Projects workspace

This repository is the synchronization and convention layer for the independent
projects stored below `Research/`, `Publish/`, `Public/`, `Experimental/`,
`Personal/`, and `LiteratureLibrary/`.

The child projects are separate Git repositories. Do not run a workspace-root
`git add -A` expecting it to commit project work.

## New machine

```powershell
git clone https://github.com/huwei-research/workspace-meta.git 2026Projects
Set-Location 2026Projects
powershell -NoProfile -ExecutionPolicy Bypass -File ./setup.ps1 -SkipVenv
powershell -NoProfile -ExecutionPolicy Bypass -File ./sync_all.ps1 -Action Status
```

`workspace-repos.json` is the canonical repository and branch inventory.
`setup.ps1` clones from that manifest, including repositories that share a
remote but use separate research and release branches. `sync_all.ps1` reports
dirty, ahead, behind, branch, and remote mismatches before any pull or push.
`audit_workspace.ps1` checks required metadata and GitHub's large-blob limit;
its `-DeepNaming` mode also checks case collisions and paper-figure naming.

See `SYNC_GUIDE.md` for the full workflow and `CONVENTIONS.md` for project,
file, experiment, and publication conventions.
