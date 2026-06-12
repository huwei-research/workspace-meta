# Mathematical Language: Sentences, Equations, Symbols, and Paragraphs

## Mathematics is written mostly in words

Equations and symbols are indispensable, but they should supplement prose rather than replace it. A mathematical manuscript should usually contain more words than formulas. Even a displayed equation is part of a sentence and should be readable aloud.

## Complete sentences

Every mathematical assertion must be a complete sentence when read aloud. Avoid fragments such as:

- `Since x is positive.`
- `If the model is fully linear.`
- `When the trust-region radius is small.`
- `Therefore boundedness.`

Repair fragments by adding the missing clause or verb:

- `Since x is positive, the logarithm is well defined.`
- `If the model is fully linear, then the Cauchy decrease estimate holds.`
- `When the trust-region radius is small, the error term is dominated by the linear term.`
- `Therefore the sequence is bounded.`

## Equations as sentence parts

A displayed equation should have a grammatical role. Introduce it and punctuate it.

Good pattern:

```tex
The model error is bounded by
\[
  |f(y)-m_k(y)| \le \kappa_f \Delta_k^2,
  \qquad y \in B(x_k,\Delta_k).
\]
This estimate is used only on successful iterations.
```

Do not leave equations floating without telling the reader whether they are assumptions, consequences, definitions, equivalent reformulations, or intermediate computations.

## Avoid isolated equation chains

A chain of equations is not a proof unless the logical relation between lines is clear. A sequence may represent equivalence, implication, a necessary condition, a sufficient condition, or a computation under an assumption. These are different.

When auditing an equation block, ask:

- What is assumed at the first line?
- Is each arrow an implication or equivalence?
- Does any step lose information, add solutions, or require a side condition?
- Are domains preserved?
- Are nonnegative quantities required before taking square roots, dividing, or applying monotonicity?
- Are final candidates checked in the original statement if only necessary conditions were used?

Use explicit prose:

```tex
Thus any solution must satisfy ... . Conversely, if ... holds, then substituting into the original equation gives ... .
```

## Starting sentences

Avoid starting a sentence with a bare symbol, lower-case variable, or citation command.

Prefer:

- `The function f is convex if ...`
- `The matrix A is nonsingular.`
- `The work of Smith [12] treats the deterministic case.`
- `Smith and Jones [12] prove ...`

Avoid:

- `f is convex if ...`
- `A is nonsingular.`
- `[12] proves ...`

This rule prevents ambiguity and improves the sentence's rhythm.

## Punctuation around symbols

Use punctuation or words to separate adjacent mathematical clauses.

Bad:

```tex
If x=1 f(x)=0.
```

Better:

```tex
If x=1, then f(x)=0.
```

When using `let`, `suppose`, or `assume`, do not splice the setup and the conclusion with a comma.

Bad:

```tex
Let x be positive, then x^2>0.
```

Better:

```tex
Let x be positive. Then x^2>0.
```

## Use words when words are clearer

A compact symbolic statement may be correct but hard to read. Replace dense symbolic logic by prose when the symbols do not aid precision.

Dense:

```tex
\forall \epsilon>0\;\exists\delta>0\;\text{s.t.}\; |x-a|<\delta \Rightarrow |f(x)-f(a)|<\epsilon.
```

Clearer:

```tex
For every \(\epsilon>0\), there exists \(\delta>0\) such that
\(|f(x)-f(a)|<\epsilon\) whenever \(|x-a|<\delta\).
```

## Big equations

Do not put a visually large or structurally complex equation inline. Use displayed equations for fractions, long sums, multi-line derivations, cases, and nested expressions. If the inline version is short and clearer, use a simplified inline form.

## Paragraphs

A paragraph should have one purpose. In mathematical writing, common paragraph purposes are:

- define an object;
- motivate an assumption;
- state a result;
- explain a proof idea;
- execute one proof step;
- compare with prior work;
- interpret a numerical result;
- state a limitation.

Do not mix proof steps, citation history, and experimental claims in one paragraph unless the connection is explicit.
