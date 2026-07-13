# Changelog

## 2.3.0

- Added a Lean/Lake environment checker for toolchain records, Lake project files, manifest package installation, pinned revision matching, and optional real builds.
- Added local Lean library registry resolution so checks can automatically select registered libraries such as `optlib`.
- Added target-specific Lean builds through `--build-target`, including unified-runner support.
- Added a Lean environment report template for reusable mathlib/optlib-style local libraries.
- Integrated Lean environment checks into the unified runner and release tests.
- Clarified that installed formal libraries must be version-locked and build-checked before supporting manuscript formal-verification claims.

## 2.2.0

- Added formal verification protocol for Lean/Coq/Isabelle/Agda artifacts and machine-checked manuscript claims.
- Added formal verification audit playbook and report template.
- Added Lean artifact trust-boundary checker for `sorry`, `admit`, new axioms/constants, unsafe code, and missing project metadata.
- Integrated formalization readiness into theorem/proof audit output.
- Extended release tests to cover Lean artifact hygiene checks.

## 2.1.0

- Reframed the skill as a publish-clean, cross-field mathematical writing skill.
- Replaced development-facing source-learning surfaces with reference-material calibration and internalized writing principles.
- Added field adaptation guidance for pure mathematics, applied mathematics, probability/statistics, numerical analysis, optimization, theoretical computer science, computational mathematics, and interdisciplinary mathematical science.
- Generalized external-skill routing by capability category instead of local installed skill names.
- Removed reference-learning ledger/checker workflow from the public command surface.
- Added a self-contained release test for metadata, manifest, public-clean text, scripts, and representative behavior.
- Added a manifest-based release packaging script.

## 2.0.0

- Added close-reading support for writing guides, reviewer reports, and exemplar papers.
- Integrated core mathematical-writing principles for sentence/symbol discipline, theorem contracts, story structure, citation context, experiment reporting, revision, and proofreading.
- Added literature/citation-context protocol with math source cards and claim-reference alignment verdicts.
- Added full-manuscript gate-review rubric with severity levels, dimension scores, and readiness verdicts.
- Added reference-learning notes, source-card, and rubric templates.
- Added playbooks for deep source reading, literature-context audit, and full manuscript gate review.
- Added validation support for reference-learning notes.
- Strengthened manuscript heuristics for weak evidence phrases and evidence-bearing words.
- Normalized external-skill output into source cards, claim ledgers, review findings, experiment obligations, and style rules.

## 1.1.0

- Added controlled external-skill collaboration rules so research, citation, visualization, slide, and style skills can support mathematical manuscripts without overriding integrity checks.
- Added claim-evidence integrity protocol, ledger template, audit playbook, and heuristic claim extraction/checking scripts.
- Added research-state protocol and manuscript passport templates for long-horizon paper continuity.
- Added mathematical author-style calibration protocol, template, and playbook.
- Added mode spectrum for fidelity, balanced, and originality tasks.
- Extended the unified check runner with optional claim-ledger validation.

## 1.0.0

- Reorganized the skill from a source-mapping prototype into an integrated mathematical-writing system.
- Removed the rigid coverage matrix from the user-facing package.
- Added a unified doctrine connecting story, reader contract, theorem contract, proof audit, notation, prose, experiments, revision, and production.
- Expanded proof-audit rules for equality, inequality, implication, equivalence, quantifiers, domains, statements vs expressions, and isolated equation chains.
- Expanded English-style rules for mathematical prose, including articles, singular/plural agreement, word forms, word order, confused words, dangling participles, parallel enumeration, naked demonstratives, double negatives, and concise active wording.
- Expanded numerical-experiment and reproducibility protocols.
- Added task playbooks for drafting, introduction review, theorem/proof audit, experiment audit, revision, and final submission.
- Added improved heuristic scripts and a unified runner.
- Added additional eval fixtures covering story, proof, symbols, usage, experiments, bibliography, and derivative-free optimization writing.

## 0.2.0

- Added source-to-rule coverage matrix, reference files, templates, scripts, and eval fixtures.

## 0.1.0

- Initial prototype for mathematical-paper writing and proof auditing.
