# Revision, Production, Bibliography, and Submission

## Start early

Writing is part of understanding. A rough draft reveals missing assumptions, unclear notation, weak motivation, and overclaimed results. Do not wait until all mathematics is complete before drafting the story.

## Revision by selection

Brevity comes from choosing what belongs, not merely compressing what is there. When revising:

1. Remove material that does not serve the reader path.
2. Move results to where they are needed.
3. Split overloaded paragraphs.
4. Replace symbolic clutter by conceptual explanation.
5. Shorten only after the structure is right.

## Six-pass proofreading

Perform six separate passes. Do not combine them into one vague read.

### Pass 1: mathematical accuracy

Check theorem statements, assumptions, proof dependencies, equality/inequality directions, quantifiers, domains, constants, and probabilistic modes.

### Pass 2: organization and logic

Check section order, paragraph purpose, transitions, result placement, missing roadmaps, and unused assumptions.

### Pass 3: sense and flow

Check whether the reader knows why each object, lemma, and example appears. Remove distractions and unexplained shifts.

### Pass 4: spelling and syntax

Check grammar, mathematical English, punctuation, labels, capitalization, articles, singular/plural, and equation punctuation.

### Pass 5: sound and readability

Read aloud when possible. Detect long subject-verb separations, clumsy rhythm, repeated openings, and ambiguous demonstratives.

### Pass 6: overall coherence

Check whether the abstract, introduction, theorem statements, experiments, and conclusion make the same claims under the same assumptions.

## Plain text and version control

Prefer plain-text authoring formats such as LaTeX, Markdown, or Org mode. Avoid proprietary formats for core source when possible. Use Git or another version-control system. Do not create version names such as `paper1.tex`, `paper2.tex`, `final_final.tex`, or `submission_new_revised2.tex`.

## LaTeX production

Audit for:

- no `$$ ... $$` display math in LaTeX manuscripts;
- no obsolete `eqnarray` unless the project explicitly requires it;
- consistent theorem environments;
- descriptive labels such as `thm:main`, `lem:model-error`, `eq:cauchy-decrease`, `fig:performance-profile`;
- all references resolved;
- equation punctuation;
- no oversized inline equations;
- consistent macros for repeated objects;
- no manual spacing hacks hiding structural problems;
- no unused or conflicting notation macros.

## Bibliography

Bibliography entries deserve proofreading as much as the main text. Downloaded BibTeX entries often contain inconsistencies. Check:

- author names;
- title capitalization;
- journal or proceedings names;
- volume, number, pages, year;
- DOI or URL if required;
- duplicate entries;
- arXiv vs published version;
- style consistency;
- preservation of capitalization for proper nouns and acronyms.

Every citation in the text should be in the bibliography, and every bibliography entry should be cited unless the style allows uncited references.

## Proofreading mindset

Proofreading is not only spell checking. It includes detecting wrong words that are real words, semantic reversals, implausible statements, typography-induced errors, OCR mistakes, missing mathematical symbols, and facts that sound wrong.

When doing final checks, slow down. Read captions, bibliography, acknowledgements, author names, theorem labels, axis labels, and table headings. These areas often contain errors because authors stop paying attention.

## Submission readiness

Before submission, produce a blocking-risk report:

- blocking: mathematical falsehood, missing proof, missing citation for central claim, irreproducible critical experiment, unresolved references;
- major: unclear contribution, theorem overstatement, notation conflict, incomplete experiment detail;
- minor: style, grammar, table formatting, label naming;
- optional: elegance improvements.
