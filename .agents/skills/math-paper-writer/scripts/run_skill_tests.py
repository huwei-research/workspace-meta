#!/usr/bin/env python3
"""Self-contained release tests for the Math Paper Writer skill."""

from __future__ import annotations

import argparse
import py_compile
import re
import subprocess
import sys
import tempfile
from pathlib import Path


PUBLIC_CLEAN_PATTERNS = [
    "D:/xwechat",
    "C:/Users",
    "source_distillation",
    "source-distillation",
    "deep_read_sources",
    "check_source_distillation",
    "--source-ledger",
]


def run(cmd: list[str], *, cwd: Path, expect: int = 0) -> tuple[bool, str]:
    proc = subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)
    output = (proc.stdout + proc.stderr).strip()
    ok = proc.returncode == expect
    return ok, output


def check(condition: bool, message: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS {message}")
    else:
        print(f"FAIL {message}")
        failures.append(message)


def parse_frontmatter(skill_md: Path) -> dict[str, str]:
    text = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if not match:
        return {}
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def manifest_entries(root: Path) -> list[str]:
    manifest = root / "manifest.txt"
    return [
        line.strip()
        for line in manifest.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]


def check_manifest(root: Path, failures: list[str]) -> None:
    entries = manifest_entries(root)
    missing = [entry for entry in entries if not (root / entry).exists()]
    check(not missing, "manifest entries exist", failures)
    if missing:
        print("Missing manifest entries:")
        for entry in missing:
            print(f"  {entry}")

    unlisted = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = path.relative_to(root).as_posix()
        if "__pycache__" in path.parts:
            continue
        if rel not in entries:
            unlisted.append(rel)
    check(not unlisted, "manifest covers all package files", failures)
    if unlisted:
        print("Unlisted files:")
        for entry in sorted(unlisted):
            print(f"  {entry}")

    forbidden = [entry for entry in entries if "__pycache__" in entry or entry.endswith(".pyc")]
    check(not forbidden, "manifest excludes generated files", failures)


def check_frontmatter(root: Path, failures: list[str]) -> None:
    data = parse_frontmatter(root / "SKILL.md")
    check(data.get("name") == "math-paper-writer", "frontmatter name", failures)
    description = data.get("description", "")
    check(0 < len(description) <= 1024, "frontmatter description length", failures)
    extra_keys = set(data) - {"name", "description"}
    check(not extra_keys, "frontmatter has only required keys", failures)


def check_public_clean(root: Path, failures: list[str]) -> None:
    offenders: list[tuple[str, str]] = []
    for path in root.rglob("*"):
        if not path.is_file() or "__pycache__" in path.parts:
            continue
        if path.name == "run_skill_tests.py":
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        rel = path.relative_to(root).as_posix()
        for pattern in PUBLIC_CLEAN_PATTERNS:
            if pattern in text:
                offenders.append((rel, pattern))
    check(not offenders, "public-clean text scan", failures)
    if offenders:
        for rel, pattern in offenders:
            print(f"  {rel}: {pattern}")


def check_python_scripts(root: Path, failures: list[str]) -> None:
    scripts = sorted((root / "scripts").glob("*.py"))
    compile_failures = []
    for script in scripts:
        try:
            py_compile.compile(str(script), doraise=True)
        except py_compile.PyCompileError as exc:
            compile_failures.append(f"{script.name}: {exc.msg}")
    check(not compile_failures, "Python scripts compile", failures)
    if compile_failures:
        for failure in compile_failures:
            print(f"  {failure}")


def check_behavior(root: Path, failures: list[str]) -> None:
    ok, output = run(
        [sys.executable, "scripts/extract_claims.py", "evals/fixtures/dfo_overclaim.tex"],
        cwd=root,
    )
    check(ok and "UNVERIFIABLE" in output and "stationary point" in output, "claim extraction fixture", failures)

    ok, output = run(
        [sys.executable, "scripts/check_math_manuscript.py", "evals/fixtures/english_style.md"],
        cwd=root,
        expect=1,
    )
    check(ok and "naked-this" in output and "ambiguous-any" in output, "manuscript checker fixture", failures)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        good = tmp_path / "good-ledger.md"
        bad = tmp_path / "bad-ledger.md"
        good.write_text(
            "| ID | Claim | Evidence | Status | Severity |\n"
            "|---|---|---|---|---|\n"
            "| C1 | Theorem 1 proves convergence under A1. | Theorem 1 proof. | SUPPORTED | minor |\n",
            encoding="utf-8",
        )
        bad.write_text(
            "| ID | Claim | Evidence | Status | Severity |\n"
            "|---|---|---|---|---|\n"
            "| C1 | Novel improvement. |  | NEEDS_CITATION | major |\n",
            encoding="utf-8",
        )
        ok_good, _ = run([sys.executable, "scripts/check_claim_evidence.py", str(good)], cwd=root)
        ok_bad, bad_output = run([sys.executable, "scripts/check_claim_evidence.py", str(bad)], cwd=root, expect=1)
        check(ok_good and ok_bad and "missing-evidence" in bad_output, "claim ledger checker behavior", failures)

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        good_lean = tmp_path / "Good.lean"
        bad_lean = tmp_path / "Bad.lean"
        good_lean.write_text("theorem add_zero_nat (n : Nat) : n + 0 = n := by\n  simp\n", encoding="utf-8")
        bad_lean.write_text("axiom unchecked : False\n\ntheorem broken : 1 = 2 := by\n  sorry\n", encoding="utf-8")
        ok_good, good_output = run([sys.executable, "scripts/check_lean_project.py", str(good_lean)], cwd=root)
        ok_bad, bad_output = run([sys.executable, "scripts/check_lean_project.py", str(bad_lean)], cwd=root, expect=1)
        check(
            ok_good
            and "No Lean trust-boundary issues found" in good_output
            and ok_bad
            and "sorry" in bad_output
            and "axiom" in bad_output,
            "Lean artifact checker behavior",
            failures,
        )

    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        lean_project = tmp_path / "lean-project"
        lean_project.mkdir()
        (lean_project / "lean-toolchain").write_text("leanprover/lean4:v4.13.0\n", encoding="utf-8")
        (lean_project / "lakefile.lean").write_text(
            "import Lake\nopen Lake DSL\n\npackage Test where\n\n@[default_target]\nlean_lib Test where\n",
            encoding="utf-8",
        )
        (lean_project / "lake-manifest.json").write_text(
            '{"version":"1.1.0","packagesDir":".lake/packages","packages":[]}\n',
            encoding="utf-8",
        )
        (lean_project / "Test.lean").write_text("theorem test_true : True := by\n  trivial\n", encoding="utf-8")
        ok_env, env_output = run(
            [sys.executable, "scripts/check_lean_environment.py", str(lean_project)],
            cwd=root,
        )
        check(
            ok_env
            and "Lake manifest packages: all pinned revisions match" in env_output
            and "Build: not run" in env_output,
            "Lean environment checker behavior",
            failures,
        )

    ok, output = run([sys.executable, "scripts/run_all_checks.py", "--help"], cwd=root)
    check(
        ok and "--claim-ledger" in output and "--lean-project" in output and "--source-ledger" not in output,
        "unified runner CLI",
        failures,
    )

    ok, output = run([sys.executable, "scripts/package_skill.py", "--dry-run"], cwd=root)
    check(ok and "Would package" in output, "release package dry run", failures)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run release tests for math-paper-writer.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()

    root = args.root.resolve()
    failures: list[str] = []
    print(f"Testing {root}")

    check((root / "SKILL.md").exists(), "SKILL.md exists", failures)
    check((root / "agents" / "openai.yaml").exists(), "agents/openai.yaml exists", failures)
    check((root / "README.md").exists(), "README.md exists", failures)

    check_frontmatter(root, failures)
    check_manifest(root, failures)
    check_public_clean(root, failures)
    check_python_scripts(root, failures)
    check_behavior(root, failures)

    if failures:
        print("\nRelease tests failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("\nAll release tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
