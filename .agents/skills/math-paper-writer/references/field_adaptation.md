# Field Adaptation

Use this reference to adapt the skill to different mathematical disciplines
without importing assumptions from optimization, numerical analysis, or any
single field.

## First identify the discipline

Before reviewing or drafting, identify the paper's mathematical culture:

- pure theory: algebra, geometry, topology, number theory, logic, category
  theory, analysis, combinatorics;
- probability, statistics, stochastic processes, information theory;
- applied mathematics, differential equations, control, inverse problems,
  mathematical biology, mathematical physics;
- numerical analysis, optimization, scientific computing, computational
  mathematics;
- theoretical computer science, algorithms, complexity, cryptography;
- interdisciplinary work using mathematical methods in another domain.

If the field is unclear, infer from definitions, theorem style, cited venues,
and notation, then state the assumption briefly.

## Preserve local conventions

Check field conventions before changing notation or prose:

- theorem naming and hierarchy;
- preferred notation for objects and morphisms/maps/operators;
- standard names for assumptions;
- citation density and placement;
- proof style: constructive, contradiction, diagrammatic, probabilistic,
  variational, asymptotic, computational, or categorical;
- whether examples, counterexamples, algorithms, or experiments are central.

Do not "normalize" a manuscript into another field's style merely because it is
more familiar.

## Universal checks

These apply across mathematical disciplines:

- objects and domains are defined before use;
- quantifiers and dependencies are explicit;
- theorem statements are no stronger than proofs;
- proof steps are justified and type-correct;
- notation has stable meaning;
- prior work is represented accurately;
- limitations are stated where claims could be overread.

## Field-sensitive checks

Pure theory:

- confirm definitions, universal properties, equivalence of formulations,
  counterexamples, edge cases, and dependence on choice or set-theoretic
  assumptions when relevant.

Analysis and PDE:

- check topology, norm, convergence mode, regularity, boundary conditions,
  compactness, weak/strong formulation, and limit interchanges.

Probability and statistics:

- check probability spaces, filtrations, measurability, independence,
  conditioning, modes of convergence, asymptotics, estimands, and uncertainty.

Numerical analysis and optimization:

- check constants, oracle model, conditioning, finite precision, stopping
  criteria, complexity model, and reproducibility of experiments.

Discrete mathematics and theoretical computer science:

- check reductions, asymptotic notation, input model, randomized vs
  deterministic guarantees, edge cases, and construction size.

Interdisciplinary mathematics:

- separate mathematical claims from domain claims and verify each through the
  appropriate evidence route.

## External support

Use external research, citation, symbolic, numerical, or visualization tools
only when they fit the field. Re-audit their output under the universal checks
before treating it as manuscript-ready.
