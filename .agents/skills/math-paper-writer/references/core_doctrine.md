# Core Doctrine: Mathematical Writing as Guided Reasoning

Mathematical writing must satisfy four simultaneous tests.

1. **Credibility test.** The prose should create an impression of rigor, discipline-specific competence, and care. Sloppy language, inconsistent notation, and careless bibliography entries make the mathematics less trustworthy even when the theorem is true.
2. **Reader-path test.** The reader should be able to follow not only each local derivation but also why that derivation appears where it does.
3. **Logical-contract test.** Every theorem, proof, example, algorithm, and experiment should state what is assumed, what is proved or observed, and what is not claimed.
4. **Mechanical-integrity test.** Sentences, symbols, punctuation, references, LaTeX, figures, tables, and bibliography entries must be checked as carefully as theorems.

## The central principle

Communicate ideas, not just results. A mathematically correct manuscript can still fail if the reader cannot see the problem, motivation, route, dependencies, or payoff. A good paper gives the reader both a path and a reason to walk it.

Before drafting, identify:

- what the paper has to say;
- whom it says it to;
- what the reader already knows;
- what the reader needs next;
- which results deserve emphasis;
- which details should be omitted, postponed, or moved to an appendix.

## The reader is not a proof checker only

A reader wants to know where ideas come from. If every displayed line is correct but the purpose of the derivation is unclear, the writing has failed. Put results where they are needed. Explain why an assumption or symbol is introduced. Do not introduce a prime number, a compact set, a Lipschitz constant, or a probability event unless the reader will later see why that property mattered.

## The paper is a journey

Good mathematical papers usually follow this pattern:

1. A problem arises naturally.
2. Existing work explains part of the landscape.
3. A gap or limitation remains.
4. The paper introduces a precise approach.
5. The main results close the gap under stated assumptions.
6. Proofs show the mechanism, not just the conclusion.
7. Experiments, examples, or discussion clarify scope and limitations.
8. The conclusion tells the reader what has been gained and what remains open.

## Revision is spiral-shaped

Do not expect Section 1 to be final before Section 2 exists. Later results reveal weaknesses in earlier motivation; proof details reveal missing assumptions in theorem statements; experiments reveal overclaiming in the abstract. Revise in a spiral:

```text
1 -> 2 -> 1 -> 2 -> 3 -> 1 -> 2 -> 3 -> 4 -> ...
```

At each pass, simplify and streamline by selection. Do not compress a bad structure into shorter sentences; remove, reorder, or rewrite the structure.

## Style follows truth

Never convert a weak theorem into a strong-looking sentence. Never hide uncertainty with elegant prose. Never replace a precise quantitative claim by an impressive adjective. Prefer a modest correct statement over a broad unsupported one.

## The skill's default editing order

1. Mathematical contract.
2. Story and reader path.
3. Section structure.
4. Theorem and proof correctness.
5. Notation and terminology.
6. Sentence, equation, and paragraph form.
7. Citations, experiments, figures, tables.
8. LaTeX, bibliography, and final proofreading.

Do not invert this order unless the user explicitly requests a local copy edit.
