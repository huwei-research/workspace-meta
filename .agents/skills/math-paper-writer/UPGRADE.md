# Upgrade Guide

## From v2.2 to v2.3

Version 2.3 adds Lean/Lake environment integration checks. If a project includes
a reusable Lean environment or local libraries such as `mathlib` or `optlib`,
run:

```bash
python .agents/skills/math-paper-writer/scripts/check_lean_environment.py path/to/lean/project
```

Use `--run-build` only when the requested Lean toolchain is installed and a
real `lake build` should be attempted.

If the workspace provides a `lean-library-registry.yaml`, registered libraries
can be selected without spelling out their paths:

```bash
python .agents/skills/math-paper-writer/scripts/check_lean_environment.py --library optlib --allow-sorry --require-toolchain-installed --run-build --build-target Optlib
```

## From v2.1 to v2.2

Version 2.2 adds formal-verification readiness and Lean artifact hygiene checks.
If a project includes Lean files, run:

```bash
python .agents/skills/math-paper-writer/scripts/check_lean_project.py path/to/lean/project
```

## From v2.0 to v2.1

Version 2.1 is a publish-clean release. It removes local source paths and
development-facing reference-learning ledger/checker surfaces from the public
skill interface, while preserving the learned writing principles as general
reference-material calibration and field adaptation.

## From v1.1 to v2.0

Version 2.0 adds source-backed learning and stricter readiness gates. Existing
manuscript workflows still work, but new tasks may create these optional files:

- `reference-calibration-notes.md`
- `source-cards.md` or per-source cards
- `gate-review.md`

Recommended first checks after upgrading:

```bash
python .agents/skills/math-paper-writer/scripts/run_all_checks.py main.tex --bib refs.bib --claim-ledger claim-evidence-ledger.md
```

## From v0.1 or v0.2

Back up the old skill and install the current integrated release:

```bash
cd /path/to/your-paper-project
mkdir -p .agents/skills
if [ -d .agents/skills/math-paper-writer ]; then
  mv .agents/skills/math-paper-writer .agents/skills/math-paper-writer.backup
fi
unzip math-paper-writer-skill-v2.3.zip -d .agents/skills
test -f .agents/skills/math-paper-writer/SKILL.md
```

Version 1.0 and later no longer organize the skill as a rigid page-by-page
coverage matrix. The content has been internalized into `SKILL.md`, task
playbooks, reference protocols, templates, scripts, and eval cases.

## After upgrading

Run one proof audit, one introduction review, and one claim/source audit before
using the skill for full-manuscript editing. This confirms that Codex loads the
integrated protocols.
