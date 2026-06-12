# Paper Architecture

## Title

A title should be short enough to be remembered and precise enough to be useful. It should identify the mathematical object, problem, method, phenomenon, or contribution. Avoid vague titles that only state a broad topic. Avoid abbreviations that only specialists in a narrow subcommunity will recognize.

A strong mathematical title often has one of these forms:

- `A [method/property] for [problem/class]`
- `[Phenomenon] in [mathematical setting]`
- `[Main result] for [object] under [condition]`
- `[Sharp/Stable/Randomized/Structure-preserving] [method/result] for [problem]`

Title audit questions:

- Does the title identify the content rather than merely the area?
- Is it terse without being cryptic?
- Does it avoid overclaiming?
- Would a reader searching the field recognize the paper's object?
- Would a non-author remember it after one reading?

## Abstract

The abstract should not be a table of contents. It should be a compact argument:

1. State the problem or setting.
2. State the obstacle or gap.
3. State the main contribution.
4. State the mathematical form of the result.
5. Mention evidence: theorem, algorithm, complexity bound, experiment, or example.
6. State scope or limitations when necessary.

Avoid claims such as `efficient`, `robust`, `novel`, or `significant` unless the paper states the comparison and evidence. Prefer measurable claims: iteration bound, approximation order, stability property, complexity class, error level, probability guarantee, or reproducibility evidence.

## Introduction

The introduction invites the reader into the problem. It should not begin with unnecessary formalism unless the target journal expects it. A good introduction answers:

- What problem is being studied?
- Why does it matter mathematically or computationally?
- What has been done before?
- What remains insufficient, unavailable, unstable, too expensive, too restrictive, or unexplained?
- What is the paper's approach?
- What are the precise contributions?
- How should the reader navigate the paper?

### Prior work as narrative, not a dump

Each cited work should perform a function:

- establish the problem's importance;
- define the current state of the art;
- motivate an assumption, method, or comparison;
- identify a limitation that the present paper addresses;
- connect the paper to another area;
- justify a baseline, model, or theorem form.

Avoid a paragraph that merely lists references with no relationship to the story. Name authors when doing so improves readability, especially when the citation is the subject of the sentence.

### Contribution claims

Every contribution should be attached to evidence. Use a contribution ledger:

| Contribution | Evidence | Assumptions | Compared with | Limitation |
|---|---|---|---|---|
| | theorem/algorithm/experiment | | | |

Bad contribution claims are vague or untraceable:

- `We propose an efficient method.`
- `We significantly improve previous work.`
- `Our approach is robust.`

Safer claims:

- `Under Assumptions A--C, Theorem 2 proves an iteration bound of ... .`
- `The method removes the bounded-domain assumption used in ... .`
- `On the test set described in Section 5, the method requires fewer function evaluations than ... .`

## Related work

Related work should be structured by ideas, not citation chronology. Good organizing axes include:

- problem variants;
- assumptions;
- proof techniques;
- algorithmic families;
- complexity guarantees;
- deterministic vs stochastic settings;
- exact vs approximate models;
- smooth vs nonsmooth settings;
- convex vs nonconvex settings.

Do not move all references into a disconnected related-work section if they are needed to motivate the main story. Use related work to compare and situate; use the introduction to motivate.

## Section order

A paper should introduce material before it is needed, but not much earlier. If a definition appears too early, the reader forgets it. If it appears too late, the reader is confused. Put results where they reduce future resistance.

Typical order:

1. Introduction and contributions.
2. Notation and assumptions, only those needed soon.
3. Algorithm or main construction.
4. Main result statement.
5. Key lemmas and proof mechanism.
6. Full proof.
7. Experiments, examples, or applications.
8. Conclusion and limitations.

For theoretical papers, it is often helpful to give a short proof roadmap before technical lemmas.

## Conclusion

The conclusion should not merely repeat the abstract. It should answer:

- What has the reader learned that was not known before?
- Which assumptions are essential, technical, or removable?
- Which limitations remain?
- Which follow-up questions are mathematically natural?

Avoid unsupported future-work claims.
