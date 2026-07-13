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

Private documents, local archives, ignored experiment outputs, and global user
skills require a trusted-drive transfer in addition to Git. Use
`inventory_transfer.ps1` to generate path manifests, `export_workspace.ps1` to
copy the workspace, `verify_transfer.ps1` to check the copy, and
`restore_codex_skills.ps1` to restore user-installed skills on another
computer.

See `SYNC_GUIDE.md` for the full workflow and `CONVENTIONS.md` for project,
file, experiment, and publication conventions. See `TRANSFER_GUIDE.md` for the
manual-drive workflow and privacy boundaries. See `SKILLS_SYNC.md` for the
workspace, global, and plugin skill restore model.
