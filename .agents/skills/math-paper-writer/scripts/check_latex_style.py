#!/usr/bin/env python3
"""Heuristic LaTeX style checks for mathematical manuscripts."""

from __future__ import annotations

import argparse
import re
from pathlib import Path
from dataclasses import dataclass


@dataclass
class Issue:
    line: int
    kind: str
    message: str


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def check_latex(text: str) -> list[Issue]:
    issues: list[Issue] = []
    patterns = [
        (r"\$\$", "display-math", "Avoid $$...$$ in LaTeX manuscripts; use \\[...\\] or an equation environment."),
        (r"\\begin\{eqnarray\}", "eqnarray", "Avoid eqnarray; use align or aligned."),
        (r"\\label\{(?!((sec|subsec|thm|lem|prop|cor|def|ass|alg|eq|fig|tab|app):))", "label-prefix", "Use descriptive label prefixes such as thm:, lem:, eq:, fig:, tab:."),
        (r"\\ref\{[^}]+\}", "raw-ref", "Check whether \\Cref, \\autoref, or an explicit noun improves readability."),
        (r"\\begin\{theorem\}\s*\\label", "theorem-label-order", "Consider placing theorem label after theorem heading if house style requires it."),
        (r"paper\d+\.tex|final_final|new_revised|submission_new", "filename-versioning", "Avoid filename-based version control; use Git."),
        (r"\\vspace\{[-0-9.]+", "manual-spacing", "Manual vertical spacing may hide structural or float problems."),
    ]
    for pattern, kind, message in patterns:
        for m in re.finditer(pattern, text, flags=re.IGNORECASE):
            issues.append(Issue(line_number(text, m.start()), kind, message))

    # Long inline math.
    for m in re.finditer(r"\$([^$]{80,})\$", text):
        issues.append(Issue(line_number(text, m.start()), "long-inline-math", "Long inline math should probably be displayed."))

    return sorted(issues, key=lambda x: (x.line, x.kind))


def main() -> int:
    parser = argparse.ArgumentParser(description="Heuristic LaTeX style checks.")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()

    if not args.path.exists():
        print(f"File not found: {args.path}")
        return 2

    text = args.path.read_text(encoding="utf-8", errors="replace")
    issues = check_latex(text)
    if not issues:
        print("No heuristic LaTeX style issues found.")
        return 0

    print(f"Found {len(issues)} heuristic LaTeX style issue(s):")
    for issue in issues:
        print(f"{args.path}:{issue.line}: {issue.kind}: {issue.message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
