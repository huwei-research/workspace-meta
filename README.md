# 2026Projects workspace

This repository is the synchronization and convention layer for the independent
projects stored below `Research/`, `Publish/`, `Public/`, `Experimental/`,
`Personal/`, and `LiteratureLibrary/`.

The child projects are separate Git repositories. Do not run a workspace-root
`git add -A` expecting it to commit project work.

## Instruction and structure guide

- [AGENTS.md](AGENTS.md) defines shared boundaries and how to read each instruction layer.
- [CONVENTIONS.md](CONVENTIONS.md) owns directory, naming, version, evidence, and Git defaults.
- Category instructions define the role of [Research](Research/AGENTS.md),
  [Publish](Publish/AGENTS.md), [Public](Public/AGENTS.md),
  [Experimental](Experimental/AGENTS.md), [Personal](Personal/AGENTS.md),
  [LiteratureLibrary](LiteratureLibrary/AGENTS.md), and [Archive](Archive/AGENTS.md).
- Each project's `AGENTS.md` records actual entry points, local exceptions, and checks.
  More local instruction files add only the rules needed for their subtree.
- New projects use the [project template](.agents/templates/project_agents_template.md);
  specialized subtrees use the [subdirectory template](.agents/templates/subdirectory_agents_template.md).

The root repository tracks category instruction files; it continues to exclude
the projects and private local contents beneath those categories. A standalone
project clone has its own instructions and must not depend on private sibling
repositories for ordinary setup or tests.

## Local workspace overview

The local [workspace overview](Personal/WorkspaceManagement/2026-09-05/INDEX.md)
links the research-status snapshot, the current minimal skills profile, and reversible
desktop organization records. This directory is private and intentionally
excluded from Git; the link is available only on this computer or a trusted copy.

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
