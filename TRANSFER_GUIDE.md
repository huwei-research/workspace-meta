# Manual Transfer Guide

This guide complements Git synchronization. It covers private documents,
ignored research outputs, local archives, experimental packages, and user
skills that are intentionally outside normal repository cloning.

## What is synchronized by Git

`workspace-repos.json` defines 23 managed worktrees. These repositories can be
recreated with `setup.ps1` and checked with `sync_all.ps1`.

The workspace-local skills `math-paper-writer` and `research-orchestrator` are
tracked by `workspace-meta`. The private `weihu-resume-writer` source is tracked
in `Personal/Weihu-resume` and installed into the workspace by `setup.ps1`.

## What requires a trusted drive

- `Personal/PrivateDocuments/`
- `Personal/AIContext/`
- `Personal/SkillBackups/`
- `Archive/`
- `Experimental/MetricizedMuonP0/`
- ignored raw or expensive-to-regenerate outputs inside managed repositories
- optional external Lean toolchains and checkouts under
  `Experimental/lean-libraries/`
- user-installed skills from `%USERPROFILE%\.codex\skills`, excluding the
  version-managed `.system` directory

Do not copy Codex authentication files, browser sessions, or plugin credentials.
Reauthenticate plugins and connectors on the destination computer.

## Recommended exact-drive transfer

Generate a path inventory first:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ./inventory_transfer.ps1 -IncludeGitMetadata
```

Copy everything, including repository metadata and rebuildable environments:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ./export_workspace.ps1 `
  -Destination 'E:\CodexTransfer' -Mode Exact -IncludeGlobalSkills
```

One ignored pytest cache at `Research/MemOTRO/codes/.pytest_cache` has an
inherited ACL that denies the current user access. Both inventory and export
skip this rebuildable cache; it contains no project source or research result.

For a smaller but still usable workspace, omit virtual environments, package
caches, Lean build directories, and Python caches:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ./export_workspace.ps1 `
  -Destination 'E:\CodexTransfer' -Mode Portable -IncludeGlobalSkills
```

Both modes retain Git metadata. `Portable` may need dependency and LFS restores
before experiments run.

## Verify the drive copy

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ./verify_transfer.ps1 `
  -Destination 'E:\CodexTransfer' -Mode Exact -IncludeGlobalSkills
```

Use the same mode for export and verification.

## Restore on another computer

1. Copy `E:\CodexTransfer\2026Projects` to the intended local path.
2. Run `setup.ps1 -SkipVenv`; existing repositories will be checked rather than
   cloned again.
3. Run `sync_all.ps1 -Action Status`.
4. Restore user skills:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File ./restore_codex_skills.ps1 `
  -BackupPath 'E:\CodexTransfer\CodexProfile\user-skills'
```

5. Reinstall plugins through Codex and sign in again where required.
6. Rebuild omitted environments when `Portable` mode was used.

Never delete the source copy until `verify_transfer.ps1` succeeds and several
important private PDFs and research outputs open correctly on the destination.
