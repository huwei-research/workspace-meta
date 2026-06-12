# English Style for Mathematical Prose

## First principles

Good mathematical English helps the reader follow the argument. The goal is not ornament but precision, early meaning, and low friction.

Prefer sentences that begin with a clear subject and verb. Keep the subject close to its verb. Put heavy qualifications later unless they are needed immediately.

## Articles

Use articles deliberately.

- Use `the` for a specific known object, theorem, algorithm, or previously introduced item.
- Use `a` or `an` for one unspecified object.
- Use zero article with a symbol name: `By Lemma 2, g is continuous`.
- Use a noun when using `the`: `the function g`, not `the g`.
- Use `an` before letter names that begin with a vowel sound, such as `an m-by-n matrix`.

## Singular and plural

Check agreement:

- `Every square is a rectangle.`
- `All squares are rectangles.`
- `There exists a point.`
- `There exist points.`
- `A matrix`, plural `matrices`.
- `A vertex`, plural `vertices`.
- `A maximum`, plural `maxima`.

## Verb forms and word forms

Use the correct grammatical form:

- `The sequence does not converge` or `The sequence is not convergent`.
- `The result follows`, not `The result is followed`.
- `This proves the claim`; `This completes the proof`.
- `The surface area increases by ...`; `the increase is ...`.
- `The maximum value`, not `the maximal value`, unless using `maximal` in its order-theoretic sense.
- `One plus one equals two` or `is equal to two`, not `equals to two`.

## Word order

Use conventional mathematical word order:

- `Let x be a positive real number.`
- `Let y be the width of the rectangle.`
- `The maximum degree of the remainder is 1.`
- `The smallest possible value is 0.`
- `We will show that ... for every ...` when this reads more naturally.
- Keep `strictly` next to `increasing` or `decreasing`.

## Choice of words

- Use `i.e.` for `that is` and `e.g.` for examples.
- Use `in other words` for explanation, not for examples.
- Use `respectively` only when the pairing is unambiguous.
- Use `finitely many` or `a finite number of`, not `finite solutions`.
- Use `infinitely many`, not `infinite solutions`.
- Use `deduce` for logical inference and `deduct` for subtraction.
- Use `cannot` unless the meaning is explicitly `can choose not to`.
- Use `without loss of generality`, not similar-sounding variants.

## All, any, each, every

`Any` can be ambiguous between universal and existential meanings. Prefer `each` or `every` for universal statements when clarity matters.

- Use `Each continuous function has a maximum` when each function may have its own maximum.
- Use `Any one example suffices` only when existential or arbitrary choice is intended.

## If, then, since, when

If a sentence begins with `if`, include a clear conclusion. For long hypotheses, use `then` to mark the conclusion.

- `If x>0, then x^2>0.`

Do not turn dependent clauses into sentences:

- `Since x is nonnegative, x+1>0.`
- `When x=0, we obtain f(0)=0.`

Use `if` for mathematical conditions and `when` for a variable taking a value if that is the convention in context.

## That

Use `that` after `assume` and `suppose` when it helps parsing:

- `Assume that f is continuous.`
- `Suppose that there exists a point x such that ...`.

Avoid `we have that x=y`; write `we have x=y`.

## Where

Do not use `where` to define a term after using it. Define important terms before they are used. A late `where` often signals an overloaded sentence.

## Demonstratives

Avoid naked `this`, `that`, `these`, and `those`. Qualify them:

- `this estimate`;
- `that assumption`;
- `these experiments`;
- `those iterates`.

If the referent is still ambiguous, rewrite the sentence.

## Citations in sentences

Name authors when the citation is the grammatical subject or when it improves the story:

- `Smith and Jones [12] prove ...`.
- `The deterministic case was studied by Smith [12].`

Avoid beginning a sentence with a citation label.

## Active and passive voice

Prefer active voice when it is clearer and shorter:

- `We estimate the error using ...`.
- `Table 4 shows that ...`.

Use passive voice when the actor is irrelevant or when the mathematical object should be the subject.

## Adjectives and adverbs

Do not use adjectives and adverbs as substitutes for evidence. Replace vague evaluation by quantitative or structural information.

- Instead of `very accurate`, state the error level.
- Instead of `clearly efficient`, state the complexity or observed cost.
- Remove redundant intensifiers such as `completely failed` when `failed` suffices.

## Avoid double negatives

Rewrite double negatives and negative-without constructions when they obscure the claim.

- Prefer `To guarantee convergence, assume ...` over `Convergence is not guaranteed without ...`.

## Parallel enumeration

Items in a list should be grammatically parallel. If a list begins with verbs, every item should begin with a verb. If it begins with nouns, every item should be a noun phrase.

Bad structure:

```text
The method has three advantages:
1. Reduces storage.
2. The proof is simpler.
3. It can be implemented efficiently.
```

Better:

```text
The method has three advantages:
1. lower storage;
2. a simpler proof;
3. efficient implementation.
```

## Dangling participles

When a sentence begins with a participial phrase, the following subject should be the actor of that phrase.

Bad:

```text
Using random test data, a bug was found in the implementation.
```

Better:

```text
Using random test data, we found a bug in the implementation.
```

## Sentence openings

Avoid overusing `It is`, `There are`, `There is`, `It can be seen`, and `Also`. These often hide the subject.

- `Table 2 shows ...` is usually better than `It can be seen from Table 2 that ...`.
- `Ties can be broken in three ways` is usually better than `There are three possibilities that can be used to break ties`.

## Confused words

Check the following pairs:

- `affect` as verb, `effect` as noun;
- `alternative` vs `alternate`;
- `compare with` for similarities/differences;
- `comprise`, `compose`, `constitute`;
- `fewer` with count nouns, `less` with mass nouns;
- `phenomenon` singular, `phenomena` plural;
- `criterion` singular, `criteria` plural;
- `discrete` mathematical, `discreet` tactful;
- `supersede`, not common misspellings;
- `lose`, not `loose`, when meaning fail to retain;
- `its` possessive, `it's` contraction;
- `MATLAB`, not `Matlab`.

## Formal writing

Do not use contractions in formal manuscripts. Capitalize named numbered objects: Theorem 1, Lemma 2, Algorithm 3, Problem 4, Figure 5, Table 6, Section 7.
