#!/usr/bin/env python3
"""Check a claim-evidence ledger for missing or risky entries."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


RISKY_STATUS_RE = re.compile(
    r"\b("
    r"needs?|missing|overclaim|distorted|unverifiable|unverified|unsupported|"
    r"pending|open|todo|tbd|citation needed|verification needed|proof needed|experiment needed"
    r")\b",
    re.IGNORECASE,
)

PLACEHOLDER_RE = re.compile(r"^\s*(?:-|--|n/a|todo|tbd|open|pending)?\s*$", re.IGNORECASE)


@dataclass
class Issue:
    row: int
    claim_id: str
    kind: str
    message: str


def split_row(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return []
    return [cell.strip().replace("\\|", "|") for cell in stripped.strip("|").split("|")]


def is_separator(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def find_table(lines: list[str]) -> tuple[list[str], list[tuple[int, list[str]]]]:
    header: list[str] = []
    rows: list[tuple[int, list[str]]] = []
    collecting = False
    for index, line in enumerate(lines, start=1):
        cells = split_row(line)
        if not cells:
            if collecting and rows:
                break
            continue
        lowered = [cell.lower() for cell in cells]
        if not collecting and "claim" in lowered and ("status" in lowered or "verdict" in lowered):
            header = lowered
            collecting = True
            continue
        if collecting and is_separator(cells):
            continue
        if collecting and len(cells) >= 3:
            rows.append((index, cells))
    return header, rows


def cell(cells: list[str], header: list[str], names: list[str]) -> str:
    for name in names:
        if name in header:
            pos = header.index(name)
            if pos < len(cells):
                return cells[pos].strip()
    return ""


def check_ledger(text: str) -> list[Issue]:
    lines = text.splitlines()
    header, rows = find_table(lines)
    issues: list[Issue] = []
    if not header:
        return [Issue(0, "", "missing-table", "No Markdown claim table with Claim and Status/Verdict columns found.")]

    for row_num, cells in rows:
        claim_id = cell(cells, header, ["id", "claim id"]) or f"row {row_num}"
        claim = cell(cells, header, ["claim"])
        evidence = cell(cells, header, ["evidence", "support", "source evidence checked"])
        status = cell(cells, header, ["status", "verdict"])
        severity = cell(cells, header, ["severity"])

        if PLACEHOLDER_RE.match(claim):
            issues.append(Issue(row_num, claim_id, "missing-claim", "Claim text is empty or placeholder."))
        if PLACEHOLDER_RE.match(evidence):
            issues.append(Issue(row_num, claim_id, "missing-evidence", "Evidence cell is empty or placeholder."))
        if PLACEHOLDER_RE.match(status):
            issues.append(Issue(row_num, claim_id, "missing-status", "Status/verdict cell is empty or placeholder."))
        elif RISKY_STATUS_RE.search(status):
            issues.append(Issue(row_num, claim_id, "risky-status", f"Status still requires attention: {status}"))
        if severity.lower() in {"blocking", "major"} and RISKY_STATUS_RE.search(status):
            issues.append(Issue(row_num, claim_id, "publication-gate", "Blocking/major unresolved claim should be fixed before final submission."))

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description="Check claim-evidence ledger completeness.")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()

    if not args.path.exists():
        print(f"File not found: {args.path}")
        return 2

    text = args.path.read_text(encoding="utf-8", errors="replace")
    issues = check_ledger(text)

    if not issues:
        print("No claim-evidence ledger issues found.")
        return 0

    print(f"Found {len(issues)} claim-evidence issue(s):")
    for issue in issues:
        location = f"{args.path}:{issue.row}" if issue.row else str(args.path)
        label = f"{issue.claim_id}: " if issue.claim_id else ""
        print(f"{location}: {issue.kind}: {label}{issue.message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
