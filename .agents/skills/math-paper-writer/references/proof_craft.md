# Theorem and Proof Craft

## Theorem statement contract

A theorem statement must be precise, not impressive. It should be as simple as possible without hiding necessary assumptions.

Check every theorem for:

- objects and spaces;
- deterministic or stochastic setting;
- regularity assumptions;
- constants and whether they depend on dimension, iteration, sample size, tolerance, or probability level;
- quantifier order;
- conclusion type;
- probability mode if any: deterministic, in expectation, high probability, almost sure;
- whether the statement is local, global, asymptotic, finite-time, qualitative, or quantitative;
- whether every assumption is used and every used condition is stated.

Avoid overstatement. If the proof only gives convergence of a subsequence, do not state convergence of the full sequence. If the result is in expectation, do not write a high-probability claim. If constants depend on dimension, do not call the bound dimension-free.

## Result cards

Before editing a theorem, create a result card:

- Name of result.
- Mathematical setting.
- Assumptions.
- Conclusion.
- Proof mechanism.
- Dependencies.
- Limitations.
- Later use.

If the card cannot be completed, the statement or surrounding exposition is probably under-specified.

## Proof roadmap

For a long proof, give the reader a roadmap before technical details. A proof roadmap should say:

- what the proof reduces to;
- which lemma gives the key estimate;
- where the main assumption enters;
- how the final conclusion follows.

The roadmap should not repeat every algebraic detail.

## Line-by-line proof audit

For each line or displayed block, classify the transition:

- definition;
- assumption;
- previous lemma;
- algebraic equality;
- inequality by monotonicity, convexity, smoothness, Lipschitz continuity, Cauchy-Schwarz, Jensen, triangle inequality, or another named result;
- implication;
- equivalence;
- necessary condition only;
- sufficient condition only;
- probabilistic conditioning;
- limit passage;
- case split;
- contradiction step.

If a transition cannot be classified, flag it.

## Equality checks

When using `=`, the two sides must be the same object. Do not use equality between:

- a function and a function value;
- a statement and an expression;
- a matrix and a row-equivalent matrix;
- an equation and a variable;
- a set and an element;
- a null space and its dimension;
- a process and its result.

For equality chains, check order. Put the expression whose equality is justified at each step adjacent to the reason. If a term is transformed by a theorem, show the relevant expression before and after the transformation.

## Inequality checks

Inequality direction errors are critical. Before accepting an inequality, check:

- Was a negative quantity multiplied or divided?
- Was a monotone function applied on the correct domain?
- Was a convexity or concavity inequality used in the correct direction?
- Was a norm inequality applied to the correct norm?
- Were absolute values or squares introduced safely?
- Was an expectation, supremum, infimum, maximum, or minimum moved through an inequality legally?
- Does the constant increase or decrease in the intended direction?
- Are all quantities finite and well defined?

If the sign of a multiplier is unknown, the step is invalid until the sign is established.

## Implication and equivalence

Use implication arrows only between statements. Do not mix `if` and `\Rightarrow` redundantly in the same phrase. Do not write an implication symbol in the middle of nowhere.

Use equivalence only when both directions are valid. Many proof steps are one-way because they square both sides, relax a condition, take absolute values, replace a quantity by an upper bound, or discard constraints. Mark these as implications, not equivalences.

When solving equations, distinguish:

- candidates obtained from necessary conditions;
- solutions verified in the original equation;
- sufficient conditions that guarantee a solution.

## Non-transitive relations

Do not chain non-transitive relations. In particular, `a \ne b \ne c` does not imply that all three quantities are pairwise distinct. Write `a`, `b`, and `c` are pairwise distinct, or state all three inequalities.

## Quantifiers

Quantifier order is part of the theorem. Check whether the statement means:

- for every object there exists a parameter;
- there exists one parameter that works for every object;
- for every tolerance there exists an iteration;
- there exists an iteration after which every later point satisfies a property.

Do not swap `for all` and `there exists`. Do not write `for \forall`. Do not use `\forall x such that ...` when the intended meaning is restricted universal quantification over a subset; write the set first.

## Statements vs expressions

Only statements can be true, false, assumed, proved, contradicted, or equivalent. Expressions can be equal, bounded, differentiated, minimized, or substituted.

Bad patterns:

- `S(k+1)=...` when `S(k+1)` is a statement.
- `n=k+1 is true.`
- `The equation is equivalent to x=3` when an implication has only produced candidates.

## Induction proofs

Audit induction proofs with special care:

1. Define the statement `P(n)` without already quantifying over all `n`.
2. Prove the base case without writing meaningless ellipses.
3. Assume `P(k)` for a fixed but arbitrary admissible `k`, not for all `k`.
4. Use the induction hypothesis only at the allowed index.
5. Prove `P(k+1)` as a statement, not an equality involving `P(k+1)`.
6. Conclude with the correct range and the correct principle.

## Contradiction and contrapositive

When using contradiction, explicitly state the negation of the theorem's conclusion under the theorem's assumptions. When using contrapositive, verify that the statement has the form `P implies Q` and that the proof establishes `not Q implies not P`.

## Limit passages

Before passing to a limit, check:

- existence of the limit;
- subsequence vs full sequence;
- continuity or lower semicontinuity assumptions;
- interchange of limit and expectation, infimum, supremum, derivative, integral, or probability;
- uniformity of constants;
- topology and mode of convergence.

## Probabilistic proofs

Identify the probability space, random variables, filtration if any, conditioning, event definitions, and failure probabilities. Keep separate:

- almost-sure statements;
- high-probability statements;
- in-expectation statements;
- statements conditional on a good event.

Do not silently turn a conditional good-event result into an unconditional theorem.

## Proof polishing after audit

After correctness is established:

- combine trivial steps only when no logical relation is lost;
- introduce lemmas for repeated estimates;
- avoid unnecessary symbolic synonyms;
- replace dense case expressions by a conceptual definition when possible;
- keep the subject and verb near each other;
- remove redundant adverbs and inflated adjectives.
