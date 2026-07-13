# Research State Protocol

Use this reference for long-horizon papers, multi-session projects, or research-to-paper orchestration. The goal is continuity without inventing progress.

## Recommended state files

Keep these files in the project when useful, using the project's established directories if they exist:

- `paper-state.yaml`: compact machine-readable state.
- `proof-ledger.md`: theorem/proof obligations and status.
- `claim-evidence-ledger.md`: central claims and supporting evidence.
- `reference-calibration-notes.md`: reusable guidance from venue instructions,
  writing guides, reviewer reports, or exemplar papers when durable notes are
  useful.
- `source-cards.md` or `sources/`: cards for important cited mathematical
  sources.
- `experiment-ledger.md`: experiment questions, configurations, outputs, and reproducibility notes.
- `gate-review.md`: latest rubric-based readiness review.
- `revision-log.md`: dated decisions, edits, and unresolved risks.

Use the templates in `assets/` as starting points. Do not create these files unless the user asks, the project already uses ledgers, or the manuscript task clearly needs continuity.

## Paper-state fields

Minimum useful fields:

- project and manuscript entry file;
- target venue or audience;
- working mode: `fidelity`, `balanced`, or `originality`;
- main theorem/result list;
- open proof obligations;
- open citation/source obligations;
- open source-card or reference-calibration obligations;
- open experiment obligations;
- latest readiness verdict if any;
- current strongest risks;
- next safe actions.

## Update rules

- Update state after a substantive proof audit, claim audit, experiment audit, or major structural revision.
- Record uncertainty as uncertainty; do not convert conjectures into results.
- Link claims to labels, sections, tables, figures, citation keys, or file paths.
- Link cited claims to source cards when source context is risky.
- Separate "observed" from "interpreted" in experiment notes.
- Record exact dates for external facts, source lookups, and experiment runs.

## Research-to-paper loop

1. Gather candidate material with external research skills when useful.
2. Convert candidate material into paper objects: claims, citations, definitions, theorem contracts, experiment questions, and limitations.
3. Create source cards or reference-calibration notes for material that will
   shape manuscript claims or writing rules.
4. Audit each object under this skill.
5. Draft only the subset whose evidence is ready or explicitly marked as pending.
6. Update ledgers before final prose polish.

## Anti-drift checks

Before resuming a paper after a gap, check:

- Did the main claim change?
- Did assumptions move between theorem, proof, experiment, and introduction?
- Did experiments support a narrower claim than the abstract says?
- Did related work summaries drift from source evidence?
- Did notation or labels change without updating references?

If yes, fix the ledger first, then revise prose.
