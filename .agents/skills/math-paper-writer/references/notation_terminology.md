# Notation and Terminology

## Notation as memory support

Good notation helps the reader remember the object. Bad notation forces the reader to decode the paper repeatedly. Choose notation that is standard in the field, mnemonic when possible, and visually distinguishable.

Useful conventions:

- small tolerances: `\epsilon`, `\delta`;
- integer counts: `n`, `m`, `k`;
- constants: `c`, `C`, `\kappa`, `L` depending on field convention;
- matrices: uppercase roman or bold letters;
- vectors: lowercase bold or plain lowercase, but choose one convention;
- sets: uppercase calligraphic or roman letters;
- collections of sets: visually distinct calligraphic or fraktur letters.

## Notation ledger

For any long manuscript, maintain a notation ledger:

| Symbol | Meaning | Type | Domain | First defined | Used where | Possible conflict |
|---|---|---|---|---|---|---|
| | | scalar/vector/set/function/event | | | | |

When auditing, check that every important symbol is defined before use and that every defined symbol is used.

## Avoid excessive decoration

Do not use many variants of one symbol unless the distinctions are central and repeatedly used. A page containing `x`, `x'`, `x''`, `\bar{x}`, `\tilde{x}`, `\hat{x}`, and indexed versions of each is a warning sign.

Prefer conceptual names or subscripts:

- `x_k` for an iterate;
- `x_k^+` for a trial point if standard in the paper;
- `x_k^{\rm acc}` only if the accepted point must be distinguished;
- `s_k` for a step;
- `m_k` for a model;
- `\Delta_k` for a trust-region radius.

## Avoid confusing symbols

Check whether the reader can distinguish:

- a sequence index from a vector coordinate;
- a vector from a scalar;
- a set from an element;
- a function from its value;
- a matrix from its entries;
- a random variable from its realization;
- a deterministic constant from an iteration-dependent quantity.

If `x_i` can mean either the `i`th coordinate of `x` or the `i`th iterate in a sequence, choose a different convention and state it early.

## Function vs function value

A function and its value are different objects. Do not assign properties of the function to its value.

- `f` is continuous, convex, differentiable, Lipschitz, or measurable.
- `f(x)` is a scalar, vector, matrix, probability, or value at `x`.

Avoid `Suppose that f(x) is convex`. Write `Suppose that f is convex` or define the unnamed function using mapping notation.

## Standard mathematical terms

Use a word for the right object.

### Algebra

- A constant polynomial is a polynomial; a constant is a fixed value.
- If `a` divides `b`, then `b` is divisible by `a`.
- The result of multiplication is a product.
- A graph is translated by a vector; it is not merely moved when formal terminology is required.
- Use `prime`, not redundant phrases such as `prime number` after the noun is already clear.

### Geometry

- A circumcenter is the center of the circumscribed circle.
- Points are concyclic; polygons are cyclic.
- A perimeter is a length; a circumference may mean the boundary or its length depending on convention.

### Induction

- Use `principle of mathematical induction`, not `principal`.
- A statement can be true; a variable assignment is not true by itself.
- Define `P(n)` as a statement depending on `n`, then prove it for all admissible `n`.

### Functions and calculus

- A number is in the domain of a function; it is not the domain.
- A derivative is the result; differentiation is the process.
- Use `set` when imposing an equation for solving; use `suppose` for an assumption.
- A function is increasing on an interval.
- An expression may be undefined; an equation may have no solution.

### Linear algebra

- State matrix entries by row and column, such as `(i,j)`-entry.
- Write matrix products as `AB` unless the `\times` sign is needed for clarity.
- A matrix may be positive definite, entrywise positive, nonnegative, stochastic, or invertible; do not write `positive` without specifying the sense.
- Vectors, not matrices, are linearly independent unless referring to rows or columns.
- A basis is a set or ordered list of vectors, according to context; do not write two vectors separated by a comma without braces if a set is meant.
- A null space has dimension; it is not equal to a number.
- Rank is already a number; do not write `number of rank`.

## Symbol audit

### Equality and row operations

Use equality only for equal objects. Use arrows or stated row operations for row-equivalent matrices.

### Membership and subset

Use `\in` for element membership and `\subseteq` for set inclusion. Intervals are subsets of `\mathbb{R}`, not elements of `\mathbb{R}`.

### Quantifiers

`\forall` means for all. `\exists` means there exists. There is no universal symbol that means `for some`. Use prose when it is clearer.

### Arrows

`\Rightarrow` and `\Leftrightarrow` connect statements, not phrases. If prose already says `hence`, do not append an implication statement as if the previous prose were the antecedent.

## Visual distinguishability

Watch for characters that are easily confused in handwritten notes, scans, or dense LaTeX:

- `t` and `+`;
- `1`, `l`, and `I`;
- `x` and `\times`;
- `p` and `\rho`;
- `a`, `\alpha`, and `2`;
- `0`, `6`, and `\sigma`.

In final manuscripts, choose fonts and notation that reduce such ambiguity.
