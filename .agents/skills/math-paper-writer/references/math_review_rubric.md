# Mathematical Manuscript Review Rubric

Use this reference for full-paper review, gate review before submission,
reviewer-style critique, or deciding whether a draft is ready for polishing.

## Severity scale

- `P0 blocking`: likely false, unproved, source-distorting, unreproducible, or
  publication-threatening. Do not polish around it.
- `P1 major`: important gap or ambiguity that can mislead readers or reviewers.
- `P2 minor`: local clarity, wording, notation, or presentation issue.
- `P3 optional`: improvement that is useful but not necessary for readiness.

## Dimension scores

Use scores only as a diagnostic aid. A high average cannot offset a `P0`.

| Score | Meaning |
|---:|---|
| 5 | Publication-ready for this dimension. |
| 4 | Strong; only local fixes remain. |
| 3 | Usable but needs targeted revision. |
| 2 | Weak; major revision needed. |
| 1 | Unreliable or structurally incomplete. |
| 0 | Not assessable from available material. |

## Review dimensions

### 1. Mathematical correctness

Check theorem statements, proof steps, assumptions, domains, constants,
quantifier order, inequalities, implications, equivalences, and limit passages.
Any suspected false theorem, invalid proof step, or hidden assumption is at
least `P0` or `P1`.

### 2. Theorem/result contract

Each main result should state objects, setting, assumptions, conclusion,
dependencies, scope, probability mode if any, novelty relative to prior work,
and limitations.

### 3. Proof traceability

Proofs should have a readable path. Long proofs need roadmaps; equation chains
need prose; each transition should be classifiable as definition, assumption,
lemma, equality, inequality, implication, equivalence, limit passage, or case
split.

### 4. Claim-evidence integrity

Title, abstract, introduction, contributions, conclusion, and experiment
discussion must be supported by proofs, experiments, citations, computations,
or explicit limitations. Novelty and comparison claims require source checks.

### 5. Literature and citation accuracy

Related work should be organized by ideas and accurately represent each source.
Bibliography metadata, citation anchors, and source contexts must be checked.

### 6. Notation and symbol grammar

Notation should reduce memory burden. Symbols must have stable meanings,
definitions must precede use, and equations/symbols must be grammatically and
logically correct.

### 7. Narrative architecture

The paper should guide the reader from problem to gap to approach to result to
mechanism to scope. Definitions and assumptions should appear when needed.
Section order should reduce reader resistance.

### 8. Experiments and reproducibility

Numerical claims require reproducibility details, fair baselines, metrics,
budgets, seeds or randomness policy, environment information, and honest
interpretation of tables and figures.

### 9. Mathematical English and readability

Sentences should begin with clear subjects and verbs when possible. Equations
should be part of sentences. Avoid unnecessary intensifiers, ambiguous `any`,
naked `This`, dangling modifiers, weak openings, and over-compressed prose.

### 10. Production readiness

Check LaTeX labels, references, theorem numbering, bibliography, figures,
tables, appendices, generated artifacts, submission package, and final
proofreading.

## Gate verdicts

- `READY`: no `P0`, no unresolved central `P1`, and all required evidence is
  checked.
- `READY_AFTER_LOCAL_FIXES`: no `P0`; remaining `P1` items are narrow and
  explicitly fixable.
- `NOT_READY`: at least one `P0` or several unresolved central `P1` items.
- `INSUFFICIENT_MATERIAL`: the manuscript, sources, or experiment artifacts are
  not available enough to judge readiness.

## Review output

Lead with findings ordered by severity. For each finding include:

- location;
- issue;
- why it matters;
- evidence or missing evidence;
- safe fix.

After findings, include dimension scores, gate verdict, and the shortest safe
revision plan.
