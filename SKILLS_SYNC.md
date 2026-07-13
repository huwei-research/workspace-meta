# Skills Synchronization

Codex skills in this environment come from three different sources and should
not be backed up in the same way.

## Workspace-managed skills

| Skill | Canonical source | Restore method |
|---|---|---|
| `math-paper-writer` | `.agents/skills/math-paper-writer/` in `workspace-meta` | clone/pull the workspace |
| `research-orchestrator` | `.agents/skills/research-orchestrator/` in `workspace-meta` | clone/pull the workspace |
| `weihu-resume-writer` | `Personal/Weihu-resume/.agents/skills/weihu-resume-writer/` | run `setup.ps1` after cloning the private resume repository |

The workspace-root `weihu-resume-writer` directory is an installed ignored
copy. Its private resume repository remains the canonical source.

## User-installed global skills

`%USERPROFILE%\.codex\skills` currently contains user-installed skills that
are not a Git repository. Use `export_workspace.ps1 -IncludeGlobalSkills` to
place them under `CodexProfile/user-skills` on the trusted drive, then use
`restore_codex_skills.ps1` on the destination computer.

For direct folder copying, a dated local snapshot is also stored under
`Personal/SkillBackups/`. Its `file-manifest.csv` records the relative path,
size, and SHA-256 hash of every backed-up skill file.

The `.system` subdirectory is deliberately excluded because it belongs to the
installed Codex version and should be supplied by the destination installation.

## Plugin-provided skills

Plugin caches under `%USERPROFILE%\.codex\plugins\cache` are version-managed
artifacts. Reinstall plugins through Codex instead of copying their caches.
GitHub, Slack, email, calendar, and other connector authentication must be
performed again on the destination computer.

## Verification

`inventory_transfer.ps1` writes `codex-user-skills.csv`. Compare that inventory
after restoring the backup, restart Codex, and confirm that workspace skills
are discovered from the new `2026Projects` path.
