#!/usr/bin/env python3
"""Package the canonical Skill source for WorkBuddy and verify linked references."""

from __future__ import annotations

import hashlib
import re
import sys
import zipfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE = REPO_ROOT / "skills" / "student-portfolio-site"
DIST = REPO_ROOT / "dist"
ARCHIVE = DIST / "student-portfolio-site-workbuddy-skill.zip"
CHECKSUM = DIST / "SHA256SUMS"
MARKDOWN_LINK = re.compile(r"\]\((?![a-zA-Z][a-zA-Z0-9+.-]*:)([^)#]+\.md)(?:#[^)]+)?\)")


def verify_source() -> list[Path]:
    skill = SOURCE / "SKILL.md"
    if not skill.is_file():
        raise FileNotFoundError(f"Missing required source file: {skill}")

    files = [skill]
    references = SOURCE / "references"
    if references.is_dir():
        files.extend(sorted(path for path in references.rglob("*") if path.is_file()))

    linked = []
    for document in files:
        for match in MARKDOWN_LINK.finditer(document.read_text()):
            linked.append(document.parent / match.group(1))
    missing = [path for path in linked if not path.is_file()]
    if missing:
        raise FileNotFoundError("Missing Skill references: " + ", ".join(map(str, missing)))

    return files


def package(files: list[Path]) -> None:
    DIST.mkdir(exist_ok=True)
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, path.relative_to(SOURCE).as_posix())

    digest = hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()
    CHECKSUM.write_text(f"{digest}  {ARCHIVE.name}\n")


def verify_archive(files: list[Path]) -> None:
    expected = {path.relative_to(SOURCE).as_posix() for path in files}
    with zipfile.ZipFile(ARCHIVE) as archive:
        actual = set(archive.namelist())
        if actual != expected:
            raise RuntimeError(f"Archive entries do not match source: expected {expected}, got {actual}")
        if archive.testzip() is not None:
            raise RuntimeError("Archive integrity check failed")


def main() -> int:
    files = verify_source()
    package(files)
    verify_archive(files)
    print(f"Packaged {ARCHIVE}")
    print(f"Wrote {CHECKSUM}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
