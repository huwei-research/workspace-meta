#!/usr/bin/env python3
"""Package the Math Paper Writer skill using manifest.txt."""

from __future__ import annotations

import argparse
import zipfile
from pathlib import Path


def read_manifest(root: Path) -> list[Path]:
    manifest = root / "manifest.txt"
    entries: list[Path] = []
    for line in manifest.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            entries.append(Path(stripped))
    return entries


def package(root: Path, output: Path, *, dry_run: bool = False) -> list[str]:
    root = root.resolve()
    entries = read_manifest(root)
    missing = [entry.as_posix() for entry in entries if not (root / entry).is_file()]
    if missing:
        raise FileNotFoundError("Missing manifest entries: " + ", ".join(missing))

    archive_names = [f"{root.name}/{entry.as_posix()}" for entry in entries]
    if dry_run:
        return archive_names

    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for entry, archive_name in zip(entries, archive_names):
            zf.write(root / entry, archive_name)
    return archive_names


def main() -> int:
    parser = argparse.ArgumentParser(description="Package math-paper-writer for release.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path, default=None)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = args.root.resolve()
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    output = args.output or root / "dist" / f"{root.name}-skill-v{version}.zip"
    archive_names = package(root, output, dry_run=args.dry_run)

    if args.dry_run:
        print(f"Would package {len(archive_names)} files.")
    else:
        print(f"Wrote {output}")
        print(f"Packaged {len(archive_names)} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
