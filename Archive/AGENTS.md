# Archive Category Instructions

## Scope and Inheritance

Read `../AGENTS.md` and the archive guidance in `../CONVENTIONS.md`.
This instruction file belongs to `workspace-meta`. Archive contents remain
local and excluded from normal synchronization.

## Preservation

- Archives store historical snapshots, superseded workspace records, and
  provenance. They are not editable current project authorities.
- Preserve snapshot filenames, source bytes, hashes, manifests, and copied
  instructions. Embedded `AGENTS.md` files describe their historical snapshot;
  do not apply them to active sibling projects or normalize their contents.
- For a new archived item, record the originating project, source revision,
  reason, date/time, and the current authority or superseding artifact.
- Use the existing category/date hierarchy. New snapshot IDs should be
  descriptive and dated; avoid unexplained `old` or `final` copies.
- Restore by copying to an explicitly chosen working destination with provenance.
  Do not edit the preserved original to make a restoration or build succeed.
- Follow `../TRANSFER_GUIDE.md` for trusted transfers. Cleanup does not authorize
  deletion, remote publication, worktree pruning, or movement across Git boundaries.
