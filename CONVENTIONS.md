# Project Conventions

This file owns the workspace defaults for project structure, naming, versioning,
and reproducibility. `AGENTS.md` owns shared integrity, privacy, and Git boundaries.
Project instructions own verified project facts and documented exceptions.
Apply the relevant sections; a template is not an instruction to restructure an
existing project or create unused directories.

## 1. Instruction Hierarchy and Maintenance

### 1.1 Reading and scope

Read the workspace `AGENTS.md`, category `AGENTS.md`, project `AGENTS.md` and README,
then applicable subdirectory instructions before changing files in that subtree.
Each local file adds context within its scope; it retains shared integrity and
repository boundaries. The user's current task and enabled-skill policy take
priority over older workflow clauses.

Codex normally discovers project instructions from the Git root down to its
working directory. Thus, a child repository must explicitly point to workspace
and category instructions when available. A standalone clone must still state
its essential safeguards, actual paths, and usable verification commands.
See the [official instruction discovery documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md).

Use the exact filename `AGENTS.md`. Avoid alternate spellings and competing
`AGENTS.override.md` files for permanent workspace policy. Do not assume a
README or a local `CONVENTIONS.md` is automatically loaded as instructions.
Keep the automatically loaded instruction chain concise; detailed examples and
research records belong in linked documentation.

### 1.2 Ownership and exceptions

| Document | Owns | Must not duplicate |
|---|---|---|
| Workspace `AGENTS.md` | Shared boundaries and reading contract | Project inventories and long examples |
| Workspace `CONVENTIONS.md` | Detailed defaults | Live branch/status inventories |
| Category `AGENTS.md` | Role, contents, and transitions | Every project's path map |
| Project `AGENTS.md` | Actual entry points, local rules, commands, exceptions | Whole workspace policy |
| Subdirectory `AGENTS.md` | Rules specific to that subtree | The complete parent file |
| README / focused guides | User-facing setup and navigation | A competing policy |
| `workspace-repos.json` | Managed remotes, branches, visibility, sync eligibility | Research/publication claims |

Document each meaningful exception with its actual path, purpose, and reason.
Existing package layouts, versioned manuscripts, result protocols, imported
filenames, and immutable historical records are valid exceptions. Do not
silently rewrite them to match a generic template.

Resolve a disagreement using the relevant authority and existing evidence.
When evidence does not identify the current manuscript or intended destination,
record that gap and resolve it before a dependent edit. File modification time,
the largest version suffix, folder category, and a journal template are not
authority or publication evidence.

### 1.3 Maintaining a rule

1. Edit the layer that owns the rule.
2. Check affected category/project instructions, local convention stubs, Cursor
   pointers, README entry points, and templates.
3. Verify referenced paths and the working directory of documented commands.
   Distinguish implemented checks from planned checks and expensive full runs.
4. Inspect the diff in each independent repository and preserve unrelated work.
5. Report the coverage and unresolved facts. A structural audit cannot certify
   mathematical correctness or guarantee that all semantic conflicts are absent.

Historical snapshots, backups, third-party checkouts, and other Git worktrees
retain their own versioned instructions. Do not rewrite them during a primary
checkout policy update. Coordinate another active worktree separately.

## 2. Workspace Categories and Repository Boundaries

`workspace-repos.json` is the managed synchronization inventory. The actual Git
state must also be checked before synchronization; a manifest can become stale.
Most managed repositories use `huwei-research`, but owners and remote names are
defined per entry. Do not maintain another complete hand-written repository list.

| Directory | Role | Default handling |
|---|---|---|
| `Research/` | Active theory, code, experiments, and working manuscripts | Private research |
| `Publish/` | Publication working sources and frozen delivery packages | Private until a particular release is authorized |
| `Public/` | Code intended for external use | Public-safe contents; actual visibility is separate |
| `Experimental/` | Exploratory studies and prototypes | Private or local-only |
| `LiteratureLibrary/` | Literature tooling and private source/evidence stores | Separate distributable tools from private corpus |
| `Personal/` | Personal repositories and private local documents | Private; many folders are manual-transfer only |
| `Archive/` | Historical snapshots and provenance | Local preservation, no active editing |
| `tmp/` | Disposable workspace scratch | Ignored; never the only copy of evidence |

