# Formal Verification Protocol

Use this reference when the user asks whether a theorem or proof can be
formalized, whether a Lean/Coq/Isabelle development supports a manuscript
claim, or whether a paper may say that a result is formally verified.

This protocol is informed by Lean/mathlib practice and by mathematical
formalization work around optimization libraries such as `optlib`: the core
lesson is that a proof is not formally verified until the exact theorem
statement is represented in the proof assistant and checked by the toolchain
without trust holes.

## Verification levels

- `INFORMAL_AUDIT`: human-readable proof audit only.
- `FORMALIZATION_READY`: theorem contract is precise enough to attempt
  formalization, but no machine-checked proof is available.
- `PARTIALLY_FORMALIZED`: definitions, theorem statement, or supporting lemmas
  exist, but proof obligations remain.
- `FORMALLY_CHECKED`: exact statement compiles under a recorded toolchain with
  no `sorry`, `admit`, new untrusted axioms, or unexplained unsafe code.
- `STATEMENT_MISMATCH`: code proves a related statement, but not the manuscript
  claim.
- `NOT_READY`: missing definitions, ambiguous assumptions, or field/library
  gaps block formalization.

Do not describe a theorem as "formally verified" unless it reaches
`FORMALLY_CHECKED`.

## Statement alignment

Before trusting formal code, compare the manuscript theorem and formal theorem:

- objects and types;
- domains, topologies, norms, metrics, or algebraic structures;
- hypotheses and side conditions;
- quantifier order;
- constants and dependencies;
- conclusion strength;
- deterministic/probabilistic/asymptotic mode;
- imported definitions and theorem names.

The formal theorem may be stronger, weaker, or merely different. Record this
explicitly.

## Formalization workflow

1. Translate the theorem into a theorem contract.
2. Identify the proof assistant and library: Lean/mathlib, Coq, Isabelle/HOL,
   Agda, or another system.
3. Identify existing definitions and lemmas.
4. Draft the formal statement before attempting the proof.
5. Split the informal proof into reusable lemmas.
6. Compile continuously and use proof-state feedback to expose missing
   assumptions.
7. Remove all `sorry`/`admit` placeholders before claiming formal verification.
8. Record toolchain version, library commit or package lock, and build command.

## Library and environment integration

Treat formal libraries such as `mathlib` and domain libraries such as `optlib`
as external dependencies with recorded versions, not as vague background
knowledge. A usable local environment should record:

- repository URL or local path;
- exact commit, tag, or package-lock revision;
- `lean-toolchain` value;
- `lakefile` and `lake-manifest.json`;
- whether manifest packages are installed at pinned revisions;
- whether a build was actually run, and with which command;
- unresolved trust-boundary issues in the project and imported libraries.

Do not assume a library is compatible just because it is installed somewhere on
disk. Lean projects are version-sensitive: a current `mathlib` checkout may be
incompatible with an older project pinned to a previous Lean release. Prefer the
project's own `lake-manifest.json` and `lean-toolchain` over the newest
available library version.

## Automatic local registry workflow

When a workspace provides a `lean-library-registry.yaml`, use it before asking
the user for a path. A formal-verification request that mentions Lean, mathlib,
optlib, a Lean module, a theorem name, or whole-library usability should trigger
the local checker automatically unless the user explicitly says not to run
commands.

Recommended commands:

```bash
python .agents/skills/math-paper-writer/scripts/check_lean_environment.py --library optlib --allow-sorry --require-toolchain-installed
python .agents/skills/math-paper-writer/scripts/check_lean_environment.py --library optlib --allow-sorry --require-toolchain-installed --run-build --build-target +Optlib.Algorithm.SubgradientMethod
```

Use a target build for a specific module or theorem-bearing file. Use a full
Lake build only for whole-library usability or release claims:

```bash
lake build Optlib
```

Build success means the Lean files elaborate and produce artifacts under the
recorded toolchain. It does not erase trust-boundary issues elsewhere in the
library. A manuscript theorem reaches `FORMALLY_CHECKED` only when its exact
formal statement and dependency path build without unresolved placeholders.

## Trust boundary

Formal verification shifts trust to the proof assistant kernel, imported
libraries, toolchain, and any declared axioms. Audit:

- `sorry` or `admit`;
- new `axiom` or `constant` declarations used as theorems;
- `unsafe` code used in proof-critical paths;
- local changes to standard library assumptions;
- disabled checks or opaque automation hiding unresolved obligations;
- mismatch between compiled theorem and manuscript theorem.

For a local Lean/Lake project, use the environment checker when available:

```bash
python .agents/skills/math-paper-writer/scripts/check_lean_environment.py path/to/project
```

Use `--run-build` only when the proof-assistant toolchain is installed and a
real build should be attempted. If the build cannot run, say so explicitly
rather than reporting formal verification.

## Manuscript wording

Safe:

- `The Lean development contains a machine-checked proof of Theorem 2 under
  the assumptions stated in Section 3.`
- `The formal statement is slightly stronger/weaker in the following respect:
  ... .`
- `The accompanying code formalizes the definitions and several supporting
  lemmas, but the main theorem remains informal.`

Unsafe:

- `The result is formally verified` when only the statement or examples compile.
- `Lean proves the theorem` when the Lean theorem omits assumptions, changes
  domains, or proves a special case.
- `Verified by AI` without a proof assistant build and trust-boundary report.

## When to use external formal tools

Use a formal proof assistant or formalization skill when:

- a theorem is central and reusable;
- a proof has many hidden side conditions;
- proof state/type feedback could reveal missing assumptions;
- the manuscript claims formal verification;
- a library or artifact accompanies the paper.

Use symbolic or numerical tools only for computations, counterexample search,
or algebraic simplification. They do not replace formal proof unless their
output is independently certified in the proof assistant.
