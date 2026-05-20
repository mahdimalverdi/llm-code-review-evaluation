#!/usr/bin/env python3
"""Refresh BibTeX entries from DOI metadata while preserving project notes.

The script reads ``references/references.bib``, fetches publisher/Crossref BibTeX
for entries with non-arXiv DOIs, preserves the existing BibTeX keys and project
notes, and optionally runs ``bibtex-tidy`` if it is available through ``npx``.

Usage:
    python3 scripts/refresh_bib_from_doi.py
    python3 scripts/refresh_bib_from_doi.py --no-tidy
    python3 scripts/refresh_bib_from_doi.py --bib-file references/references.bib

Notes:
    - arXiv DOI entries such as ``10.48550/arXiv...`` are intentionally skipped
      so their ``eprint`` and ``archivePrefix`` fields are not lost.
    - Existing ``note`` fields are preserved when the DOI response does not
      provide a note. This keeps values such as ``Project ID: P52`` or
      ``Methodological ID: M08`` in the bibliography.
    - A ``.bak`` file is written before modifications.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import time
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BIB_PATH = REPO_ROOT / "references" / "references.bib"
ENTRY_PATTERN = re.compile(
    r"(?P<prefix>\n?%[^\n]*\n)?"
    r"(?P<entry>@[a-zA-Z]+\s*\{\s*(?P<key>[^,\s]+)\s*,.*?\n\})",
    re.DOTALL,
)
DOI_PATTERN = re.compile(r"\bdoi\s*=\s*[\{\"]([^}\"]+)[}\"]", re.IGNORECASE)
NOTE_PATTERN = re.compile(r"\bnote\s*=\s*[\{\"]([^}\"]+)[}\"]", re.IGNORECASE)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--bib-file",
        type=Path,
        default=DEFAULT_BIB_PATH,
        help="Path to the BibTeX file to refresh.",
    )
    parser.add_argument(
        "--no-tidy",
        action="store_true",
        help="Skip bibtex-tidy formatting after DOI refresh.",
    )
    parser.add_argument(
        "--request-delay-seconds",
        type=float,
        default=0.3,
        help="Delay between DOI requests to avoid being too aggressive.",
    )
    return parser.parse_args()


def normalize_doi(raw: str) -> str:
    doi = raw.strip()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        doi = doi.removeprefix(prefix)
    return doi.strip()


def should_skip_doi(doi: str) -> bool:
    return doi.lower().startswith("10.48550/arxiv")


def run_command(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def fetch_bibtex_from_doi(doi: str) -> str | None:
    result = run_command([
        "curl",
        "-fsSL",
        "-LH",
        "Accept: application/x-bibtex",
        f"https://doi.org/{doi}",
    ])
    if result.returncode != 0:
        print(f"SKIP {doi}: curl failed: {result.stderr.strip()}")
        return None

    bibtex = result.stdout.strip()
    if not bibtex.startswith("@"):
        print(f"SKIP {doi}: DOI response is not BibTeX")
        return None
    return bibtex


def replace_key(entry: str, key: str) -> str:
    return re.sub(
        r"^@[a-zA-Z]+\s*\{\s*[^,\s]+",
        lambda match: match.group(0).split("{")[0] + "{" + key,
        entry,
        count=1,
    )


def has_field(entry: str, field: str) -> bool:
    return re.search(rf"\b{re.escape(field)}\s*=", entry, flags=re.IGNORECASE) is not None


def add_field_before_closing_brace(entry: str, field: str, value: str) -> str:
    stripped = entry.rstrip()
    if not stripped.endswith("}"):
        return entry
    return stripped[:-1].rstrip() + f",\n  {field} = {{{value}}}\n}}"


def ensure_project_note(entry: str, original_note: str | None) -> str:
    if not original_note or has_field(entry, "note"):
        return entry
    return add_field_before_closing_brace(entry, "note", original_note)


def ensure_url(entry: str, doi: str) -> str:
    if has_field(entry, "url"):
        return entry
    return add_field_before_closing_brace(entry, "url", f"https://doi.org/{doi}")


def refresh_entries(text: str, request_delay_seconds: float) -> tuple[str, int, int]:
    updated_count = 0
    skipped_arxiv_count = 0

    def update_entry(match: re.Match[str]) -> str:
        nonlocal updated_count, skipped_arxiv_count

        prefix = match.group("prefix") or ""
        original_entry = match.group("entry")
        original_key = match.group("key").strip()

        doi_match = DOI_PATTERN.search(original_entry)
        if not doi_match:
            return match.group(0)

        doi = normalize_doi(doi_match.group(1))
        if should_skip_doi(doi):
            skipped_arxiv_count += 1
            return match.group(0)

        note_match = NOTE_PATTERN.search(original_entry)
        original_note = note_match.group(1).strip() if note_match else None

        fetched = fetch_bibtex_from_doi(doi)
        if fetched is None:
            return match.group(0)

        updated = replace_key(fetched, original_key)
        updated = ensure_url(updated, doi)
        updated = ensure_project_note(updated, original_note)

        updated_count += 1
        print(f"UPDATED {original_key} from DOI {doi}")
        time.sleep(request_delay_seconds)
        return prefix + updated

    return ENTRY_PATTERN.sub(update_entry, text), updated_count, skipped_arxiv_count


def run_bibtex_tidy(bib_file: Path) -> None:
    if shutil.which("npx") is None:
        print("SKIP bibtex-tidy: npx is not available")
        return

    command = [
        "npx",
        "--yes",
        "bibtex-tidy",
        str(bib_file),
        "--modify",
        "--curly",
        "--numeric",
        "--align=13",
        "--sort=key",
    ]
    result = run_command(command)
    if result.returncode != 0:
        print(result.stdout)
        print(result.stderr)
        raise SystemExit("bibtex-tidy failed")
    if result.stdout.strip():
        print(result.stdout.strip())


def main() -> None:
    args = parse_args()
    bib_file = args.bib_file
    if not bib_file.is_absolute():
        bib_file = REPO_ROOT / bib_file

    if not bib_file.exists():
        raise FileNotFoundError(f"Missing bibliography file: {bib_file}")

    backup_file = bib_file.with_suffix(bib_file.suffix + ".bak")
    shutil.copy2(bib_file, backup_file)
    print(f"Wrote backup: {backup_file.relative_to(REPO_ROOT)}")

    text = bib_file.read_text(encoding="utf-8")
    updated_text, updated_count, skipped_arxiv_count = refresh_entries(
        text,
        args.request_delay_seconds,
    )
    bib_file.write_text(updated_text, encoding="utf-8")

    print(f"Updated DOI-backed entries: {updated_count}")
    print(f"Skipped arXiv DOI entries: {skipped_arxiv_count}")

    if args.no_tidy:
        print("Skipped bibtex-tidy because --no-tidy was passed")
    else:
        run_bibtex_tidy(bib_file)

    print("Next steps:")
    print("  git diff references/references.bib")
    print("  ./scripts/build_pdf.sh")


if __name__ == "__main__":
    main()
