# Mathematical Writing Principles

Use this reference for general mathematical writing quality across pure,
applied, computational, and interdisciplinary mathematics.

## Core principle

Mathematical writing is guided reasoning. A manuscript must help the reader
understand what is true, why it is true, how it is connected to prior work, and
where its limits are.

## Prose and symbols

- Treat equations, symbols, algorithms, tables, and citations as parts of
  sentences.
- Introduce displayed equations with prose and punctuate them when they
  complete a sentence.
- Avoid sentence fragments beginning with `Since`, `If`, or `When`.
- Avoid starting sentences with bare lower-case variables, displayed symbols,
  or naked citations.
- Prefer words over dense symbolic logic when the words preserve precision and
  reduce reader burden.

## Symbol grammar

- Use `=` only between objects of the same type.
- Use implication and equivalence arrows only between statements.
- Use equivalence only when both directions are justified.
- Do not chain non-transitive relations such as `a \ne b \ne c`.
- Check quantifier order before editing style.
- Distinguish objects from their values, sets from elements, functions from
  function values, and equations from expressions.

## Theorem and result contracts

Every theorem, lemma, proposition, algorithmic guarantee, example, or numerical
claim needs a contract:

- objects and setting;
- assumptions and domains;
- conclusion;
- dependency of constants and rates;
- proof or evidence route;
- scope and limitations;
- relation to prior work when relevant.

Do not make the statement stronger than the proof, computation, citation, or
experiment supports.

## Reader path

A reader should understand not only each local derivation but also why the
derivation appears where it does.

- Introduce assumptions and notation when they become useful.
- Explain why a result is needed before or after stating it.
- Organize related work by ideas, assumptions, methods, or guarantees.
- Use proof roadmaps for long or technically layered arguments.
- Revise earlier motivation after proofs or experiments reveal narrower claims.

## Citation and prior work

- Citations should carry narrative function, not merely occupy parentheses.
- Name authors when the cited work is the subject of the sentence.
- Verify claims of the form "X proves Y" against the source.
- Prefer primary sources for exact theorems, rates, definitions, and algorithms.
- Use surveys for orientation but not as the only support for sharp claims when
  primary sources are available.

## Revision

Revise by selection before compression.

- Decide the paragraph's role before polishing sentences.
- Remove, reorder, or postpone distracting material.
- Separate proof audit from proof rewriting.
- Re-run claim, citation, and experiment checks after major restructuring.

## Numerical and computational evidence

Computational mathematics requires enough detail for interpretation and, when
possible, repetition.

- State problem classes, metrics, baselines, budgets, stopping rules, precision,
  software versions, and randomness policy when relevant.
- Use tables for exact small comparisons and figures for trends or large data.
- Separate observed facts from interpretation.
- Do not extrapolate beyond tested dimensions, budgets, noise models, or
  problem families without explicit caution.

## Final proofreading

Proofreading is not only spelling. Check theorem labels, equation references,
numbers, bibliography metadata, punctuation around equations, notation
consistency, and source context. Read important passages aloud when possible.