The workspace root is `workspace-meta`. It tracks shared rules, templates,
scripts, the manifest, and each category's `AGENTS.md`. All other category
contents stay excluded from the root repository. A child repository owns its
project metadata and contents. A `.git` file marks a worktree boundary just as
a `.git` directory marks a repository boundary.

Preserve established repository names, including uppercase acronyms, PascalCase,
and canonical lowercase names such as `seertr`. Use `{Project}-paper` for a new
paper-only counterpart when that split is needed. Category changes, repository
renames, and research/publication splits are explicit migrations.

Local-only folders and repositories may intentionally lack a remote or a
managed inventory entry. Follow their local instructions and manual-transfer
record; absence from the manifest is not permission to publish or add a remote.
Inventory discrepancies belong in the maintenance report until reconciled.

Branches on the same remote share that remote's visibility. A research branch
on a public repository is not private. The `Public/` category may contain private
release candidates; verify actual remote visibility before an authorized push.

## 3. Project Structure and File Placement

### 3.1 Minimum project metadata

An independent repository needs `README.md`, `AGENTS.md`, `.gitignore`, and
`.gitattributes` before substantive project commits. Add dependency metadata
when code needs it. Preserve the existing license and third-party notices;
select a license only as part of an authorized release decision.

Use `.agents/templates/project_agents_template.md` for new project instructions.
Create a subdirectory `AGENTS.md` only when a subtree has its own contract, using
`.agents/templates/subdirectory_agents_template.md`.

### 3.2 Research layout defaults

Create only the directories the project uses:

```text
PROJECT/
  README.md
  AGENTS.md
  .gitignore
  .gitattributes
  paper/                   # Manuscript authority, if owned by this repository
    {project}_main.tex      # Stable entry point for a new manuscript
    {project}_shared.tex
    {project}_refs.bib
    figures/               # Assets actually included by the manuscript
    tables/
    build/                 # Ignored compiler output
    archive/               # Documented historical snapshots
  codes/                   # Default code root; existing src/package layouts are valid
    README.md
    pyproject.toml         # Or language-appropriate build/dependency metadata
    configs/
    core/
    solvers/
    problems/
    experiments/           # Drivers: paper, benchmarks, ablation, analysis, research
    scripts/               # Reusable build, analysis, and maintenance helpers
    tests/
    results/
      paper/               # Curated evidence
      archive/             # Superseded evidence with provenance
      scratch/             # Ignored exploratory runs
  docs/                    # Durable design and usage notes
  plans/                   # Current research/implementation plans
  reviews/                 # Private research reviews when needed
  presentation/            # Talk sources and selected supporting assets
```

This is a role map, not a required Python architecture. An importable `src/`
package, a root package, MATLAB `src/`, C++ source/build tree, or a monorepo
subproject may own the equivalent roles. Keep one documented home for each role;
do not add `codes/` beside an existing package merely to match the example.
Similarly, retain established `plan/`, `codes/plans/`, `theory/`, or `proofs/`
when these already own the relevant records.

### 3.3 Other project types

- Publication projects keep working manuscript sources in their declared paper
  directory and immutable deliveries under an established release/archive tree.
  Review material stays outside upload packages.
- Public code projects include source, tests, examples, dependencies, license,
  and attribution. They normally exclude manuscripts and local result dumps;
  explicitly released data belongs in a separately documented artifact.
- Exploratory projects may contain only a focused prototype and research note.
  A monorepo gives each subproject its own path map without creating nested Git
  repositories automatically.
- Literature and personal projects use their category contracts instead of a
  scientific manuscript/code template.

### 3.4 Authority, mirrors, and build output

Declare one editable authority for each artifact role and research line. When
research and submission manuscripts coexist, name their different roles and
the direction of updates. A copied TeX/PDF, presentation figure, or arXiv bundle
is a mirror or derived delivery unless explicitly designated otherwise.

Record the source revision and regeneration/export command for mirrors. Update
working sources first, then regenerate mirrors deliberately. Keep frozen
submissions and published snapshots immutable; create a new identified snapshot
for corrections.

Use the documented build directory and entry point. New LaTeX workflows should
write intermediates to an ignored `build/` directory. Legacy in-place build
commands remain valid if intermediates are ignored. PDFs intentionally tracked
as deliverables and bibliography files required by source bundles are explicit
exceptions; a blanket extension rule must not remove them.

## 4. Naming

