#!/usr/bin/env python3
"""Print unresolved LaTeX citations and references from build logs.

Usage:
    python3 scripts/diagnose_latex.py

The script reads build/paper.log and build/paper.blg if they exist and prints the
exact citation or reference keys that LaTeX/BibTeX could not resolve.
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = REPO_ROOT / "build"
LOG_FILES = [BUILD_DIR / "paper.log", BUILD_DIR / "paper.blg"]
AUX_FILE = BUILD_DIR / "paper.aux"

PATTERNS = {
    "undefined_citations": [
        re.compile(r"Citation `([^']+)' on page .* undefined"),
        re.compile(r"Warning--I didn't find a database entry for ['\"]([^'\"]+)['\"]"),
    ],
    "undefined_references": [
        re.compile(r"Reference `([^']+)' on page .* undefined"),
    ],
}


def collect_matches(text: str, patterns: list[re.Pattern[str]]) -> list[str]:
    values: set[str] = set()
    for pattern in patterns:
        values.update(match.group(1) for match in pattern.finditer(text))
    return sorted(values)


def main() -> None:
    existing_logs = [path for path in LOG_FILES if path.exists()]
    if not existing_logs:
        print("No build/paper.log or build/paper.blg file found. Run the LaTeX build first.")
        return

    combined = "\n".join(path.read_text(encoding="utf-8", errors="replace") for path in existing_logs)
    citations = collect_matches(combined, PATTERNS["undefined_citations"])
    references = collect_matches(combined, PATTERNS["undefined_references"])

    # The first LaTeX pass necessarily reports citations/references as undefined
    # before BibTeX and later passes resolve them. Filter those transient warnings
    # against the final .aux file so the diagnostic reflects the completed build.
    if AUX_FILE.exists():
        aux = AUX_FILE.read_text(encoding="utf-8", errors="replace")
        resolved_citations = set(re.findall(r"^\\bibcite\{([^}]+)\}", aux, re.MULTILINE))
        resolved_references = set(re.findall(r"^\\newlabel\{([^}]+)\}", aux, re.MULTILINE))
        citations = [key for key in citations if key not in resolved_citations]
        references = [key for key in references if key not in resolved_references]

    if citations:
        print("Undefined citation keys:")
        for key in citations:
            print(f"  - {key}")
    else:
        print("No undefined citation keys found in LaTeX/BibTeX logs.")

    if references:
        print("\nUndefined LaTeX references:")
        for key in references:
            print(f"  - {key}")
    else:
        print("No undefined LaTeX references found in paper.log.")


if __name__ == "__main__":
    main()
