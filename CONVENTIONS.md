# Project Conventions

This document defines the naming, formatting, structural, and workflow conventions for all
research projects under the `huwei-research` GitHub Organization and the local workspace
`2026Projects/`. Every new project and every modification must follow these rules.

---

## 1. Workspace and Organization Structure

### 1.1 GitHub Organization

All repositories live under **`github.com/huwei-research/`**. Repositories are classified
into five categories using GitHub Topics:

| Category | Topic Label | Visibility | Purpose |
|----------|-------------|-----------|---------|
| Research | `research` | Private | Active projects with code + paper together |
| Publish | `publish` | Private | Papers of submitted/published projects |
| Public | `public` | Public | Open-source code releases |
| Experimental | `experimental` | Private | Exploratory projects in early stages |
| Personal | `personal` | Private | Non-research files (resume, etc.) |

### 1.2 Local Directory Layout

```
2026Projects/
├── CONVENTIONS.md
├── .cursor/
│   └── rules/project-conventions.mdc
├── Research/
│   ├── BUPTR/
│   ├── MATRO/
│   ├── STARTRO/
│   ├── RITRO/
│   ├── MemOTRO/
│   ├── BARN/
│   └── RSSM/
├── Publish/
│   ├── DisGRem-paper/
│   └── ArXiv/
├── Public/
│   └── DisGRem/
├── Experimental/
│   ├── QuasiNewton/
│   └── SelfCorrecting/
└── Personal/
    └── Weihu-resume/
```

Each subfolder is an independent Git repository. The category directories (`Research/`, etc.)
are NOT Git repositories themselves.

### 1.3 Repository Naming

| Rule | Example |
|------|---------|
| Research projects: uppercase acronym | `BUPTR`, `MATRO`, `STARTRO` |
| Compound names: PascalCase | `MemOTRO`, `SelfCorrecting`, `QuasiNewton` |
| Paper-only repos: `{Project}-paper` | `DisGRem-paper` |
| ArXiv bundle: `ArXiv` | `ArXiv` |
| Repo name = local folder name = GitHub name | Always consistent across all three |
| No `-private` suffix | Visibility controlled by GitHub settings |

### 1.4 Repository Description Format

```
[Category] One-sentence description of the project
```

Examples:
- `[Research] Bayesian Uncertainty-Penalized Trust-Region method for DFO`
- `[Publish] DisGRem paper sources, SIOPT submission, and poster materials`
- `[Public] DisGRem: Distributed Gradient-Regularized Newton Method (code)`

---

## 2. Project Structure

### 2.1 Research Project Template

Every Research or Experimental project must contain:

```
PROJECT/
├── README.md
├── .gitignore
├── .gitattributes
├── paper/
│   ├── {project}_{journal}_submission.tex
│   ├── {project}_{journal}_shared.tex
│   ├── figures/
│   │   ├── main/
│   │   └── supplementary/
│   └── archive/
├── codes/
│   ├── README.md
│   ├── requirements.txt
│   ├── core/
│   ├── solvers/
│   │   ├── __init__.py
│   │   ├── CATALOG.md
│   │   └── {algorithm}/
│   ├── problems/
│   ├── experiments/
│   │   ├── benchmarks/
│   │   ├── ablation/
│   │   ├── analysis/
│   │   ├── research/
│   │   └── paper/
│   ├── tests/
│   ├── utils/
│   ├── scripts/
│   ├── results/
│   │   ├── paper/
│   │   ├── archive/
│   │   └── scratch/       (gitignored)
│   └── plans/
└── presentation/           (optional)
```

### 2.2 Publish Project Template

```
DisGRem-paper/
├── README.md
├── .gitignore
├── .gitattributes
├── paper/
│   ├── disgrem_siopt_submission.tex
│   ├── disgrem_siopt_shared.tex
│   ├── cover_letter_siopt.tex
│   ├── figures/main/
│   └── archive/
├── arxiv/
│   └── disgrem22/
└── posters/
    └── moa_disgrem_poster/
```

### 2.3 Public Code Release Template

```
DisGRem/
├── README.md
├── LICENSE                  (MIT)
├── .gitignore
├── .gitattributes
├── codes/
│   ├── README.md
│   ├── requirements.txt
│   ├── core/
│   ├── solvers/
│   ├── problems/
│   ├── experiments/
│   ├── utils/
│   ├── scripts/
│   └── results/
└── docs/                    (optional, for public API docs)
```

---

### 2.4 Agent Instructions

Every independent repository must have a project-local `AGENTS.md`.

The file must specify:

- project identity and current research status;
- key manuscript, code, experiment, result, and counterpart-repository paths;
- project-specific mathematical assumptions, notation, and claim boundaries;
- the narrowest useful verification commands;
- which result directories are paper-grade, archival, or scratch;
- git boundaries for the repository.

