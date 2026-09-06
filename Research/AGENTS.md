# Research Category Instructions

## Scope and Inheritance

This file governs active research projects under this category. Read the
workspace `../AGENTS.md` and relevant `../CONVENTIONS.md` sections, then the
target project's `AGENTS.md` and README. This file belongs to `workspace-meta`;
each project or Git worktree retains its independent repository boundary.

## Role and Structure

- Keep theory, reusable code, experimental evidence, and working manuscripts
  in the locations declared by each project. Existing root-package, C++, and
  monorepo layouts are valid; create only the directories needed.
- Declare the editable manuscript authority and any Publish/Public counterparts.
  If Publish owns publication sources, a Research paper mirror is archival or
  derived. If research and submission lines coexist, distinguish their roles.
- Keep plans, reviews, build outputs, scratch runs, and formal evidence distinct.
  A folder name or a passed smoke test does not establish a scientific claim.

## Evidence and Handoffs

- Preserve proof assumptions, raw data, negative results, and source lineage.
  Formal runs follow the project's report/configuration and freeze contracts.
- Use Git for working changes. Preserve established versioned entry points and
  record an explicit current target before starting a manuscript revision.
- Publication packaging and code release are deliberate transfers with recorded
  source revisions; never synchronize entire research trees into public code.
- Research contents are private by default. Check remote visibility, including
  shared research/release remotes; a branch name is not access control.
- Local-only projects remain local unless a remote is explicitly authorized.