Use English ASCII names for new files and folders, with lowercase `snake_case`
for ordinary project files. Preserve recognized metadata names (`AGENTS.md`,
`README.md`, `REPORT.md`, `LICENSE`, `CITATION.cff`), project names, language
syntax, third-party filenames, and documented compatibility names.
Avoid spaces, Windows-reserved names, trailing dots/spaces, and paths that
differ only by case. Keep paths short enough for the project's supported tools.

| Item | New default | Existing exceptions |
|---|---|---|
| Python module | `solver_name.py`, `run_benchmark.py` | Preserve public imports and registry keys |
| Python test | `test_component.py` | Follow the language's test framework |
| Main manuscript | `{project}_main.tex` | Keep a declared versioned or submission entry |
| Shared TeX / references | `{project}_shared.tex` / `{project}_refs.bib` | Keep existing include paths |
| Figure / table | `performance_profile.pdf` / `summary.csv` | Preserve immutable released names |
| Dated note | `YYYY-MM-DD_topic.md` | Keep existing indexed notes |
| New run directory | `YYYYMMDDTHHMMSSZ_experiment_name/` | Retain existing timestamp/version conventions |
| Frozen snapshot | `YYYY-MM-DD_venue_stage/` inside the declared archive/release tree | Preserve established release IDs |

Use UTC for new timestamped run IDs and include the timezone in metadata.
Established `YYYYMMDD_HHMMSS` or version-based names are not renamed retroactively.
Use a fresh unique run ID when an output path already exists.

Do not use `final`, `final2`, `new`, `old`, or `latest` as the only version
identity. Descriptive algorithm variants may coexist when they have different
scientific meaning; numbered filenames are not a replacement for Git history.
An experiment's evidence status comes from its protocol/report, not an underscore
prefix or the name of its driver directory.

## 5. Version Management

| Object | Version authority | Rule |
|---|---|---|
| Working source and ordinary edits | Git commit history | Keep stable names; make focused commits |
| Software release | Project release metadata and `vMAJOR.MINOR.PATCH` tags when applicable | Follow the public API contract |
| Manuscript revision | Declared current entry and existing version ledger/README | Identify one current target per manuscript line |
| Formal experiment | Run ID, source revision, configuration, raw data, report | Preserve raw data; identify derived analysis revisions |
| Submitted/uploaded snapshot | Immutable release ID, manifest, source commit, hashes | New snapshot for each changed delivery |

Existing `v{major}_{minor}` manuscript names and solver variants remain supported.
Do not create a new numbered copy for every edit. Update the current-entry index
when deliberately starting a new revision; record what was superseded and why.
Keep earlier copies as historical artifacts until a provenance-preserving
migration, or use Git to retrieve versions that were never separate artifacts.

Use new working branches such as `codex/describe-change` when a branch is needed;
do not rename existing branches to conform. Keep software release tags separate
from paper milestones. Optional annotated paper tags can use
`paper/YYYY-MM-DD-venue-prepared` or `paper/YYYY-MM-DD-venue-submitted`.
Apply a submitted/published label only when supported by the actual record.
Never retarget an existing release tag or rewrite shared history during cleanup.

An existing `VERSION_MAP.md` or equivalent ledger remains authoritative. Add a
ledger only when multiple manuscript lines, mirrors, or frozen releases require
one; do not create redundant version documents for a small project.

## 6. Evidence, Data, and Generated Artifacts

### 6.1 Result status and storage

| Status | Default storage | Git/release handling |
|---|---|---|
| Curated formal evidence | Declared paper result tree | Track suitable raw data, configs, summaries, and reports in the authorized repository |
| Superseded formal evidence | Declared result archive | Preserve provenance; identify superseding runs |
| Exploratory / smoke output | Scratch tree or documented equivalent | Ignored by default; no unqualified paper claims |
| Manuscript assets | Declared paper figures/tables | Track selected assets with regeneration lineage |
| Temporary plots/builds/caches | Results scratch, build, cache, or tmp | Ignore and regenerate |
| Large/private/restricted source data | Declared data store or trusted local storage | Record access method and hashes; do not publish implicitly |

Extensions alone do not decide tracking. A CSV can be private or disposable; a
PDF can be a required paper asset. Curated result figures may be retained when a
frozen evidence package requires them. Public code-only repositories retain
their stricter project-specific result exclusions.

Keep raw outputs unchanged. A new run gets a new directory; a new analysis
records its input hashes and output location without overwriting frozen results.
Do not discard failures, select favorable seeds after seeing outcomes, or edit
data to match the paper narrative.

### 6.2 Formal run record