For new projects, start from `.agents/templates/project_agents_template.md` in the
workspace-meta repository and specialize it before the first substantive code,
paper, or experiment commit.

---

## 3. File Naming Conventions

### 3.1 Python Files

| Category | Pattern | Example |
|----------|---------|---------|
| Solver (main) | `{algorithm}.py` | `bup_tr.py`, `disgrem.py` |
| Solver (version) | `{algorithm}_v{N}.py` | `bup_newuoa_v7.py` |
| External wrapper | `{library}_wrapper.py` | `pdfo_wrapper.py` |
| Test file | `test_{module}.py` | `test_bup_tr.py` |
| Experiment (formal) | `{descriptive_name}.py` | `standard_benchmark.py` |
| Experiment (exploratory) | `_{descriptive_name}.py` | `_test_v7_quick.py` |
| Helper script | `{verb}_{noun}.py` | `merge_results.py`, `replot.py` |
| Paper experiment | `exp_paper_{section_id}_{name}.py` | `exp_paper_s41_oracle.py` |

### 3.2 LaTeX Files

| Category | Pattern | Example |
|----------|---------|---------|
| Submission | `{project}_{journal}_submission.tex` | `disgrem_siopt_submission.tex` |
| Working draft | `{project}_paper_v{major}_{minor}.tex` | `startro_paper_v2_1.tex` |
| Shared macros | `{project}_{journal}_shared.tex` | `disgrem_siopt_shared.tex` |
| Supplementary | `{project}_supplementary.tex` | `buptr_supplementary.tex` |
| Cover letter | `cover_letter_{journal}.tex` | `cover_letter_siopt.tex` |
| Style files | Keep original name | `siamart171218.cls` |
| Archived versions | Move to `paper/archive/` | `paper/archive/disgrem_paper_v12_0.tex` |

### 3.3 Figure Files

| Category | Location | Pattern | Example |
|----------|----------|---------|---------|
| Paper figures (main) | `paper/figures/main/` | `{descriptive_name}.pdf` | `perf_profiles_panel.pdf` |
| Paper figures (supp) | `paper/figures/supplementary/` | `{name}.pdf` | `ada_m_trajectory.pdf` |
| Result figures | `codes/results/{exp}/` | `{name}.{pdf,png}` | `convergence_grid.pdf` |
| Debug/scratch | `codes/results/scratch/` | anything | (gitignored) |

Rules:
- All lowercase `snake_case`, no spaces, no Chinese characters
- PDF for publication quality, PNG for quick previews
- Paper figures ARE tracked by Git; result figures are NOT

### 3.4 Results and Data Files

| Category | Pattern | Example |
|----------|---------|---------|
| Formal results dir | `codes/results/paper/{experiment_name}/` | `results/paper/s44_main/` |
| Timestamped scratch | `codes/results/scratch/{YYYYMMDD_HHMMSS}_{name}/` | `results/scratch/20260526_183732_benchmark/` |
| Archive | `codes/results/archive/` | Old formal results moved here |
| Raw CSV | `{descriptive_name}.csv` | `main_results.csv` |
| Summary/report | `REPORT.md` | Required in every formal result dir |

---

## 4. Version Conventions

### 4.1 Paper Versions

- File naming: `v{major}_{minor}` in filename
- Major version: structural changes, new sections, major rewrites
- Minor version: polishing, minor additions, typo fixes
- Upon journal submission: rename to `{project}_{journal}_submission.tex`
- Previous submissions: move to `paper/archive/` with `_old` suffix

### 4.2 Code Versions

- Use Git tags: `v{major}.{minor}.{patch}` (e.g., `v1.0.0`)
- Tag at every paper submission milestone
- Tag format: `v1.0.0-siopt-submission`, `v1.1.0-revision`
- Solver versions in filenames: `{algorithm}_v{N}.py` for experimental variants

### 4.3 Experiment Reproducibility

- Every formal experiment REPORT.md must record:
  - Git commit hash at time of run
  - Python version and key package versions
  - Command used to run
  - Hardware info (if runtime-sensitive)

---

## 5. Python Code Style

### 5.1 General

- **PEP 8** compliance
- **Line length**: 100 characters max
- **Indentation**: 4 spaces (no tabs)
- **Trailing whitespace**: none
- **File ending**: single newline at EOF

### 5.2 Naming

| Entity | Convention | Example |
|--------|-----------|---------|
| Module | `lower_snake_case` | `gp_utils.py` |
| Class | `PascalCase` | `BUPTRSolver` |
| Function / method | `lower_snake_case` | `solve_subproblem()` |
| Variable | `lower_snake_case` | `trust_radius` |
| Constant | `UPPER_SNAKE_CASE` | `MAX_ITERATIONS` |
| Private | Leading underscore | `_fit_gp()` |

### 5.3 Imports

