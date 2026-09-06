# Experimental Category Instructions

## Scope and Inheritance

Read `../AGENTS.md`, relevant `../CONVENTIONS.md` sections, and each project's
`AGENTS.md` and README. This file is owned by `workspace-meta`.

## Role and Structure

- Use a small structure suited to the question: a note, prototype, configuration,
  and recorded results may be enough. Add paper/package layers when needed.
- A monorepo may contain self-contained research subprojects. Use a local
  `AGENTS.md` for distinct subproject contracts without creating nested Git roots.
- Keep exploratory code, reusable components, experiment records, and temporary
  builds distinct. Preserve existing directory and version names for provenance.

## Evidence and Promotion

- Label observations, hypotheses, negative results, and proved statements
  separately. P0 verdicts and smoke results are not paper-grade conclusions.
- Use fresh output locations; retain actual commands, seeds, budgets,
  environments, and failure records needed to interpret an experiment.
- Promotion to Research or Publish requires a declared authority, reproducible
  evidence, and updated references; moving a directory does not certify a result.
- Preserve local-only/manual-transfer status until repository/remote creation
  is authorized. Third-party checkouts keep their upstream names and licenses
  and are outside workspace policy rewrites and ordinary synchronization.
