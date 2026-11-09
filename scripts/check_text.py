#!/usr/bin/env python3
"""Check text: the writing rules of Unique Domains.

Fails when a file written by hand in this repository carries a character or a word the project's writing rules ban:
the em dash, and the internal name of the scanner (say "scanner"). The snapshot, the generated files and the recorded
fixtures are the API's own published text and are checked by the API's repository, so they are left out here.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".venv", "venv", "dist", "build", "__pycache__", ".pytest_cache", ".ruff_cache", ".mypy_cache"}
SKIP_PATHS = [ROOT / "openapi", ROOT / "tests" / "fixtures" / "recorded", ROOT / "src" / "uniquedomains" / "_generated"]
# The generated tables carry the document's summaries.
SKIP_FILES = {ROOT / "src" / "uniquedomains" / name for name in ("_operations.py", "_listings.py", "_namespaces.py")}
TEXT = re.compile(r"\.(py|toml|cfg|ini|json|md|ya?ml|txt|sh)$|^(LICENSE|\.gitignore)$")

# Built from parts so this file does not trip its own check.
BANNED = [
    (re.compile(chr(0x2014)), "an em dash"),
    (re.compile(r"\b" + "dae" + "mon", re.IGNORECASE), 'the internal name of the scanner (write "scanner")'),
]


def files() -> list[Path]:
    found = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if any(path.is_relative_to(skip) for skip in SKIP_PATHS) or path in SKIP_FILES:
            continue
        if TEXT.search(path.name):
            found.append(path)
    return found


def main() -> int:
    problems = []
    for path in files():
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            for pattern, label in BANNED:
                if pattern.search(line):
                    problems.append(f"{path.relative_to(ROOT)}:{number}: {label}")
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    print("The text rules hold.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
