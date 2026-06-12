#!/usr/bin/env python3
"""Heuristic BibTeX consistency checks."""

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


def check_bib(text: str) -> list[Issue]:
    issues: list[Issue] = []

    keys: dict[str, int] = {}
    for m in re.finditer(r"@\w+\s*\{\s*([^,\s]+)", text):
        key = m.group(1)
        line = line_number(text, m.start())
        if key in keys:
            issues.append(Issue(line, "duplicate-key", f"Duplicate BibTeX key also appears on line {keys[key]}."))
        else:
            keys[key] = line

    for m in re.finditer(r"title\s*=\s*[\"{]([^\"}]*)[\"}]", text, flags=re.IGNORECASE):
        title = m.group(1)
        if re.search(r"\b(MATLAB|SIAM|IEEE|CPU|GPU|PDE|ODE|SVD|QR|Newton|Gauss|Laplacian)\b", title):
            # If braces are absent around uppercase acronyms/proper names, warn.
            raw = m.group(0)
            if "{{" not in raw and "}" not in title:
                issues.append(Issue(line_number(text, m.start()), "title-capitalization", "Check whether proper nouns or acronyms in title need braces."))

    required_fields = {
        "article": ["author", "title", "journal", "year"],
        "inproceedings": ["author", "title", "booktitle", "year"],
        "book": ["author", "title", "publisher", "year"],
    }
    for entry in re.finditer(r"@(\w+)\s*\{([^@]*)", text, flags=re.DOTALL):
        kind = entry.group(1).lower()
        body = entry.group(2)
        start_line = line_number(text, entry.start())
        if kind in required_fields:
            lower_body = body.lower()
            for field in required_fields[kind]:
                if not re.search(rf"\b{field}\s*=", lower_body):
                    issues.append(Issue(start_line, "missing-field", f"Entry of type {kind} may be missing field '{field}'."))

    for m in re.finditer(r"journal\s*=\s*[\"{]\s*(SIAM J\.|Siam|J\. of)\b", text, flags=re.IGNORECASE):
        issues.append(Issue(line_number(text, m.start()), "journal-abbreviation", "Check journal abbreviation against the target style."))

    return sorted(issues, key=lambda x: (x.line, x.kind))


def main() -> int:
    parser = argparse.ArgumentParser(description="Heuristic BibTeX consistency checks.")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()

    if not args.path.exists():
        print(f"File not found: {args.path}")
        return 2

    text = args.path.read_text(encoding="utf-8", errors="replace")
    issues = check_bib(text)
    if not issues:
        print("No heuristic BibTeX issues found.")
        return 0

    print(f"Found {len(issues)} heuristic BibTeX issue(s):")
    for issue in issues:
        print(f"{args.path}:{issue.line}: {issue.kind}: {issue.message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
