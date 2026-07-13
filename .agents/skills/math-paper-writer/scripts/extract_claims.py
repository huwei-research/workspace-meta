#!/usr/bin/env python3
"""Extract likely manuscript claims into a Markdown ledger draft.

This is a heuristic triage script. It finds sentences that look like central
claims; it does not verify them.
"""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


CLAIM_RE = re.compile(
    r"\b("
    r"we\s+(prove|show|establish|derive|demonstrate|propose|introduce|obtain|provide|present|develop)|"
    r"this\s+(paper|work)\s+(proves|shows|establishes|derives|demonstrates|proposes|introduces|provides|presents|develops)|"
    r"to\s+our\s+knowledge|"
    r"first|novel|new|improve[sd]?|sharper|weaker\s+assumptions|"
    r"converges?|convergence|stationary\s+point|global\s+(minimum|minimizer|solution)|"
    r"rate|complexity|guarantee[sd]?|"
    r"outperform[s]?|superior|state-of-the-art|robust|scalable|efficient|significant"
    r")\b",
    re.IGNORECASE,
)


SECTION_RE = re.compile(r"\\(?:section|subsection|subsubsection)\*?\{([^}]*)\}")
ABSTRACT_BEGIN_RE = re.compile(r"\\begin\{abstract\}", re.IGNORECASE)
ABSTRACT_END_RE = re.compile(r"\\end\{abstract\}", re.IGNORECASE)


@dataclass
class Claim:
    claim_id: str
    line: int
    section: str
    text: str
    claim_type: str


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def strip_tex(text: str) -> str:
    text = re.sub(r"%.*", "", text)
    text = re.sub(r"\\cite[a-zA-Z*]*\{[^}]*\}", "[citation]", text)
    text = re.sub(r"\\ref\{[^}]*\}|\\eqref\{[^}]*\}", "[ref]", text)
    text = re.sub(r"\\[a-zA-Z]+\*?(?:\[[^\]]*\])?\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def sentence_spans(text: str) -> list[tuple[int, int, str]]:
    spans: list[tuple[int, int, str]] = []
    start = 0
    for match in re.finditer(r"(?<=[.!?])\s+(?=[A-Z\\])", text):
        end = match.start()
        raw = text[start:end].strip()
        if raw:
            spans.append((start, end, raw))
        start = match.end()
    raw = text[start:].strip()
    if raw:
        spans.append((start, len(text), raw))
    return spans


def section_at(text: str, index: int, in_abstract: bool) -> str:
    if in_abstract:
        return "abstract"
    section = "preamble"
    for match in SECTION_RE.finditer(text, 0, index):
        section = strip_tex(match.group(1)).lower() or "section"
    return section


def is_abstract(text: str, index: int) -> bool:
    begin = None
    for match in ABSTRACT_BEGIN_RE.finditer(text, 0, index + 1):
        begin = match.end()
    if begin is None:
        return False
    end = ABSTRACT_END_RE.search(text, begin)
    return end is None or index < end.start()


def infer_type(sentence: str) -> str:
    lower = sentence.lower()
    if any(
        word in lower
        for word in [
            "convergen",
            "converges",
            "stationary point",
            "global minimum",
            "global minimizer",
            "global solution",
            "rate",
            "complexity",
            "prove",
            "theorem",
            "lemma",
            "guarantee",
        ]
    ):
        return "mathematical"
    if any(word in lower for word in ["outperform", "state-of-the-art", "significant", "robust", "experiment"]):
        return "experimental"
    if any(word in lower for word in ["to our knowledge", "first", "novel", "new", "improve", "sharper", "weaker assumption"]):
        return "novelty"
    if any(word in lower for word in ["algorithm", "solver", "implementation", "oracle"]):
        return "algorithmic"
    return "claim"


def escape_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


def extract_claims(text: str, max_claims: int) -> list[Claim]:
    claims: list[Claim] = []
    for start, _end, sentence in sentence_spans(text):
        visible = strip_tex(sentence)
        if len(visible) < 25:
            continue
        if not CLAIM_RE.search(visible):
            continue
        in_abs = is_abstract(text, start)
        section = section_at(text, start, in_abs)
        if section not in {"abstract", "introduction", "intro", "conclusion", "discussion", "contributions", "results"}:
            if len(claims) >= max_claims:
                break
        claims.append(
            Claim(
                claim_id=f"C{len(claims) + 1}",
                line=line_number(text, start),
                section=section,
                text=visible,
                claim_type=infer_type(visible),
            )
        )
        if len(claims) >= max_claims:
            break
    return claims


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract likely manuscript claims as a Markdown table.")
    parser.add_argument("path", type=Path)
    parser.add_argument("--max-claims", type=int, default=80)
    args = parser.parse_args()

    if not args.path.exists():
        print(f"File not found: {args.path}")
        return 2

    text = args.path.read_text(encoding="utf-8", errors="replace")
    claims = extract_claims(text, args.max_claims)

    if not claims:
        print("No likely central claims found.")
        return 0

    print("| ID | Location | Claim | Type | Evidence | Status | Severity | Required fix |")
    print("| --- | --- | --- | --- | --- | --- | --- | --- |")
    for claim in claims:
        location = f"{claim.section}: line {claim.line}"
        print(
            "| "
            + " | ".join(
                [
                    claim.claim_id,
                    escape_cell(location),
                    escape_cell(claim.text),
                    claim.claim_type,
                    "",
                    "UNVERIFIABLE",
                    "major",
                    "Map to proof, citation, experiment, or limitation.",
                ]
            )
            + " |"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
