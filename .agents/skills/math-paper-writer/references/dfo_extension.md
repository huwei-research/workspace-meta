# Derivative-Free Optimization Extension

Use this extension for derivative-free optimization, zeroth-order optimization, model-based trust-region methods, direct search, stochastic DFO, and black-box optimization papers.

## Problem contract

Check that the manuscript states:

- objective type: deterministic, noisy, stochastic, simulation-based, nonsmooth, constrained, composite, or multiobjective;
- domain and constraints;
- oracle model: function values, noisy values, comparison oracle, random samples, constraints, failures;
- smoothness assumptions;
- stationarity notion;
- evaluation budget and complexity measure.

## Model assumptions

For model-based DFO, check:

- fully linear, fully quadratic, probabilistically fully linear, or other model accuracy condition;
- norm used in model accuracy;
- ball or trust-region where accuracy holds;
- constants and whether they are uniform in `k`;
- relation between sample geometry and model accuracy;
- whether poisedness or interpolation assumptions are defined before use;
- whether the trust-region radius in the theorem matches the one in the algorithm.

## Algorithm specification

The algorithm must specify:

- initialization;
- sample-set construction;
- model construction;
- step computation;
- acceptance test;
- trust-region radius update;
- geometry-improvement step if any;
- stopping criterion;
- handling of failed evaluations or noise;
- randomization and seed policy if stochastic.

## Decrease and acceptance logic

Audit every decrease inequality:

- predicted reduction vs actual reduction;
- model decrease vs function decrease;
- sufficient decrease constants;
- Cauchy decrease or criticality step conditions;
- sign and absolute-value handling;
- upper/lower model error bounds;
- whether successful and unsuccessful iterations are separated.

## Stationarity

Check that the stationarity measure matches the theorem:

- gradient norm;
- projected gradient or criticality measure;
- Clarke stationarity;
- approximate first-order stationarity;
- second-order stationarity;
- stochastic stationarity in expectation or high probability.

Do not allow the abstract to claim `convergence to a stationary point` if the theorem proves only `liminf` stationarity, subsequential stationarity, expected stationarity, or convergence of a measure.

## Complexity

State whether the bound is measured in:

- iterations;
- function evaluations;
- samples;
- oracle calls;
- successful iterations;
- total iterations including geometry steps;
- wall-clock time.

Check that the tolerance in the complexity bound matches the stationarity measure. Check dependencies on dimension, Lipschitz constants, noise variance, failure probability, model constants, and geometry constants.

## Stochastic and noisy DFO

Separate:

- unbiased noise;
- bounded variance;
- sub-Gaussian tails;
- deterministic bounded noise;
- common random numbers;
- sample-average approximation;
- high-probability model events;
- conditional expectations.

When events are combined across iterations, check union bounds, independence assumptions, conditioning, and summability.

## Experiments for DFO

DFO experiments should report:

- function-evaluation budget;
- dimension;
- starting points;
- noise model and noise level;
- performance and data profiles if appropriate;
- success definition;
- random seeds or repetitions;
- baseline solvers and parameter settings;
- failure handling;
- scaling with dimension and noise when claimed.

Avoid saying a method is `efficient` without specifying function evaluations, success criteria, and tested problem class.
