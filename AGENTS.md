# Workspace Agent Instructions

## Scope

- This file is the workspace-level constitution for `2026Projects`.
- Project-local `AGENTS.md` files inside `Research/`, `Publish/`, `Public/`,
  `Experimental/`, and `Personal/` repositories add project-specific context.
- When instructions conflict, follow the more local `AGENTS.md` for project
  details, while preserving the research-integrity rules in this file.
- Each child directory with its own `.git/` is an independent repository.
  Do not mix workspace-meta commits with child-project commits.
- When creating a new child repository, create a project-local `AGENTS.md` before
  the first substantive code, paper, or experiment commit. Start from
  `.agents/templates/project_agents_template.md` and specialize it to the
  project.

## Mission

This workspace supports mathematical optimization research, especially
derivative-free optimization, trust-region methods, model-based optimization,
Riemannian optimization, distributed second-order methods, and reproducible
numerical experiments tied to LaTeX manuscripts.

The agent's job is not just to edit files. The agent must protect mathematical
truth, reproducibility, publication readiness, and the continuity of each
research thread.

## Communication

- Use Chinese for user-facing discussion unless the user requests another
  language.
- Keep code, code comments, shell commands, configuration, filenames, labels,
  BibTeX keys, and TeX code in English.
- Be explicit about assumptions, uncertainty, and verification gaps.
- For review tasks, lead with concrete findings and file/line references.

## Research Integrity

- Mathematical correctness is prior to style, speed, and narrative smoothness.
- Do not invent citations, theorem assumptions, proof steps, algorithms,
  datasets, numerical results, author names, journal names, URLs, or dates.
- Mark unsupported factual claims with `[citation needed]` or
  `[verification needed]`.
- Separate diagnosis from rewriting. If a proof, result, or experiment is
  questionable, report the issue before polishing the prose.
- Preserve theorem labels, equation labels, references, bibliography keys,
  notation, constants, quantifiers, domains, and inequality directions unless
  the user explicitly asks for a structural refactor.
- Claims about superiority, complexity, robustness, or scalability must be
  supported by a theorem, proof, experiment, citation, or clearly stated
  conjecture.

## Skill Routing

- Use `.agents/skills/research-orchestrator/SKILL.md` as the master entry point
  for nontrivial literature reading/search, research-direction analysis,
  manuscript review/writing/revision, numerical experiment design/execution,
  result analysis, peer review, and resumable multi-stage research work. It
  must audit the governed corpus, create full-corpus coverage, and route only
  the next specialist skill.
- Use `.agents/skills/math-paper-writer/SKILL.md` for mathematical paper
  drafting, theorem/proof audits, notation review, introduction and related-work
  review, numerical-experiment reporting, bibliography checks, LaTeX production
  checks, response-to-reviewers work, and final submission review.
- For substantive writing tasks, first read that skill's `SKILL.md`, then load
  only the relevant reference, playbook, asset, or script files named by its
  progressive reading protocol.
- Use `CONVENTIONS.md` for workspace layout, naming, code, experiment, results,
  figure, and sync conventions.
- Use project README files and project-local `AGENTS.md` files before making
  project-specific claims.

## Mathematical Writing Workflow

- Before drafting more than one paragraph, identify the reader, purpose, main
  claim, scope, evidence, and risk.
- Before editing a theorem or proof, identify objects, assumptions, domains,
  quantifiers, constants, dependencies, and where each result is used.
- Audit proofs line by line before rewriting them. Check equalities,
  inequalities, implications, equivalences, hidden assumptions, and boundary
  cases.
- Treat equations as parts of sentences. Introduce displayed equations with
  prose and punctuate them when appropriate.
- Integrate references into the narrative. Do not dump prior work into an
  isolated list unless the section is explicitly a bibliography note.
- Store drafts in `drafts/` when possible and review reports in `reviews/` or
  the project's established report directory.

## Experiment Workflow

- Reproducibility is part of the result. Record seeds, environment, problem set,
  solver versions, budgets, stopping rules, and plotting scripts for paper-grade
  experiments.
- Formal paper results belong in tracked paper/result directories with a
  `REPORT.md` or an equivalent project report. Scratch runs belong in scratch
  directories and should not be promoted without an audit.
- Never change raw results merely to match a narrative. If results contradict
  the story, revise the story or mark the gap.
- Distinguish objective observations from interpretation. Do not extrapolate
  beyond the tested problem classes, dimensions, budgets, or noise models.
- Regenerate figures from raw CSV/JSON/source data when possible instead of
  editing exported figures by hand.

## Code Workflow

- Prefer the existing project architecture and helper APIs over new abstractions.
- Keep changes scoped and reviewable. Do not refactor unrelated code while
  editing a manuscript, and do not rewrite manuscript prose while fixing a code
  bug unless the user requested both.
- Use `pathlib.Path` for Python paths. Avoid hardcoded platform separators.
- Run the narrowest meaningful checks first, then broaden when touching shared
  solvers, experiment pipelines, or public APIs.
- Public repositories must not receive private notes, unpublished manuscript
  sources, local benchmark outputs, or confidential reviewer material.

## LaTeX And Publication Workflow

- Compile from the directory and entry file documented by the project-local
  `AGENTS.md` or README.
- Keep generated LaTeX artifacts out of the repository unless the project
  explicitly tracks PDFs or source packages.
- Before final submission, perform a six-pass review: mathematical accuracy,
  organization, meaning flow, English/style, read-aloud clarity, and submission
  risk.
- For arXiv or journal bundles, verify a clean build from the packaged source,
  not just the working manuscript tree.

## Git And Sync

- The workspace root is the `workspace-meta` repository. It tracks shared
  conventions, setup scripts, Cursor rules, and project-local agent skills.
- Category directories are ignored by the root repository because they are
  independent child repositories.
- Before committing in a child repository, inspect that child's `git status`.
  Do not include unrelated user changes in commits.
- If several child repositories need commits, commit them separately with
  project-specific messages.
- Do not run destructive git commands such as `reset --hard` or `checkout --`
  unless the user explicitly asks for them.
- New projects are not considered fully initialized until they have README,
  `.gitignore`, `.gitattributes`, and a project-local `AGENTS.md`.
