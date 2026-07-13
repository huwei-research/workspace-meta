# Claim-Evidence Integrity

Use this reference when auditing abstract, introduction, related work, conclusions, rebuttals, experiment sections, or any manuscript passage that makes claims beyond local algebra.

## Claim types

- `mathematical`: theorem, lemma, corollary, proof step, convergence claim, complexity claim, assumption implication.
- `algorithmic`: solver behavior, implementation detail, stopping rule, computational cost, oracle model.
- `experimental`: observed performance, robustness, sensitivity, ablation, statistical comparison.
- `bibliographic`: what another paper proved, assumed, tested, or failed to address.
- `novelty`: first, new, sharper, weaker assumptions, broader class, improved rate, simpler proof.
- `scope`: limitation, applicability, failure mode, open problem.
- `reproducibility`: data, code, seeds, versions, budgets, and figure-generation path.

## Verdicts

- `SUPPORTED`: evidence is present and the wording matches it.
- `NEEDS_PROOF`: a mathematical claim lacks a complete proof or cites an insufficient result.
- `NEEDS_CITATION`: a factual or prior-work claim needs a source.
- `NEEDS_EXPERIMENT`: an empirical claim needs data, controls, or a reproducibility record.
- `OVERCLAIMED`: evidence exists but the wording is too broad or too strong.
- `DISTORTED_SOURCE`: the cited source is represented inaccurately.
- `UNVERIFIABLE`: the claim cannot be checked from available manuscript, source, data, or code.
- `OUT_OF_SCOPE`: the claim may be true but does not belong in the current paper.

## Audit procedure

1. Extract central claims from title, abstract, introduction, contributions, theorem statements, experiment discussion, and conclusion.
2. Classify each claim by type.
3. Locate the evidence route: theorem/proof, equation, computation, experiment table, figure, code path, citation/source card, software/data artifact, appendix, or limitation note.
4. Check exactness. Compare wording against evidence for quantifiers, domains, constants, rates, probability, and assumptions.
5. Check source context. For cited work, verify what the source actually establishes and whether the manuscript overextends it.
6. Check empirical support. Verify problem sets, seeds, budgets, baselines, stopping rules, statistical summaries, and plotting scripts.
7. Assign verdict and severity.
8. Produce required fixes before rewriting for style.

## Evidence routes must not substitute for each other

- A citation cannot replace a missing proof of this paper's theorem.
- A theorem cannot replace missing experiment details for an empirical
  comparison.
- An experiment cannot prove an asymptotic or universal mathematical claim.
- A survey can orient related work but should not be the only evidence for a
  sharp theorem when the primary source is available.
- A source card verifies what another paper says; it does not verify that the
  present manuscript's new proof or implementation is correct.

For risky cited claims, use `references/citation_literature_protocol.md` and
`assets/math_source_card_template.md`.

## Severity

- `blocking`: central claim is false, unproved, source-distorting, or contradicted by results.
- `major`: important claim is unsupported, overbroad, or missing a key condition.
- `minor`: wording is imprecise but unlikely to mislead after a local fix.
- `optional`: improvement to clarity, traceability, or redundancy.

## Publication gate

Before final submission:

- No central mathematical claim may remain `NEEDS_PROOF`, `OVERCLAIMED`, `DISTORTED_SOURCE`, or `UNVERIFIABLE`.
- No central empirical claim may remain `NEEDS_EXPERIMENT`, `OVERCLAIMED`, or `UNVERIFIABLE`.
- No novelty or comparison claim may remain `NEEDS_CITATION`, `DISTORTED_SOURCE`, or `UNVERIFIABLE`.
- Limitation language must match the actual assumptions, test classes, dimensions, budgets, and noise models.

## Safe rewrite rules

- Prefer "under Assumptions A-B" over a broad unqualified claim.
- Prefer "on the tested problem set" over "in practice" when experiments are limited.
- Prefer "to our knowledge" only after a reasonable literature check; otherwise use `[verification needed]`.
- Prefer "extends X from setting A to setting B" only when the cited source and theorem statement both confirm the mapping.
- Preserve uncertainty markers until verification is complete.
