# Math Paper Writer Skill v1.0

A Codex skill for rigorous mathematical-paper writing, revision, proof auditing, notation review, numerical-experiment reporting, bibliography checking, and final submission preparation.

This is a synthesized, integrated skill rather than a page-by-page source map. The supporting documents are organized by how a mathematical writer works: build a story, state results, write proofs, choose notation, integrate equations with prose, report experiments, revise, and submit.

## Installation

Repository-level installation:

```bash
mkdir -p .agents/skills
unzip math-paper-writer-skill-v1.0-integrated.zip -d .agents/skills
test -f .agents/skills/math-paper-writer/SKILL.md
```

User-level installation:

```bash
mkdir -p ~/.agents/skills
unzip math-paper-writer-skill-v1.0-integrated.zip -d ~/.agents/skills
test -f ~/.agents/skills/math-paper-writer/SKILL.md
```

## Typical use

```text
$math-paper-writer Audit the proof of Theorem 3.1. Check every inequality direction and hidden assumption. Do not rewrite yet.
```

```text
$math-paper-writer Review the introduction and related work in main.tex. Check whether the prior work is integrated into the story rather than dumped.
```

```text
$math-paper-writer Review the numerical experiments section for reproducibility, overclaiming, and table/figure design.
```

```text
$math-paper-writer Perform a six-pass final review of main.tex before submission.
```

## Design principles

- Mathematical truth is prior to style.
- Story structure is prior to sentence polishing.
- Proof audit is separate from proof rewriting.
- Equations and symbols are parts of prose.
- Notation should reduce reader burden.
- Citations must carry narrative function.
- Experiments must be interpretable and reproducible.
- Final review must be multi-pass, not one broad skim.

## Files

- `SKILL.md`: invocation, task classification, global workflow, and output protocols.
- `references/`: integrated writing doctrine and detailed rules.
- `playbooks/`: task-specific execution procedures.
- `assets/`: reusable templates for contracts, outlines, audits, and revision reports.
- `scripts/`: heuristic deterministic checks for manuscripts and bibliography files.
- `evals/`: small fixtures and expected diagnoses for regression testing the skill.

## Version

`1.0.0` is the first integrated release. It removes the rigid source-to-rule coverage table from earlier drafts and replaces it with an internalized writing manual arranged around actual authoring and reviewing tasks.
