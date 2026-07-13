#!/usr/bin/env python3
"""Heuristic checks for Lean formalization artifacts.

This script does not invoke Lean. It scans Lean files for common trust-boundary
risks and reports whether the artifact is clean enough to support a formal
verification claim after an actual Lean build.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


BLOCKING_PATTERNS = [
    (re.compile(r"\bsorry\b"), "sorry", "Unresolved Lean proof placeholder."),
    (re.compile(r"\badmit\b"), "admit", "Unresolved Lean proof placeholder."),
]

WARNING_PATTERNS = [
    (re.compile(r"^\s*axiom\s+\w+", re.MULTILINE), "axiom", "New axiom changes the trust boundary."),
    (re.compile(r"^\s*constant\s+\w+", re.MULTILINE), "constant", "Unproved constant may change the trust boundary."),
    (re.compile(r"\bunsafe\b"), "unsafe", "Unsafe code requires manual trust-boundary review."),
]


@dataclass
class Issue:
    path: Path
    line: int
    severity: str
    kind: str
    message: str


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def lean_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path] if path.suffix == ".lean" else []
    return sorted(p for p in path.rglob("*.lean") if ".lake" not in p.parts)


def scan_file(path: Path, root: Path) -> list[Issue]:
    text = path.read_text(encoding="utf-8", errors="replace")
    issues: list[Issue] = []
    for pattern, kind, message in BLOCKING_PATTERNS:
        for match in pattern.finditer(text):
            issues.append(Issue(path.relative_to(root), line_number(text, match.start()), "blocking", kind, message))
    for pattern, kind, message in WARNING_PATTERNS:
        for match in pattern.finditer(text):
            issues.append(Issue(path.relative_to(root), line_number(text, match.start()), "warning", kind, message))
    return issues


def check_project(path: Path) -> tuple[list[Issue], list[str]]:
    root = path if path.is_dir() else path.parent
    files = lean_files(path)
    notes: list[str] = []
    if not files:
        notes.append("No Lean files found.")
    if path.is_dir():
        if not (path / "lean-toolchain").exists():
            notes.append("No lean-toolchain file found; record the Lean/mathlib version before claiming verification.")
        if not ((path / "lakefile.lean").exists() or (path / "lakefile.toml").exists()):
            notes.append("No Lake project file found; record the build command before claiming verification.")

    issues: list[Issue] = []
    for file_path in files:
        issues.extend(scan_file(file_path, root))
    return issues, notes


def main() -> int:
    parser = argparse.ArgumentParser(description="Check Lean formalization artifacts for trust-boundary risks.")
    parser.add_argument("path", type=Path)
    parser.add_argument("--allow-sorry", action="store_true", help="Do not fail on sorry/admit placeholders.")
    parser.add_argument("--fail-on-warning", action="store_true", help="Treat axioms/constants/unsafe as failures.")
    args = parser.parse_args()

    if not args.path.exists():
        print(f"Path not found: {args.path}")
        return 2

    issues, notes = check_project(args.path)
    blocking = [issue for issue in issues if issue.severity == "blocking"]
    warnings = [issue for issue in issues if issue.severity == "warning"]

    for note in notes:
        print(f"NOTE: {note}")

    if not issues:
        print("No Lean trust-boundary issues found.")
    else:
        print(f"Found {len(issues)} Lean trust-boundary issue(s):")
        for issue in issues:
            print(f"{issue.path}:{issue.line}: {issue.severity}: {issue.kind}: {issue.message}")

    if blocking and not args.allow_sorry:
        return 1
    if warnings and args.fail_on_warning:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
