# PROJECT Agent Instructions

Template: specialize the fields below and remove this paragraph before use.
State unavailable or undecided roles explicitly; do not invent paths, commands,
scientific results, publication status, or a remote.

## Scope and Inheritance

- This file governs this project. Read the relevant README and any instructions
  within the subtree being changed.
- When placed in `2026Projects/CATEGORY/PROJECT`, read `../../AGENTS.md`,
  `../AGENTS.md`, and relevant `../../CONVENTIONS.md` sections explicitly.
  These files may be outside automatic discovery at this independent Git root.
- For another location/worktree, locate the actual workspace before using
  relative counterpart paths. Standalone clones use this file and their README;
  missing private siblings are not a normal setup/test dependency.
- Local facts and documented exceptions specialize shared defaults. Preserve
  research integrity, raw evidence, privacy, and independent Git boundaries.
- Respect the user's enabled-skill policy; use only relevant enabled skills,
  without a mandatory pipeline or automatic reactivation.

## Project Identity

- Purpose and research/software area:
- Category and current phase, with a source for material status claims:
- Repository versus local-only package status:
- Manuscript/publication/code counterpart roles, or not applicable:

## Key Paths and Authority

Paths below are project-relative unless marked as workspace-relative.

| Role | Actual path / authority | Status |
|---|---|---|
| Main manuscript, if any | | Editable source / mirror / absent |
| Shared TeX, bibliography, and paper assets | | |
| Code/package and dependency metadata | | |
| Solver/API entry points | | |
| Experiment drivers and configurations | | |
| Formal results and reports | | |
| Scratch, build, and cache output | | Ignored |
| Plans, proof records, and reviews | | |
| Frozen releases / version ledger | | Immutable snapshots |
| External counterparts | | Explicit optional location and role |

## Organization and Versioning

- State which directories own code, paper, evidence, notes, and generated output.
- Record exceptions to the shared layout and naming defaults with their reason.
- Prefer stable working filenames and Git history; preserve existing public
  names, includes, and declared versioned manuscript entry points.
- Identify one current target per manuscript/artifact line. Mark mirrors and
  frozen snapshots explicitly and record the source of regenerated copies.
- Describe actual code-release, manuscript, experiment, and submission versions.
  Existing version ledgers take priority over creating duplicate metadata.

## Mathematical and Research Rules

- State the assumptions, domains, constants, notation, and algorithm distinctions
  that require care. For software-only projects, state evidence/claim boundaries.
- Distinguish proved, observed, interpreted, and open claims.
- Preserve labels, quantifiers, inequalities, raw data, and negative results.
- Check affected dependencies before changing a mathematical result.

## Verification

For each implemented command state its starting directory, dependencies,
purpose, expected cost, and whether it writes results. Include the narrowest
useful check, relevant build, and separately labeled full experiment/release
checks. Planned or missing checks are gaps, not runnable readiness evidence.
Documentation-only edits need reference and diff checks, not a default full run.

## Results and Artifact Policy

- Identify formal, exploratory, scratch, archival, and public-release artifacts.
- Record exact code state, configuration, environment, command, seeds, budgets,
  stopping rules, failures, raw-data location, and plotting lineage for formal runs.
- Preserve raw data and frozen packages; use a new run/output ID for reruns.
- Define tracking exceptions for paper figures, PDFs, large data, or source bundles.
- For a project without experiments, state that this policy is not applicable.

## Git and Privacy

- Inspect the actual repository/worktree status before staging named task paths.
  Preserve unrelated user changes; commit independently in this repository.
- Push only within user-authorized scope after checking the remote, branch,
  visibility, and outgoing commits. Do not publish private material implicitly.
- State any local-only, manual-transfer, shared-remote, or release exclusions.
- Do not create a remote, change visibility, rewrite history, or delete source
  evidence as a side effect of ordinary cleanup.
