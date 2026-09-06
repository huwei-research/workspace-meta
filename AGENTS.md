# Workspace Agent Instructions

## Scope and Priorities

- This workspace supports mathematical optimization research and reproducible software.
- Follow the user's current task and preferences; scale the process to the actual work.
- Use the exact filename `AGENTS.md` for maintained instructions.
- Read this file, the target category's `AGENTS.md`, the project's `AGENTS.md` and README,
  and any instructions between that project root and the files being changed.
- Apply relevant sections of `CONVENTIONS.md` for directory, naming, version, and artifact
  defaults. Read only the sections needed for the task.
- Runtime instructions and the user's task take priority. Within workspace documents,
  local rules specialize paths, notation, commands, and explicitly documented exceptions;
  they must retain the research-integrity, privacy, and Git boundaries below.
- If documents disagree, use verified project facts to correct stale guidance within scope.
  Report unresolved material ambiguity; do not invent an authority or silently rename files.

## Instruction Responsibilities

| Layer | Responsibility | Git owner |
|---|---|---|
| Workspace `AGENTS.md` | Shared boundaries and instruction-reading contract | `workspace-meta` |
| Workspace `CONVENTIONS.md` | Detailed defaults, naming, versioning, and maintenance | `workspace-meta` |
| Category `AGENTS.md` | Category purpose, allowed contents, and handoff rules | `workspace-meta` |
| Project `AGENTS.md` | Actual paths, authority, exceptions, mathematics, and checks | That project's repository |
| Subdirectory `AGENTS.md` | Additional rules for that subtree only | Its containing repository |

- Category directories are organizational containers, not independent repositories.
  Their instruction files are the only category contents tracked by `workspace-meta`.
- Independent Git roots may prevent automatic loading of workspace/category instructions.
  Project instructions must explicitly direct agents to read these files when available,
  and retain enough guidance to work from a standalone clone.
- Paths in a project instruction file are relative to that project root unless explicitly
  marked otherwise; paths in a subdirectory file are relative to that directory.
- Keep shared rules at their owning layer. README files explain use and index the same
  entry points; Cursor rules and local convention stubs link to the owning instructions.
- Add a subdirectory instruction file only for a real local contract. Do not duplicate
  the complete parent file or add instructions to every ordinary folder.
- Instructions in frozen snapshots, backups, vendored sources, and separate Git worktrees
  are not guidance for the primary checkout. Preserve those versions during bulk maintenance;
  update another active worktree only as a separate, coordinated change.
- After changing an entry point or policy, update affected instructions, README links,
  build/config references, and templates together. See `CONVENTIONS.md` section 1.

## Project Organization

- Use the project-local path map before creating files. Preserve established layouts;
  new code/paper/results directories are created only when needed.
- Each artifact role has one declared editable authority. Mark mirrors, derived exports,
  archived versions, and frozen releases explicitly; never edit a mirror as the source.
- Keep reusable code, experiment drivers/configs, evidence, manuscript assets, notes,
  and temporary build output in their documented locations.
- Prefer stable descriptive filenames for new working sources and Git history for edits.
  Retain documented versioned entry points and API names until a scoped migration.
- Keep dated or versioned snapshots immutable, with a source revision and provenance.
  Record code versions, manuscript revisions, experiment runs, and submissions separately.
- Classify results by evidence status and release permission, not just extension or folder
  name. `Public/` is a code-release category, not proof of remote visibility or publication.

## Communication and Autonomy

- Use Chinese for discussion unless the user requests another language.
- Use English for code, comments, configuration, filenames, and TeX identifiers.
- Lead reviews with concrete findings and file/line references.
- State material assumptions, uncertainty, and verification gaps.
- Complete authorized, reversible work without repeating permission requests.
- Ask when missing information or authorization materially affects the next action.
- Keep reports proportional to the task; avoid mandatory plans and fixed review rounds.

## Skills

- Respect the user's current enabled-skill policy.
- That policy overrides older mandatory skill-routing clauses in project instructions.
- Skip references to disabled skills while retaining project facts and integrity requirements.
- Do not reactivate, reinstall, or substitute a disabled workflow without user authorization.
- Use an enabled skill when explicitly requested or when its specific capability helps.
- Keep skill use scoped to the task; no mandatory master router or fixed agent pipeline.
- `grill-me` is for requested plan or design interrogation, not a gate for routine work.
- Do not expand a local task into a full-corpus audit unless the task requires it.

## Mathematical and Research Integrity

- Mathematical correctness takes priority over style and narrative.
- Never invent citations, assumptions, proof steps, data, numerical results, or publication status.
- Mark unsupported factual claims with `[citation needed]` or `[verification needed]`.
- Distinguish evidence, interpretation, and conjecture.
- Before substantive proof changes, inspect relevant assumptions, domains, and dependencies.
- Check the affected derivation and boundary cases to the depth warranted by the change.
- Report mathematical defects before presenting polished text as correct.
- Preserve notation, labels, references, constants, quantifiers, and inequality directions by default.
- Make justified corrections within the authorized task and explain their mathematical impact.
- Verify downstream uses when changing a result or assumption.
- Support performance and complexity claims within the actual theorem or experimental scope.

## Experiments and Artifacts

- Preserve raw results; never alter them to support a preferred narrative.
- Separate formal results, exploratory runs, and archived outputs.
- For paper-grade runs, record code revision, environment, seeds, problems, solver versions,
  budgets, stopping rules, commands, and runtime-relevant hardware.
- Choose settings and metrics for the research question; document actual choices and fair comparisons.
- Keep figures reproducible from recorded source data and plotting code.
- Use the project's documented manuscript entry point and build directory.
- Keep generated LaTeX artifacts untracked unless the project explicitly tracks them.
- Verify submission bundles with a clean build from the packaged source.
- Report what was verified and what remains unverified.

## Code, Privacy, and Git

- Prefer existing architecture and helper APIs; keep changes scoped and reviewable.
- Use `pathlib.Path` for Python filesystem paths.
- Run the narrowest meaningful checks; broaden when shared behavior or evidence requires it.
- Keep private notes, unpublished manuscripts, local benchmark outputs, and confidential
  reviewer material out of public repositories unless the user explicitly authorizes publication.
- Never commit credentials or secrets.
- The workspace root (`workspace-meta`) and each child repository are independent Git boundaries.
- A `.git` file also marks a Git worktree boundary. Do not recursively stage its contents
  from a parent checkout or infer its branch from the parent.
- Inspect the target repository's status before staging or committing.
- Preserve unrelated user changes; stage only changes belonging to the authorized task.
- Commit separately in each repository; routine work does not authorize a push.
- Before an authorized push, verify the actual remote, destination branch, visibility,
  and outgoing commits against `workspace-repos.json` and the current task. Stop on a
  mismatch rather than changing branches or remotes to make a bulk sync pass.
- A private branch on a public remote does not protect unpublished material. Keep private
  research on private remotes; repository category and branch name are not access controls.
- Do not use destructive Git commands or delete user work without explicit authorization.
- For new repositories, create README, `.gitignore`, `.gitattributes`, and project-local
  `AGENTS.md` before substantive commits; tailor `.agents/templates/project_agents_template.md`.