Three blocks separated by blank lines: stdlib / third-party / local.

```python
import sys
from pathlib import Path

import numpy as np
import scipy.linalg as la

from core.base import Solver, OptimizationProblem
from solvers.bup_tr import BUPTRSolver
```

### 5.4 Docstrings

NumPy-style for all public functions and classes:

```python
def solve(self, problem, x0, options=None):
    """Solve an unconstrained optimization problem.

    Parameters
    ----------
    problem : OptimizationProblem
        The problem to solve.
    x0 : np.ndarray
        Initial point.
    options : dict, optional
        Solver options.

    Returns
    -------
    OptimizationResult
        The result containing x_best, f_best, nfev, etc.
    """
```

### 5.5 Comments

- Only explain non-obvious intent, trade-offs, or constraints.
- Do NOT narrate what the code does line-by-line.
- Use `# TODO:` for planned changes; `# HACK:` for workarounds; `# NOTE:` for important context.

---

## 6. Cross-Platform Compatibility

### 6.1 Path Handling

- Always use `pathlib.Path`. Never hardcode `\` or `/`.
- Canonical sys.path setup:

```python
import sys
from pathlib import Path

_CODES_ROOT = Path(__file__).resolve().parents[N]  # N = depth from codes/
if str(_CODES_ROOT) not in sys.path:
    sys.path.insert(0, str(_CODES_ROOT))
```

| File location | N |
|---------------|---|
| `codes/*.py` | 0 |
| `codes/experiments/*.py` | 1 |
| `codes/experiments/benchmarks/*.py` | 2 |
| `codes/tests/*.py` | 1 |

- Create directories with `Path.mkdir(parents=True, exist_ok=True)`.
- Pass `str(path)` to libraries (matplotlib, pandas).

### 6.2 Line Endings

Every project root must have `.gitattributes`:

```gitattributes
* text=auto eol=lf

*.pdf  binary
*.png  binary
*.jpg  binary
*.gif  binary
*.xlsx binary
*.xls  binary
*.gz   binary
*.zip  binary
*.7z   binary

*.sh   text eol=lf
```

### 6.3 Environment Isolation

- Each project: `codes/.venv/` (gitignored)
- `requirements.txt` pins exact versions: `numpy==1.26.4`
- Setup: `python -m venv .venv && pip install -r requirements.txt`

---

## 7. Git Conventions

### 7.1 Standard `.gitignore`

```gitignore
# Python
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/
.pytest_cache/

# Virtual environments
.venv*/
venv/
env/

# IDE
.idea/
.vscode/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
desktop.ini

# LaTeX build artifacts
*.aux
*.out
*.thm
*.bbl
*.blg
*.fls
*.fdb_latexmk
*.synctex.gz
*.log
texput.log

# Generated figures (regenerate locally)
codes/results/scratch/
*.eps
*.svg

# Exception: paper figures ARE tracked
!paper/**/*.pdf
!paper/**/*.png
```

### 7.2 What IS Tracked

`.py`, `.csv`, `.json`, `.xls`, `.xlsx`, `.md`, `.tex`, `.txt`, `.sh`, `.cls`, `.bst`,
`.bib`, `requirements.txt`, `LICENSE`, `paper/**/*.pdf`, `paper/**/*.png`

### 7.3 What is NOT Tracked

LaTeX build artifacts, `__pycache__/`, `.venv*/`, IDE files, OS files,
`codes/results/scratch/`, generated result figures

### 7.4 Commit Messages

- Imperative mood: "Add benchmark results", not "Added..."
- First line: concise summary (<=72 chars)
- Optional body after blank line

### 7.5 Tags

- Tag at milestones: `v1.0.0-siopt-submission`, `v1.0.1-revision`
- Use annotated tags: `git tag -a v1.0.0 -m "SIOPT submission"`

---

## 8. Numerical Experiment Conventions

### 8.1 Experiment Script Structure

```python
#!/usr/bin/env python
"""One-line title.

Extended description: what is being tested, why, and key hypotheses.

Usage:
    python experiments/benchmarks/xxx.py [--option value]
"""

import sys
from pathlib import Path

_CODES_ROOT = Path(__file__).resolve().parents[2]
if str(_CODES_ROOT) not in sys.path:
    sys.path.insert(0, str(_CODES_ROOT))

import numpy as np

from problems.xxx import get_problem
from solvers import get_solver

SOLVERS = ["solver_a", "solver_b"]
PROBLEMS = {"rosenbrock": [2, 10], "sphere": [5, 10]}
SEEDS = [42, 123, 7, 256, 999]
OPTS = {"max_eval": 3000, "rhobeg": 1.0, "rhoend": 1e-8}

RESULTS_DIR = _CODES_ROOT / "results" / "paper" / "experiment_name"


def main():
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    # ... run experiments ...
    df.to_csv(RESULTS_DIR / "raw_results.csv", index=False)


