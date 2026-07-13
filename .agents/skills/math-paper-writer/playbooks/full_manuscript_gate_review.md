# Playbook: Full Manuscript Gate Review

Use this playbook before submission, before a major rewrite, or when the user
asks whether a mathematical manuscript is ready.

## Procedure

1. Read the project-local `AGENTS.md` and compile instructions if present.
2. Identify the manuscript entry file, bibliography, figures, tables,
   appendices, experiment artifacts, and any ledgers.
3. Reconstruct the paper thesis and main claims.
4. Build or update a claim-evidence snapshot.
5. Review with the rubric:
   - mathematical correctness;
   - theorem/result contract;
   - proof traceability;
   - claim-evidence integrity;
   - literature and citation accuracy;
   - notation and symbol grammar;
   - narrative architecture;
   - experiments and reproducibility;
   - mathematical English and readability;
   - production readiness.
6. Run deterministic checks when files are available.
7. Assign severity and dimension scores.
8. Produce a gate verdict:
   `READY`, `READY_AFTER_LOCAL_FIXES`, `NOT_READY`, or
   `INSUFFICIENT_MATERIAL`.

## Output

Lead with findings:

| Severity | Location | Issue | Why it matters | Safe fix |
|---|---|---|---|---|
| P0/P1/P2/P3 | | | | |

Then include:

1. Dimension score table.
2. Gate verdict.
3. Required fixes before submission.
4. Optional polish.
5. Checks run and checks not run.

## Rules

- Do not let strong prose hide uncertain mathematics.
- Do not mark the manuscript ready if central claims remain unverified.
- Do not average away a blocking issue.
- If source files or experiment artifacts are unavailable, state the limitation
  in the verdict.
