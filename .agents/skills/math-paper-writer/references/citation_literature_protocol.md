# Citation and Literature Protocol

Use this reference when auditing related work, novelty claims, comparison
claims, bibliographic metadata, or the accuracy of claims about prior papers.

## Literature roles

Do not treat all citations as interchangeable. Classify each source by role:

- `foundation`: establishes a theorem, definition, method, or classical result.
- `comparison`: supplies a baseline, rate, assumption set, or experimental
  reference point.
- `motivation`: explains why the problem or model matters.
- `method-lineage`: introduces a technique, proof device, or algorithmic family.
- `limitation`: documents a gap, assumption, failure mode, or open problem.
- `software-data`: documents code, datasets, packages, problem sets, or
  implementation details.
- `survey-context`: summarizes a field but should not be used as the only
  source for a sharp theorem when a primary source is available.

## Source card

For important sources, create a card before writing strong claims:

- citation key and full bibliographic metadata;
- source locator: DOI, arXiv ID, URL, book chapter, theorem number, section, or
  page;
- manuscript claim using the source;
- source passage or result checked;
- assumption/result match;
- what the source supports;
- what the source does not support;
- version/date checked;
- verification status.

## Claim-reference alignment

For each cited claim, ask:

1. Is the citation anchor attached to the right sentence?
2. Does the sentence say what the source actually says?
3. Are assumptions, domains, rates, dimensions, probability modes, and
   limitations preserved?
4. Does the manuscript infer a stronger novelty or comparison claim than the
   source supports?
5. Is the claim empirical, mathematical, software, or historical? Use the
   correct evidence route.

Verdicts:

- `SUPPORTED`: source supports the sentence as written.
- `MINOR_DISTORTION`: local wording is too broad or missing a small condition.
- `MAJOR_DISTORTION`: source is represented incorrectly in a way that affects
  the argument.
- `UNVERIFIABLE`: source could not be checked from available material.
- `WRONG_EVIDENCE_ROUTE`: citation is being used for a claim that needs proof,
  experiment, code, or data evidence instead.

## Search and discovery record

For literature discovery, record enough detail to avoid drift:

- research question or subquestion;
- databases or tools searched;
- exact queries when feasible;
- date of search;
- inclusion and exclusion criteria;
- high-priority sources and why they matter;
- unresolved papers that still need reading.

High citation counts can prioritize reading, but they do not prove relevance or
truth. Prefer primary sources for theorem statements, algorithm definitions,
and exact assumptions.

## Writing rules

- Integrate citations into the story. Avoid isolated reference dumps.
- Name authors when the source is the grammatical subject or when it clarifies
  who did what.
- Use surveys for orientation, then cite primary sources for exact results.
- Do not write `to our knowledge`, `first`, `state of the art`, or `strictly
  improves` until the search record and source cards support it.
- Mark uncertain literature claims as `[verification needed]`.
- Proofread bibliography metadata; imported BibTeX can contain wrong titles,
  author initials, venues, pages, or capitalization.

## Math-specific source matching

A cited theorem is aligned only if the manuscript preserves:

- the same mathematical object or a correctly stated specialization;
- the same or stronger assumptions when applying the result;
- the same conclusion type;
- the same probability mode if stochastic;
- the same asymptotic or finite-time status;
- the same constants or a justified change of constants;
- the same domain, topology, norm, and regularity conditions.

If any item differs, state the difference explicitly or weaken the claim.