if __name__ == "__main__":
    main()
```

### 8.2 Reproducibility

- Fixed seeds: `SEEDS = [42, 123, 7, 256, 999]`
- Single-thread BLAS at script top
- Standard options: `{"max_eval": 3000, "rhobeg": 1.0, "rhoend": 1e-8}`

### 8.3 Success Metric

More-Wild relative error: `f_rel(x) = (f(x) - f*) / (f(x0) - f* + eps)`

Standard tolerances: `tau in {1e-1, 1e-3, 1e-5, 1e-7}`

### 8.4 Result Organization

```
codes/results/
├── paper/                   (formal, tracked by Git)
│   └── {experiment_name}/
│       ├── REPORT.md        (required)
│       ├── raw_results.csv
│       └── summary.csv
├── archive/                 (old formal results, tracked)
│   └── REPORT.md
└── scratch/                 (gitignored, temporary)
    └── {YYYYMMDD_HHMMSS}_{name}/
```

### 8.5 Plotting

- Style: SIAM journal, seaborn `whitegrid`, colorblind-friendly
- Format: PDF (publication) + PNG (preview)
- Font: LaTeX-compatible when available
- All plotting code must be re-runnable from CSV data alone
- Batch regeneration: `python scripts/replot.py`

### 8.6 Experiment Categories

| Category | Path | Purpose |
|----------|------|---------|
| Benchmarks | `experiments/benchmarks/` | Formal comparisons for paper |
| Ablation | `experiments/ablation/` | Component isolation |
| Analysis | `experiments/analysis/` | Deep dives, sensitivity |
| Research | `experiments/research/` | Exploratory, prefix with `_` |
| Paper | `experiments/paper/` | Final paper experiments |

---

## 9. Solver Version Management

- Main solver: `{algorithm}.py` (production)
- Experimental: `{algorithm}_v{N}.py` (alongside main)
- `solvers/CATALOG.md` documents every algorithm and version
- When versioned solver becomes production: update main file and CATALOG

---

## 10. License

| Category | License | File |
|----------|---------|------|
| Public | MIT | `LICENSE` at repo root |
| Research | None (private) | No LICENSE file |
| Publish | None (private) | No LICENSE file |
| Experimental | None (private) | No LICENSE file |
| Personal | None (private) | No LICENSE file |

---

## 11. README Template

Every project README follows this structure:

```markdown
# PROJECT_NAME

> One-sentence description.

**Status**: [Active Research | Submitted | Published | Exploratory | Archived]
**Category**: [Research | Publish | Public | Experimental | Personal]
**Paper**: [Link or "In preparation"]

## Abstract

2-3 sentences summarizing the project.

## Repository Structure

(Directory tree)

## Quick Start

(Setup and run instructions)

## Citation

(BibTeX entry, if applicable)

## License

(MIT for Public; omit for Private repos)
```

---

## 12. Syncing on a New Machine

### 12.1 Clone All Repositories

```bash
ORG=huwei-research
mkdir -p Research Publish Public Experimental Personal

# Research
for repo in BUPTR MATRO STARTRO RITRO MemOTRO BARN RSSM; do
  git clone https://github.com/$ORG/$repo.git Research/$repo
done

# Publish
git clone https://github.com/$ORG/DisGRem-paper.git Publish/DisGRem-paper
git clone https://github.com/$ORG/ArXiv.git Publish/ArXiv

# Public
git clone https://github.com/$ORG/DisGRem.git Public/DisGRem

# Experimental
for repo in QuasiNewton SelfCorrecting; do
  git clone https://github.com/$ORG/$repo.git Experimental/$repo
done

# Personal
git clone https://github.com/$ORG/Weihu-resume.git Personal/Weihu-resume
```

### 12.2 Environment Setup

```bash
for project in Research/*/codes Publish/*/codes Public/*/codes Experimental/*/codes; do
  if [ -f "$project/requirements.txt" ]; then
    cd "$project"
    python -m venv .venv
    source .venv/bin/activate  # or .venv\Scripts\activate on Windows
    pip install -r requirements.txt
    deactivate
    cd -
  fi
done
```

### 12.3 Figure Regeneration

After clone, regenerate figures by running each project's replot script:

```bash
cd Research/BUPTR/codes && python scripts/replot_from_csv.py
cd Public/DisGRem/codes && python scripts/replot.py
```

### 12.4 Proxy Configuration (China)

```bash
git config --global http.proxy  socks5h://127.0.0.1:7897
git config --global https.proxy socks5h://127.0.0.1:7897
```

### 12.5 Daily Workflow

```bash
# Pull all repos
for dir in Research/* Publish/* Public/* Experimental/* Personal/*; do
  git -C "$dir" pull --ff-only 2>/dev/null
done

# After changes
git add -A && git commit -m "Description" && git push
```
