# Playbook: Formal Verification Audit

Use this playbook for Lean/Coq/Isabelle/Agda code, formalization readiness, or
manuscript claims about formal verification.

## Procedure

1. Reconstruct the manuscript theorem contract.
2. Identify the formal artifact: repository, proof assistant, toolchain,
   library versions, entry modules, and build command.
3. Compare manuscript statement with formal theorem statement.
4. Check trust boundary:
   - `sorry`/`admit`;
   - new `axiom`/unjustified `constant`;
   - unsafe proof-critical code;
   - missing toolchain lock;
   - theorem proved only for a special case.
5. If Lean files are available, run:

```bash
python .agents/skills/math-paper-writer/scripts/check_lean_project.py path/to/lean/project
```

6. If a Lake project or reusable local library environment is available, run:

```bash
python .agents/skills/math-paper-writer/scripts/check_lean_environment.py path/to/lean/project
```

If a local Lean library registry is available and the task names a registered
library such as `optlib`, resolve the path automatically:

```bash
python .agents/skills/math-paper-writer/scripts/check_lean_environment.py --library optlib --allow-sorry --require-toolchain-installed
```

7. If the proof assistant is installed, run the actual build command and record
   it. Do not simulate a successful build.
8. Assign a verification level:
   `INFORMAL_AUDIT`, `FORMALIZATION_READY`, `PARTIALLY_FORMALIZED`,
   `FORMALLY_CHECKED`, `STATEMENT_MISMATCH`, or `NOT_READY`.
9. Recommend safe manuscript wording.

## Output

Use `assets/formal_verification_report_template.md` and include:

1. Theorem contract
2. Formal artifact
3. Statement alignment
4. Trust-boundary findings
5. Build/check results
6. Verification level
7. Safe wording
8. Open proof obligations
