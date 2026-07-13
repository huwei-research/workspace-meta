# Playbook: Claim-Evidence Audit

1. Identify manuscript scope: section, full paper, rebuttal, abstract, or related work.
2. Read `references/claim_evidence_integrity.md`.
3. Extract claims from title, abstract, introduction, contribution list, theorem statements, experiment discussion, and conclusion.
4. Classify each claim as mathematical, algorithmic, experimental, bibliographic, novelty, scope, or reproducibility.
5. Map each claim to exact evidence: theorem label, proof block, equation, table, figure, code path, data file, appendix, or citation key.
6. Check whether wording matches evidence, especially assumptions, domains, constants, rates, probability, dimensions, budgets, and tested problem classes.
7. For cited work, verify the source context before accepting the manuscript's summary.
8. Assign verdict and severity using `references/claim_evidence_integrity.md`.
9. Fill `assets/claim_evidence_ledger_template.md` or update the project's existing ledger.
10. Report blocking and major issues before offering polished prose.

Output order:

1. Audit scope
2. Claim-evidence ledger or summary
3. Blocking issues
4. Major issues
5. Minor issues
6. Safe wording repairs
7. Verification gaps
