# Workspace Agent Instructions

## Communication

- Use Chinese for user-facing discussion unless the user requests another language.
- Keep code, code comments, shell commands, configuration, filenames, and TeX code in English.

## Project-local skills

- The project-local mathematical writing skill is installed at:
  `.agents/skills/math-paper-writer/SKILL.md`.
- Use `math-paper-writer` for mathematical paper drafting, theorem/proof audits,
  notation review, introduction and related-work review, numerical-experiment
  reporting, bibliography checks, LaTeX production checks, and final submission
  review.
- For any substantive mathematical writing task, read the skill's `SKILL.md`
  first, then load only the relevant reference, playbook, asset, or script files
  named by its progressive reading protocol.

## Mathematical writing

- Preserve mathematical correctness over stylistic smoothness.
- Do not invent citations, theorem assumptions, numerical results, datasets, or proof steps.
- Mark unsupported factual claims with `[citation needed]` or `[verification needed]`.
- When editing proofs, preserve quantifiers, domains, assumptions, constants, and inequality directions.
- If a proof step is questionable, report the exact step before rewriting.

## Paper workflow

- Store drafts in `drafts/` when possible.
- Store review reports in `reviews/` when possible.
- Before finalizing a theorem or proof, run a proof audit.
- Before finalizing experiments, check reproducibility details.
- Before final submission, perform six-pass proofreading.