Each formal experiment has a `REPORT.md` or an equivalent indexed report plus
machine-readable metadata where the pipeline supports it. Record:

- research question, protocol, evidence status, and supported claim scope;
- code commit and whether the source tree was dirty; preserve a patch or hashed
  source snapshot if needed to reproduce the exact executed code;
- environment/dependency versions, solver versions, relevant hardware and threads;
- full command and working directory, configurations, problem set and dimensions;
- seeds and their selection/pairing policy, budgets and stopping rules;
- evaluation accounting, failures, exclusions, resumes, and deviations;
- raw data locations/checksums and the analysis/plotting commands;
- findings, limitations, and which manuscript assets use the result.

Project freeze gates may require a clean source tree or stricter metadata.
Recording a dirty state alone does not satisfy exact source reproducibility.
Promotion of scratch results requires a reproducibility and claim-scope check;
moving files into a paper folder does not perform that check.

### 6.3 Experimental choices and plotting

Choose metrics, seeds, sample counts, solver budgets, stopping rules, and thread
settings for the research question. No universal seed list, DFO budget,
single-thread rule, or normalized objective gap applies to all projects.
Document reference objective values, denominator handling, and failure treatment
when using objective-gap or performance-profile metrics.

Separate data collection from plotting. Regenerate figures from recorded input
data, configuration, and plotting code; CSV is not the only valid source format.
Use readable, color-accessible figures; prefer vector PDF for scientific plots
and PNG for previews. Follow the manuscript's actual publication requirements.

## 7. Code and Environment Defaults

- Prefer the existing architecture, helper APIs, and import mechanism.
- Python uses `pathlib.Path` for filesystem operations, four-space indentation,
  a 100-character line-length default, and NumPy-style public API docstrings.
  Existing formatter/linter configuration takes precedence for style.
- Organize imports as standard library, third-party, then local. Prefer a
  properly installed package over introducing another `sys.path` workaround.
- Use project-specific environments and language-appropriate dependency files.
  Preserve pinned experiment environments; packages may separately declare
  supported dependency ranges and a reproducibility lock/export.
- Do not claim identical numerical behavior across platforms without evidence.
  State supported runtimes, optional native dependencies, and numerical tolerances.
- Use UTF-8 and LF for new text/config files. Maintain `.gitattributes` with
  binary declarations and preserve existing Git LFS rules.

## 8. Git, Tracking, and Synchronization

Stage named task-related paths in each independent repository after inspecting
its status and diff. Avoid blanket workspace staging, automatic commit/push
recipes, branch switching, and unrelated renormalization. Preserve unrelated
staged and unstaged work.

Ignore virtual environments, caches, build intermediates, scratch results, and
temporary exports. Scope ignore rules to generated directories when possible;
do not globally ignore all PDF/PNG/SVG or CSV/JSON files. Check an exception with
`git check-ignore -v --no-index -- path` before assuming an artifact is tracked.
An ignore rule does not remove already tracked files or protect secrets.

Before an authorized push, inspect the actual remote and branch, remote
visibility, upstream state, and all outgoing commits. Verify manifest mappings
for repositories with separate research/release branches. A dirty checkout,
missing upstream, or mismatch needs a scoped resolution; never repair it by
silently staging other work, rewriting history, or changing visibility.

`sync_all.ps1` reads the manifest and never stages or commits. Its status/fetch/
pull/push actions are separate; use an action only when it fits the task. See
`SYNC_GUIDE.md` for command details. Setup uses `setup.ps1` and
`workspace-repos.json` rather than copied clone lists. Transfers of ignored
artifacts follow `TRANSFER_GUIDE.md`; skill backups follow `SKILLS_SYNC.md`.

## 9. Cleanup and Migration

1. Inspect repository status and map the existing authority, references, and
   generated/archived/private contents.
2. Record an old-to-new path map and reasons for an authorized move or rename.
   Preserve originals or a recoverable Git/source snapshot.
3. Update affected imports, build entries, configs, figure/data references,
   README links, and applicable instruction files together.
4. Run the narrowest checks that exercise those dependencies. Verify a frozen
   delivery from a clean extraction, not only the working tree.
5. Report changes and remaining gaps before the separately scheduled commit/push.

Do not combine a rules-only update with mass renames, deletion of old drafts,
movement of raw evidence, repository creation, or publication. Rules for new
artifacts take effect immediately; historical migration is a separate task.
