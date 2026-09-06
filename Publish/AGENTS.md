# Publish Category Instructions

## Scope and Inheritance

This file governs publication production projects. Read `../AGENTS.md`,
relevant `../CONVENTIONS.md` sections, and the project's `AGENTS.md` and README.
This category instruction is owned by `workspace-meta`; projects are independent.

## Role and Structure

- Each project identifies its editable manuscript or packaging authority,
  journal/arXiv entry points, research-data counterpart, and version ledger.
- Separate working manuscripts, private reviews, build output, derived upload
  bundles, and immutable submitted/uploaded snapshots.
- Preserve existing journal/style filenames, bibliography assets, and package
  entry points. A source bundle may need files ignored by a normal working build.
- A packaging-only project imports scientific changes from its declared source
  authority and records the source commit; it is not a second manuscript master.

## Versions and Evidence

- Never edit frozen submission/release contents or relabel a later revision as
  the exact submitted version. Create a new identified snapshot with a manifest.
- Record sources, code/data revisions, package hashes, build command, and actual
  delivery status. Prepared, submitted, accepted, and published are distinct.
- Verify an upload bundle by building from a clean extraction. Exclude private
  notes, reviewer material, local paths, caches, and unrelated files.
- Manuscript figures/tables retain links to their generating evidence.
- Keep projects private unless publication is explicitly authorized. Committing
  manuscript work is not permission to upload it or change repository visibility.
