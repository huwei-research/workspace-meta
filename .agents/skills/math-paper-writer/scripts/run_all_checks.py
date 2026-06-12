#!/usr/bin/env python3
"""Run all heuristic checks for the Math Paper Writer skill."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def run(cmd: list[str]) -> int:
    print("\n$ " + " ".join(cmd))
    proc = subprocess.run(cmd, text=True)
    return proc.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description="Run heuristic manuscript checks.")
    parser.add_argument("manuscript", type=Path)
    parser.add_argument("--bib", type=Path, default=None)
    args = parser.parse_args()

    here = Path(__file__).resolve().parent
    status = 0
    status |= run([sys.executable, str(here / "check_math_manuscript.py"), str(args.manuscript)])
    status |= run([sys.executable, str(here / "check_latex_style.py"), str(args.manuscript)])
    if args.bib is not None:
        status |= run([sys.executable, str(here / "check_bib_consistency.py"), str(args.bib)])
    return 1 if status else 0


if __name__ == "__main__":
    raise SystemExit(main())
