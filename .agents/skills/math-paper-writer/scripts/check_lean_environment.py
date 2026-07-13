#!/usr/bin/env python3
"""Check a Lean/Lake project environment for manuscript-grade use.

This script combines three checks:

1. Lean source trust-boundary hygiene via ``check_lean_project.py``.
2. Lake manifest package installation and pinned revision matching.
3. Optional local toolchain/build checks without pretending a build ran.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from check_lean_project import Issue, check_project  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


@dataclass
class EnvIssue:
    severity: str
    area: str
    message: str


def resolve_command(cmd: list[str]) -> list[str]:
    if not cmd:
        return cmd
    name = cmd[0]
    if name not in {"elan", "lake", "lean", "leanc", "leanmake"}:
        return cmd
    suffix = ".exe" if sys.platform.startswith("win") else ""
    local = Path.home() / ".elan" / "bin" / f"{name}{suffix}"
    if local.exists():
        return [str(local), *cmd[1:]]
    return cmd


def run_capture(cmd: list[str], *, cwd: Path | None = None, timeout: int = 60) -> tuple[int, str]:
    cmd = resolve_command(cmd)
    try:
        proc = subprocess.run(
            cmd,
            cwd=cwd,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            timeout=timeout,
        )
    except FileNotFoundError:
        return 127, f"Command not found: {cmd[0]}"
    except subprocess.TimeoutExpired as exc:
        output = ((exc.stdout or "") + (exc.stderr or "")).strip()
        return 124, output or f"Command timed out after {timeout} seconds: {' '.join(cmd)}"
    return proc.returncode, (proc.stdout + proc.stderr).strip()


def find_default_registry(start: Path) -> Path | None:
    for base in [start, *start.parents]:
        candidate = base / "Experimental" / "lean-libraries" / "lean-library-registry.yaml"
        if candidate.exists():
            return candidate
    return None


def read_library_path_from_registry(registry: Path, library: str) -> Path | None:
    current_library: str | None = None
    in_libraries = False
    for raw_line in registry.read_text(encoding="utf-8", errors="replace").splitlines():
        stripped = raw_line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if raw_line == "libraries:":
            in_libraries = True
            current_library = None
            continue
        if not in_libraries:
            continue
        if raw_line.startswith("  ") and not raw_line.startswith("    ") and stripped.endswith(":"):
            current_library = stripped[:-1]
            continue
        if current_library == library and raw_line.startswith("    path:"):
            value = raw_line.split(":", 1)[1].strip().strip('"').strip("'")
            return Path(value)
    return None


def project_root(path: Path) -> Path:
    return path if path.is_dir() else path.parent


def read_toolchain(root: Path) -> str | None:
    path = root / "lean-toolchain"
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8", errors="replace").strip()


def toolchain_variants(toolchain: str) -> set[str]:
    variants = {toolchain}
    if toolchain.startswith("leanprover/lean4:"):
        version = toolchain.split(":", 1)[1]
        variants.add(version)
        variants.add(f"leanprover--lean4---{version}")
    return variants


def is_toolchain_installed(toolchain: str) -> tuple[bool, str]:
    code, output = run_capture(["elan", "toolchain", "list"], timeout=20)
    if code != 0:
        return False, output
    variants = toolchain_variants(toolchain)
    installed = any(variant in output for variant in variants)
    return installed, output


def load_manifest(root: Path) -> tuple[dict[str, object] | None, EnvIssue | None]:
    manifest = root / "lake-manifest.json"
    if not manifest.exists():
        return None, EnvIssue("note", "manifest", "No lake-manifest.json found.")
    try:
        data = json.loads(manifest.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return None, EnvIssue("blocking", "manifest", f"Invalid lake-manifest.json: {exc}")
    return data, None


def check_manifest_packages(root: Path, manifest: dict[str, object]) -> list[EnvIssue]:
    issues: list[EnvIssue] = []
    packages_dir = Path(str(manifest.get("packagesDir", ".lake/packages")))
    package_records = manifest.get("packages", [])
    if not isinstance(package_records, list):
        return [EnvIssue("blocking", "manifest", "Manifest field 'packages' is not a list.")]

    for record in package_records:
        if not isinstance(record, dict):
            issues.append(EnvIssue("blocking", "manifest", "Manifest package record is not an object."))
            continue
        name = str(record.get("name", "")).strip()
        rev = str(record.get("rev", "")).strip()
        if not name or not rev:
            issues.append(EnvIssue("blocking", "manifest", f"Package record missing name or rev: {record!r}"))
            continue

        package_path = root / packages_dir / name
        if not (package_path / ".git").exists():
            issues.append(EnvIssue("blocking", "manifest", f"Missing Lake package checkout: {packages_dir / name}"))
            continue

        code, output = run_capture(["git", "-C", str(package_path), "rev-parse", "HEAD"], timeout=20)
        if code != 0:
            issues.append(EnvIssue("blocking", "manifest", f"Could not read git HEAD for {name}: {output}"))
            continue
        head = output.splitlines()[-1].strip()
        if head != rev:
            issues.append(
                EnvIssue(
                    "blocking",
                    "manifest",
                    f"Package {name} at {head}, expected pinned revision {rev}.",
                )
            )
    return issues


def print_lean_issues(issues: list[Issue], notes: list[str]) -> None:
    for note in notes:
        print(f"NOTE trust-boundary: {note}")
    if not issues:
        print("Trust boundary: no Lean hygiene issues found.")
        return
    print(f"Trust boundary: found {len(issues)} issue(s).")
    for issue in issues:
        print(f"{issue.path}:{issue.line}: {issue.severity}: {issue.kind}: {issue.message}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a Lean/Lake environment for formal-verification claims.")
    parser.add_argument("path", type=Path, nargs="?", help="Lean file or Lake project directory.")
    parser.add_argument(
        "--library",
        help="Resolve a library path from a lean-library-registry.yaml file, for example: optlib.",
    )
    parser.add_argument(
        "--library-registry",
        type=Path,
        default=None,
        help="Path to lean-library-registry.yaml. If omitted, search upward for Experimental/lean-libraries.",
    )
    parser.add_argument("--allow-sorry", action="store_true", help="Do not fail on sorry/admit placeholders.")
    parser.add_argument("--fail-on-warning", action="store_true", help="Treat axioms/constants/unsafe as failures.")
    parser.add_argument(
        "--require-toolchain-installed",
        action="store_true",
        help="Fail if lean-toolchain is not installed in elan.",
    )
    parser.add_argument("--run-build", action="store_true", help="Run lake build after environment checks pass.")
    parser.add_argument(
        "--build-target",
        action="append",
        default=[],
        help="Lake build target to check; repeat for multiple targets. Defaults to the package default target.",
    )
    parser.add_argument(
        "--show-build-output",
        action="store_true",
        help="Print Lake build output even when the build succeeds.",
    )
    parser.add_argument("--build-timeout", type=int, default=900, help="Seconds before lake build times out.")
    args = parser.parse_args()

    if args.path is not None:
        target = args.path.resolve()
    elif args.library:
        registry = args.library_registry.resolve() if args.library_registry else find_default_registry(Path.cwd().resolve())
        if registry is None:
            print("No lean-library-registry.yaml found. Provide a path or --library-registry.")
            return 2
        library_path = read_library_path_from_registry(registry, args.library)
        if library_path is None:
            print(f"Library not found in registry {registry}: {args.library}")
            return 2
        target = library_path.resolve()
        print(f"Library registry: {registry}")
        print(f"Selected library: {args.library}")
    else:
        parser.error("provide a Lean project path or --library")

    if not target.exists():
        print(f"Path not found: {target}")
        return 2

    root = project_root(target)
    print("Lean environment report")
    print(f"Project: {root}")

    lean_issues, lean_notes = check_project(target)
    print_lean_issues(lean_issues, lean_notes)

    env_issues: list[EnvIssue] = []
    toolchain = read_toolchain(root)
    if toolchain is None:
        env_issues.append(EnvIssue("warning", "toolchain", "No lean-toolchain file found."))
        toolchain_installed = False
    else:
        print(f"Toolchain: {toolchain}")
        toolchain_installed, toolchain_output = is_toolchain_installed(toolchain)
        if toolchain_installed:
            print("Toolchain installed: yes")
        else:
            message = f"Toolchain not installed in elan: {toolchain}"
            severity = "blocking" if args.require_toolchain_installed or args.run_build else "warning"
            env_issues.append(EnvIssue(severity, "toolchain", message))
            if toolchain_output:
                print("Elan toolchains:")
                print(toolchain_output)

    lakefile = root / "lakefile.lean"
    lakefile_toml = root / "lakefile.toml"
    if lakefile.exists() or lakefile_toml.exists():
        print("Lake project file: present")
    else:
        env_issues.append(EnvIssue("warning", "lake", "No lakefile.lean or lakefile.toml found."))

    manifest, manifest_issue = load_manifest(root)
    if manifest_issue is not None:
        env_issues.append(manifest_issue)
    elif manifest is not None:
        packages = manifest.get("packages", [])
        package_count = len(packages) if isinstance(packages, list) else "unknown"
        print(f"Lake manifest: present ({package_count} package(s))")
        manifest_issues = check_manifest_packages(root, manifest)
        env_issues.extend(manifest_issues)
        if not manifest_issues:
            print("Lake manifest packages: all pinned revisions match.")

    blocking_lean = [issue for issue in lean_issues if issue.severity == "blocking"]
    warning_lean = [issue for issue in lean_issues if issue.severity == "warning"]
    blocking_env = [issue for issue in env_issues if issue.severity == "blocking"]
    warning_env = [issue for issue in env_issues if issue.severity == "warning"]
    note_env = [issue for issue in env_issues if issue.severity == "note"]

    for issue in note_env + warning_env + blocking_env:
        print(f"{issue.severity.upper()} {issue.area}: {issue.message}")

    should_fail = False
    if blocking_lean and not args.allow_sorry:
        should_fail = True
    if warning_lean and args.fail_on_warning:
        should_fail = True
    if blocking_env:
        should_fail = True
    if warning_env and args.fail_on_warning:
        should_fail = True

    if args.run_build:
        if should_fail:
            print("Build: skipped because blocking checks failed.")
        elif not toolchain_installed:
            print("Build: skipped because the required toolchain is not installed.")
            should_fail = True
        else:
            build_cmd = ["lake", "build", *args.build_target]
            code, output = run_capture(build_cmd, cwd=root, timeout=args.build_timeout)
            print(f"Build command: {' '.join(build_cmd)}")
            if output and (code != 0 or args.show_build_output):
                print(output)
            elif output:
                line_count = len(output.splitlines())
                print(f"Build output: suppressed {line_count} line(s) from successful build.")
            if code != 0:
                print(f"Build: failed with exit code {code}.")
                should_fail = True
            else:
                print("Build: passed.")
    else:
        print("Build: not run.")

    return 1 if should_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
