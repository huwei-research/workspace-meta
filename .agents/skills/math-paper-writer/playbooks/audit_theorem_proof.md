# Playbook: Theorem and Proof Audit

1. Copy or summarize the theorem statement.
2. Build the theorem contract: objects, assumptions, conclusion, quantifiers, constants, mode of convergence or probability.
3. List dependencies: definitions, lemmas, assumptions, previous equations.
4. For each proof block, identify the transition type.
5. Check all equalities.
6. Check all inequalities, especially signs, monotonicity, convexity/concavity, norm changes, and constants.
7. Check all implications and equivalences.
8. Check quantifier order and domains.
9. Check if any symbol is used before definition.
10. Check if the conclusion exactly matches the theorem statement.
11. Report risks before rewriting.
12. Only after audit, provide a safe revised proof if requested.

Output uses `assets/proof_audit_report_template.md`.
