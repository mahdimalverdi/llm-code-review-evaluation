#!/usr/bin/env python3
"""Build the manuscript PDF from Markdown sections.

This script performs the full LaTeX build sequence from a clean auxiliary state:

1. Generate build/paper.tex and build/references.bib.
2. Run pdflatex once to create paper.aux.
3. Run BibTeX from inside the build directory.
4. Run pdflatex twice more to resolve citations, references, and outlines.
5. Fail with useful diagnostics when unresolved citations or references remain.

Usage:
    python3 scripts/build_pdf.py
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = REPO_ROOT / "build"
PAPER_TEX = BUILD_DIR / "paper.tex"
PAPER_PDF = BUILD_DIR / "paper.pdf"
BUILD_LATEX_SCRIPT = REPO_ROOT / "scripts" / "build_latex.py"
DIAGNOSE_SCRIPT = REPO_ROOT / "scripts" / "diagnose_latex.py"
AUXILIARY_SUFFIXES = {
    ".aux",
    ".bbl",
    ".blg",
    ".brf",
    ".fdb_latexmk",
    ".fls",
    ".lof",
    ".log",
    ".lot",
    ".out",
    ".toc",
}

UNDEFINED_CITATION_PATTERNS = [
    re.compile(r"Citation `([^']+)' on page .* undefined"),
    re.compile(r"Warning--I didn't find a database entry for ['\"]([^'\"]+)['\"]"),
]
UNDEFINED_REFERENCE_PATTERNS = [
    re.compile(r"Reference `([^']+)' on page .* undefined"),
]


def run(command: list[str], *, cwd: Path | None = None, allow_failure: bool = False) -> subprocess.CompletedProcess[str]:
    print("$ " + " ".join(command))
    result = subprocess.run(
        command,
        cwd=cwd,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    print(result.stdout)
    if result.returncode != 0 and not allow_failure:
        raise subprocess.CalledProcessError(result.returncode, command, output=result.stdout)
    return result


def clean_auxiliary_files() -> None:
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    for path in BUILD_DIR.iterdir():
        if path.name == "paper.pdf":
            continue
        if path.suffix in AUXILIARY_SUFFIXES:
            path.unlink()


def extract_matches(text: str, patterns: list[re.Pattern[str]]) -> set[str]:
    matches: set[str] = set()
    for pattern in patterns:
        matches.update(match.group(1) for match in pattern.finditer(text))
    return matches


def log_text(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def unresolved_items() -> tuple[set[str], set[str]]:
    combined = "\n".join([
        log_text(BUILD_DIR / "paper.log"),
        log_text(BUILD_DIR / "paper.blg"),
    ])
    citations = extract_matches(combined, UNDEFINED_CITATION_PATTERNS)
    references = extract_matches(combined, UNDEFINED_REFERENCE_PATTERNS)
    # The first pdflatex pass necessarily emits transient undefined-citation
    # warnings before BibTeX has generated paper.bbl.  Filter those warnings
    # against the final auxiliary file, just as diagnose_latex.py does.
    aux = log_text(BUILD_DIR / "paper.aux")
    resolved_citations = set(re.findall(r"^\\bibcite\{([^}]+)\}", aux, re.MULTILINE))
    resolved_references = set(re.findall(r"^\\newlabel\{([^}]+)\}", aux, re.MULTILINE))
    citations -= resolved_citations
    references -= resolved_references
    return citations, references


def print_diagnostics() -> None:
    if DIAGNOSE_SCRIPT.exists():
        run([sys.executable, str(DIAGNOSE_SCRIPT)], cwd=REPO_ROOT, allow_failure=True)


def main() -> int:
    try:
        clean_auxiliary_files()
        run([sys.executable, str(BUILD_LATEX_SCRIPT)], cwd=REPO_ROOT)

        if not PAPER_TEX.exists():
            print(f"ERROR: {PAPER_TEX.relative_to(REPO_ROOT)} was not generated.")
            return 1

        if not (BUILD_DIR / "references.bib").exists():
            print("ERROR: build/references.bib was not copied. Run scripts/build_latex.py first.")
            return 1

        # The first post-BibTeX pass can return non-zero for transient auxiliary
        # file warnings (undefined citations/labels); the following pass is the
        # authoritative result after those files have been rewritten.
        run(["pdflatex", "-interaction=nonstopmode", "paper.tex"], cwd=BUILD_DIR, allow_failure=True)
        run(["bibtex", "paper"], cwd=BUILD_DIR)
        run(["pdflatex", "-interaction=nonstopmode", "paper.tex"], cwd=BUILD_DIR)
        run(["pdflatex", "-interaction=nonstopmode", "paper.tex"], cwd=BUILD_DIR, allow_failure=True)

        citations, references = unresolved_items()
        final_log = log_text(BUILD_DIR / "paper.log")
        fatal_markers = ("Fatal error occurred", "Emergency stop")
        if any(marker in final_log for marker in fatal_markers) or not PAPER_PDF.exists():
            print("ERROR: final LaTeX pass did not produce a valid PDF.")
            print_diagnostics()
            return 1
        if citations or references:
            print("ERROR: unresolved citations or references remain.")
            print_diagnostics()
            return 1

        print(f"PDF written to {PAPER_PDF.relative_to(REPO_ROOT)}")
        return 0
    except subprocess.CalledProcessError as error:
        print(f"ERROR: command failed with exit code {error.returncode}: {' '.join(error.cmd)}")
        print_diagnostics()
        return error.returncode


if __name__ == "__main__":
    raise SystemExit(main())
