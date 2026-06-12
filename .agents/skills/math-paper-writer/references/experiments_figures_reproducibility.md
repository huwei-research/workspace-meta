# Experiments, Figures, Tables, and Reproducibility

## Purpose of experiments

Numerical experiments should answer a question. Do not report tables merely because code was run. Identify the experimental question before interpreting results:

- Does the method converge when the theory predicts it should?
- Does it outperform a baseline under specified conditions?
- Does it illustrate a sharpness, failure mode, or limitation?
- Does it show sensitivity to dimension, noise, conditioning, sample size, tolerance, or hyperparameters?

## Reproducibility contract

An experiment section should give enough detail for interpretation and repetition. Record:

- hardware or relevant computing environment;
- arithmetic precision;
- software versions;
- compiler and options if compiled code matters;
- BLAS/LAPACK or numerical library when relevant;
- random-number generator and seed policy;
- data sources or instance-generation rules;
- stopping criteria;
- tolerances;
- failure criteria;
- number of repetitions;
- aggregation method;
- metrics;
- baselines;
- repository or supplementary materials when available.

When some details are unknown, mark them as missing rather than invent them.

## Objective statement vs speculation

Separate observed facts from interpretation.

Observed:

- `On these 120 instances, Method A required fewer median function evaluations than Method B.`

Speculative:

- `This suggests that the sampling rule is more robust to noise in this regime.`

Do not turn speculation into a theorem or a universal claim.

## Digits and precision

Report only as many digits as are meaningful. Excess digits create false precision. Align significant figures with experimental variability and measurement error.

## Extrapolation

Be wary of claims beyond the tested range. A log-log plot over two decades does not establish an asymptotic law unless the paper gives additional evidence or theory. If extrapolating, state it as a conjectural interpretation.

## Tables

Use tables for small sets of numbers and exact comparisons. Keep tables simple. Use minimal rules. Put quantities to be compared in columns when that makes comparisons easier. Every table should have a caption that states what is varied, what is measured, and what is better.

Audit questions:

- Are units and metrics defined?
- Are baselines identified?
- Are failure cases shown rather than hidden?
- Are bold entries meaningful and explained?
- Is the table too dense for the conclusion it supports?

## Figures

Use graphs for trends, large datasets, distributions, scaling behavior, and qualitative patterns. Figures must be readable after resizing. Labels, legends, markers, and captions should allow interpretation without searching the text.

Audit questions:

- Is the axis scale appropriate and stated?
- Are log scales justified?
- Are error bars or variability shown when needed?
- Are methods distinguishable in grayscale or print?
- Does the caption state the experimental setting?
- Does the text interpret the figure without overstating it?

## MATLAB and code output

Use typewriter formatting for code, function names, variables, and output. Keep code/output visually distinct from prose. Do not materially alter code output; minor cleanup such as removing blank lines is acceptable if it does not change content.

When reporting MATLAB, use `MATLAB` capitalization and refer to functions without possessive constructions that obscure names.

## Experimental claims in abstract and introduction

If the abstract says experiments show superiority, the experiment section must specify: superiority by which metric, against which baselines, on which problem class, and under what setup. Otherwise weaken the claim.

## Artifact recommendation

For computational papers, recommend a permanent repository or supplementary material containing code, data, environment information, and scripts to reproduce tables and figures.
