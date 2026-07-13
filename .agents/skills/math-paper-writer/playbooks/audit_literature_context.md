# Playbook: Audit Literature and Citation Context

Use this playbook for related work, novelty claims, source-context checks, and
reference accuracy.

## Procedure

1. Extract cited claims from the manuscript passage.
2. Classify each claim as mathematical, historical, methodological,
   comparative, empirical, software/data, or novelty.
3. For important or risky sources, create a source card.
4. Retrieve or inspect the source text when available. Do not simulate access.
5. Compare manuscript wording against the source:
   - assumptions;
   - conclusion;
   - object and setting;
   - rate, constant, dimension, or probability mode;
   - experiment setting;
   - stated limitation.
6. Assign a verdict:
   `SUPPORTED`, `MINOR_DISTORTION`, `MAJOR_DISTORTION`, `UNVERIFIABLE`, or
   `WRONG_EVIDENCE_ROUTE`.
7. Rewrite only after the diagnosis is clear.
8. Transfer central issues into the claim-evidence ledger.

## Output

Use this structure:

1. Citation inventory.
2. Source cards used.
3. Claim-reference alignment table.
4. Distortions or unsupported novelty claims.
5. Safe rewrite recommendations.
6. Remaining sources to read.

## Safe wording patterns

- `Smith and Jones prove ... under ... .`
- `This differs from ... in that ... .`
- `The present result removes ... but retains ... .`
- `The experiments in Section ... compare ... on ... .`
- `A complete comparison with ... remains open.`
