# Math Paper Writer Skill v2.3

A Codex skill for rigorous mathematical-paper writing across pure mathematics, applied mathematics, probability/statistics, numerical analysis, optimization, theoretical computer science, computational mathematics, and interdisciplinary mathematical science.

It supports drafting, revision, proof auditing, formal-verification readiness checks, Lean artifact hygiene checks, notation review, claim-evidence auditing, literature/citation-context verification, numerical-experiment reporting, bibliography checking, long-horizon manuscript state tracking, controlled external-skill collaboration, manuscript gate review, reference-material calibration, and final submission preparation.

## Installation

From a GitHub checkout:

```bash
git clone https://github.com/<owner>/math-paper-writer.git ~/.codex/skills/math-paper-writer
test -f ~/.codex/skills/math-paper-writer/SKILL.md
```

Repository-level installation from a release zip:

```bash
mkdir -p .agents/skills
unzip math-paper-writer-skill-v2.3.zip -d .agents/skills
test -f .agents/skills/math-paper-writer/SKILL.md
```

User-level installation:

```bash
mkdir -p ~/.agents/skills
unzip math-paper-writer-skill-v2.3.zip -d ~/.agents/skills
test -f ~/.agents/skills/math-paper-writer/SKILL.md
```

## Typical use

```text
$math-paper-writer Audit the proof of Theorem 3.1. Check every inequality direction and hidden assumption. Do not rewrite yet.
```

```text
$math-paper-writer Check whether the Lean artifact exactly supports the manuscript theorem and whether we may claim formal verification.
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

```text
$math-paper-writer Build a claim-evidence ledger for the abstract and introduction, then identify unsupported novelty or experiment claims.
```

```text
$math-paper-writer Decide which research/citation skills to use for related-work discovery, then re-audit the resulting claims before drafting.
```

```text
$math-paper-writer Use this venue guide and these exemplar papers to calibrate style and review criteria for the revision.
```

```text
$math-paper-writer Perform a full gate review of main.tex using the mathematical manuscript rubric.
```

## Release test

```bash
python scripts/run_skill_tests.py
```

The release test validates the skill metadata, manifest, public-clean text,
Python scripts, and representative heuristic checks.

## Package

```bash
python scripts/package_skill.py
```

The package script writes `dist/math-paper-writer-skill-v<VERSION>.zip` using
`manifest.txt`.

## Lean and formal-verification checks

For a Lean/Lake project:

```bash
python scripts/check_lean_project.py path/to/project
python scripts/check_lean_environment.py path/to/project
```

For a workspace with a `lean-library-registry.yaml`, the checker can resolve a
registered library and build a specific target:

```bash
python scripts/check_lean_environment.py --library optlib --allow-sorry --require-toolchain-installed
python scripts/check_lean_environment.py --library optlib --allow-sorry --require-toolchain-installed --run-build --build-target +Optlib.Algorithm.SubgradientMethod
```

The project checker scans Lean files for trust-boundary risks. The environment
checker additionally inspects `lean-toolchain`, `lakefile.lean` or
`lakefile.toml`, `lake-manifest.json`, and installed Lake package revisions. It
does not claim a build passed unless `--run-build` is supplied and `lake build`
actually succeeds.

## Design principles

- Mathematical truth is prior to style.
- Story structure is prior to sentence polishing.
- Proof audit is separate from proof rewriting.
- Formal verification claims require exact statement alignment, toolchain record, successful build, and no unresolved placeholders.
- Equations and symbols are parts of prose.
- Notation should reduce reader burden.
- Citations must carry narrative function.
- Experiments must be interpretable and reproducible.
- External research, citation, style, visualization, and slide skills are support tools, not authorities on mathematical truth.
- Central claims should be traceable to proofs, experiments, citations, computations, or explicit limitations.
- Reference-material advice must become operational manuscript rules, not slogans.
- Literature claims require source-context alignment, not only bibliography entries.
- Field conventions matter; algebra, analysis, probability, numerical analysis, and theoretical computer science should not be forced into one house style.
- Final review must be multi-pass, not one broad skim.

## Files

- `SKILL.md`: invocation, task classification, global workflow, and output protocols.
- `references/`: integrated writing doctrine and detailed rules.
- `playbooks/`: task-specific execution procedures.
- `assets/`: reusable templates for contracts, outlines, audits, and revision reports.
- `scripts/`: heuristic deterministic checks for manuscripts and bibliography files.
- `evals/`: small fixtures and expected diagnoses for regression testing the skill.

## Version

`2.3.0` adds Lean/Lake environment integration checks for local `mathlib`,
`optlib`, and other formalization projects while preserving the publish-clean
cross-field release structure.
