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
    parser.add_argument("--claim-ledger", type=Path, default=None)
    parser.add_argument("--lean-project", type=Path, default=None)
    parser.add_argument("--lean-library", default=None)
    parser.add_argument("--lean-require-toolchain", action="store_true")
    parser.add_argument("--lean-allow-sorry", action="store_true")
    parser.add_argument("--lean-build", action="store_true")
    parser.add_argument("--lean-build-target", action="append", default=[])
    args = parser.parse_args()

    here = Path(__file__).resolve().parent
    status = 0
    status |= run([sys.executable, str(here / "check_math_manuscript.py"), str(args.manuscript)])
    status |= run([sys.executable, str(here / "check_latex_style.py"), str(args.manuscript)])
    if args.bib is not None:
        status |= run([sys.executable, str(here / "check_bib_consistency.py"), str(args.bib)])
    if args.claim_ledger is not None:
        status |= run([sys.executable, str(here / "check_claim_evidence.py"), str(args.claim_ledger)])
    if args.lean_project is not None or args.lean_library is not None:
        cmd = [sys.executable, str(here / "check_lean_environment.py")]
        if args.lean_project is not None:
            cmd.append(str(args.lean_project))
        if args.lean_library is not None:
            cmd.extend(["--library", args.lean_library])
        if args.lean_allow_sorry:
            cmd.append("--allow-sorry")
        if args.lean_require_toolchain:
            cmd.append("--require-toolchain-installed")
        if args.lean_build:
            cmd.append("--run-build")
        for target in args.lean_build_target:
            cmd.extend(["--build-target", target])
        status |= run(cmd)
    return 1 if status else 0


if __name__ == "__main__":
    raise SystemExit(main())
