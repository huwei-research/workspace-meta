#!/usr/bin/env python3
"""Heuristic manuscript checks for mathematical writing.

This script flags common issues. It does not prove correctness and should be
used together with a human or model-based mathematical audit.
"""

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


def add_regex_issues(issues: list[Issue], text: str, pattern: str, kind: str, message: str, flags: int = 0) -> None:
    for m in re.finditer(pattern, text, flags):
        issues.append(Issue(line_number(text, m.start()), kind, message))


def check_text(text: str) -> list[Issue]:
    issues: list[Issue] = []

    checks = [
        (r"\[(citation needed|verification needed|TODO|FIXME)\]", "unresolved-marker", "Unresolved marker remains."),
        (r"\b(don't|can't|won't|isn't|aren't|doesn't|didn't|it's)\b", "contraction", "Avoid contractions in formal writing; check its/it's."),
        (r"\bwe have that\b", "wording", "Prefer 'we have ...' over 'we have that ...'."),
        (r"\bfor\s+\\forall\b", "quantifier", "Do not write 'for for all'."),
        (r"(\\neq|!=)\s*[^\n.;,]*(\\neq|!=)", "nontransitive-neq", "Do not chain non-transitive inequality; state pairwise distinctness explicitly."),
        (r"\bIf\b[^.\n]{40,},[^.\n]{40,},", "long-if", "Long if-clause may obscure hypothesis and conclusion; consider adding 'then' or splitting."),
        (r"\b(any)\b", "ambiguous-any", "Check whether 'any' should be 'each', 'every', or 'some'."),
        (r"\bwhere we define\b|\bwhere .* is defined as\b", "late-where-definition", "Define important terms before use; avoid lazy 'where' definitions."),
        (r"\bThis\s+(raises|shows|implies|gives|means|suggests|proves)\b", "naked-this", "Qualify 'This' with a noun or rewrite to remove ambiguity."),
        (r"\bThere (is|are)\b|\bIt (is|can be)\b", "weak-opening", "Check whether a stronger subject-verb opening is possible."),
        (r"\bIt can be seen\b|\bIt is easy to see\b", "weak-evidence-phrase", "Name the table, theorem, or argument that shows the claim."),
        (r"\bcompletely failed\b|\binevitably require\b|\bvery accurate\b|\bclearly efficient\b", "inflated-wording", "Replace vague or redundant intensifiers by precise evidence."),
        (r"\b(first|novel|state-of-the-art|outperform|significantly|robust|efficient)\b", "evidence-bearing-word", "Check that this claim is supported by proof, experiment, citation, or limitation language."),
        (r"\bnot\b[^.\n]{0,60}\bwithout\b", "negative-without", "Consider rewriting a negative-without construction positively."),
        (r"\bMatlab\b", "matlab-capitalization", "Use 'MATLAB'."),
        (r"\bloose\b", "possible-confused-word", "Check whether 'lose' is intended."),
        (r"\bsupercede\b", "spelling", "Use 'supersede'."),
        (r"\bprincipal of mathematical induction\b", "terminology", "Use 'principle of mathematical induction'."),
        (r"\bfinite solutions\b|\binfinite solutions\b", "terminology", "Use 'finitely many' or 'infinitely many' solutions."),
        (r"\bdoes not exists\b|\bis not exist\b", "verb-form", "Use 'does not exist'."),
        (r"\bequals to\b", "word-form", "Use 'equals' or 'is equal to'."),
    ]
    for pattern, kind, message in checks:
        add_regex_issues(issues, text, pattern, kind, message, flags=re.IGNORECASE)

    # Sentence starts with a bare TeX symbol or citation.
    for m in re.finditer(r"(^|[.!?]\s+)(\$[^$]+\$|\\\([^)]*\\\)|\\cite\{|\[[0-9,\s]+\])\s+[A-Za-z]", text):
        issues.append(Issue(line_number(text, m.start(2)), "bare-symbol-or-citation-start", "Avoid starting a sentence with a bare symbol or citation."))

    # Lines beginning with implication arrows.
    add_regex_issues(issues, text, r"^\s*(\\Rightarrow|\\implies|=>)", "orphan-arrow", "An implication arrow should not begin a line without a clear antecedent.", flags=re.MULTILINE)

    # Big inline fractions.
    for m in re.finditer(r"\$([^$]{30,})\$", text):
        if "\\frac" in m.group(1) or "\\sum" in m.group(1) or "\\int" in m.group(1):
            issues.append(Issue(line_number(text, m.start()), "big-inline-math", "Consider displaying large inline mathematics."))

    # Display equations without nearby punctuation.
    for m in re.finditer(r"\\\[(.*?)\\\]", text, flags=re.DOTALL):
        body = m.group(1).strip()
        if body and body[-1] not in ".,;:":
            issues.append(Issue(line_number(text, m.start()), "display-punctuation", "Displayed equation may need punctuation as part of the sentence."))

    return sorted(issues, key=lambda x: (x.line, x.kind, x.message))


def main() -> int:
    parser = argparse.ArgumentParser(description="Heuristic mathematical writing checks.")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()

    if not args.path.exists():
        print(f"File not found: {args.path}")
        return 2

    text = args.path.read_text(encoding="utf-8", errors="replace")
    issues = check_text(text)

    if not issues:
        print("No heuristic manuscript issues found.")
        return 0

    print(f"Found {len(issues)} heuristic manuscript issue(s):")
    for issue in issues:
        print(f"{args.path}:{issue.line}: {issue.kind}: {issue.message}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
