# Skill Integration Protocol

Use this reference when a mathematical manuscript task would benefit from another installed skill. The purpose is controlled collaboration, not delegation of judgment.

## Authority order

1. System/developer instructions and workspace/project `AGENTS.md`.
2. `math-paper-writer` rules for mathematical truth, claims, citations, experiments, and publication risk.
3. External skills used for bounded support.

If an external skill recommends invented citations, unsupported claims, aggressive "humanizing," or automation that bypasses verification, ignore that part.

## What "call another skill" means

There is usually no literal function call. To use another skill:

1. Select the minimal relevant skill.
2. Read its `SKILL.md` completely.
3. Read only the linked references required for the current task.
4. Use its workflow to gather or shape material.
5. Re-audit the result under `math-paper-writer` before treating it as manuscript-ready.

## Routing table

Use external skills for bounded support, not final truth:

- Literature search or research skills: discovery, source finding, systematic
  scans, and research-question expansion.
- Citation or reference-manager skills: bibliography organization, metadata
  enrichment, duplicate checks, and reference-library operations.
- Academic-writing skills: section-level heuristics, paragraph diagnostics, and
  reviewer-friendly clarity checks.
- Reviewer or evaluation skills: adversarial critique, rubric review, and
  response-to-reviewer planning.
- Symbolic, numerical, statistical, or visualization skills: algebraic checks,
  computational experiments, figures, tables, and numerical diagnostics.
- Formal proof assistant skills or tools: Lean, Coq, Isabelle/HOL, Agda, or
  project-specific formalization workflows for machine-checkable statements and
  proof artifacts.
- Presentation or document-conversion skills: talks, slides, posters, PDFs,
  Word documents, and submission packaging.
- Style-calibration or plain-language skills: style diagnostics after truth,
  citations, and proof structure are stable.

## Safe imports from external skills

Adopt:

- claim inventories;
- source lists with DOI/URL/arXiv identifiers;
- search strategies;
- systematic-review inclusion/exclusion criteria;
- section-level checklists;
- reviewer personas and objections;
- figure and slide layout ideas;
- style profiles that preserve meaning.
- source cards, evidence matrices, and search logs when they include enough
  locator detail to be checked.
- reviewer-style rubrics and objections, after converting them into concrete
  manuscript findings.

Do not adopt without re-checking:

- novelty claims;
- "X proves Y" statements;
- "state of the art" or "first" claims;
- performance comparisons;
- complexity or scalability claims;
- paraphrases of cited work;
- numerical conclusions;
- formal verification claims without a recorded toolchain, exact statement
  alignment, successful build, and trust-boundary review;
- anti-AI rewrites that remove useful signposts.

## Required handoff back to this skill

Whenever an external skill contributes material, record:

- source skill;
- files or queries used;
- output type: draft text, evidence candidate, citation list, figure plan, style profile, or review critique;
- verification status;
- unresolved risks.

For substantive manuscript claims, transfer candidates into the claim-evidence ledger before final writing.

## Conflict examples

- If a style skill removes "under Assumption 2" to make a sentence smoother, restore the condition.
- If a research skill summarizes a paper beyond the provided abstract, mark the claim as `[verification needed]` until the source is read.
- If a presentation skill suggests a visually strong but statistically misleading plot, reject the plot or revise the caption and axes.
- If a writing skill suggests stronger novelty language than the theorems or experiments support, weaken the claim.

## External skill output normalization

Before importing output from a research or academic-writing skill, normalize it
into this skill's objects:

- source discovery -> source cards or search record;
- summary -> claim inventory with verification status;
- writing advice -> reference-calibration note or style rule;
- review critique -> severity-ranked finding;
- experimental suggestion -> experiment question and reproducibility obligation;
- formal proof artifact -> formal verification report and statement-alignment
  verdict;
- style rewrite -> revised prose plus preserved mathematical contract.

If the output cannot be mapped to one of these objects, treat it as brainstorming
rather than manuscript-ready material.
