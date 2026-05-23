#!/usr/bin/env python3

import argparse
import csv
import re
import sys
import time
import zipfile
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen


DEFAULT_SPREADSHEET_ID = "14tTs2nwIwS40JU-na5bbwBNgyPYkZv9IPXVPfbPUR1I"
PAPER_POOL_GID = "0"

MISSING_STATUSES = {
    "",
    "No Drive PDF yet",
    "Missing",
    "Not uploaded",
}


def sanitize_filename(value: str, max_length: int = 140) -> str:
    value = value.strip()
    value = re.sub(r"[^\w\s.\-()]+", "_", value, flags=re.UNICODE)
    value = re.sub(r"\s+", "_", value)
    value = re.sub(r"_+", "_", value)
    value = value.strip("._- ")

    if len(value) > max_length:
        value = value[:max_length].rstrip("._- ")

    return value or "paper"


def google_sheet_csv_url(spreadsheet_id: str, gid: str) -> str:
    return (
        f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export"
        f"?format=csv&gid={gid}"
    )


def read_csv_from_url(url: str) -> list[dict[str, str]]:
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(request, timeout=60) as response:
        content = response.read().decode("utf-8-sig")

    return list(csv.DictReader(content.splitlines()))


def normalize_pdf_url(row: dict[str, str]) -> str:
    pdf_url = row.get("PDF URL", "").strip()

    if pdf_url:
        return pdf_url

    arxiv_id = row.get("arXiv ID", "").strip()
    if arxiv_id:
        return f"https://arxiv.org/pdf/{arxiv_id}"

    source_url = row.get("Source URL", "").strip()
    if "arxiv.org/abs/" in source_url:
        return source_url.replace("/abs/", "/pdf/")

    return ""


def build_output_filename(row: dict[str, str]) -> str:
    existing_name = row.get("Drive PDF Filename", "").strip()
    if existing_name and existing_name.lower().endswith(".pdf"):
        return sanitize_filename(existing_name)

    paper_id = row.get("ID", "").strip()
    title = row.get("Title", "").strip()

    base_name = sanitize_filename(f"{paper_id}_{title}")
    if not base_name.lower().endswith(".pdf"):
        base_name += ".pdf"

    return base_name


def should_download(row: dict[str, str], include_all: bool) -> bool:
    if include_all:
        return True

    status = row.get("Drive PDF Status", "").strip()
    drive_url = row.get("Drive PDF URL", "").strip()

    if status in MISSING_STATUSES:
        return True

    if "No Drive PDF yet" in status:
        return True

    if "not uploaded" in status.lower():
        return True

    if not drive_url and status.lower() != "no drive pdf needed":
        return True

    return False


def download_file(url: str, output_path: Path, retries: int = 3) -> None:
    last_error = None

    for attempt in range(1, retries + 1):
        try:
            request = Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urlopen(request, timeout=90) as response:
                content_type = response.headers.get("Content-Type", "")
                data = response.read()

            if not data:
                raise RuntimeError("empty response")

            if b"%PDF" not in data[:2048] and "pdf" not in content_type.lower():
                raise RuntimeError(
                    f"response does not look like a PDF; content-type={content_type}"
                )

            output_path.write_bytes(data)
            return

        except (HTTPError, URLError, TimeoutError, RuntimeError) as error:
            last_error = error
            if attempt < retries:
                time.sleep(2 * attempt)

    raise RuntimeError(f"failed to download {url}: {last_error}")


def zip_directory(source_dir: Path, zip_path: Path) -> None:
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zip_file:
        for file_path in sorted(source_dir.glob("*.pdf")):
            zip_file.write(file_path, arcname=file_path.name)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--spreadsheet-id",
        default=DEFAULT_SPREADSHEET_ID,
        help="Google Spreadsheet ID",
    )
    parser.add_argument(
        "--gid",
        default=PAPER_POOL_GID,
        help="Sheet gid for Paper Pool",
    )
    parser.add_argument(
        "--output-dir",
        default="downloaded_pdfs",
        help="Directory for downloaded PDFs",
    )
    parser.add_argument(
        "--zip-path",
        default="missing_pdfs.zip",
        help="Output zip file path",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Download all rows instead of only missing Drive PDFs",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    csv_url = google_sheet_csv_url(args.spreadsheet_id, args.gid)
    rows = read_csv_from_url(csv_url)

    downloaded = []
    skipped = []
    failed = []

    for row in rows:
        paper_id = row.get("ID", "").strip()
        title = row.get("Title", "").strip()

        if not paper_id or not title:
            continue

        if not should_download(row, include_all=args.all):
            skipped.append((paper_id, "already available or not needed"))
            continue

        pdf_url = normalize_pdf_url(row)
        if not pdf_url:
            failed.append((paper_id, title, "no PDF URL / arXiv ID"))
            continue

        filename = build_output_filename(row)
        output_path = output_dir / filename

        if output_path.exists() and output_path.stat().st_size > 0:
            downloaded.append((paper_id, output_path.name, "already downloaded"))
            continue

        try:
            print(f"Downloading {paper_id}: {title}")
            print(f"  {pdf_url}")
            download_file(pdf_url, output_path)
            downloaded.append((paper_id, output_path.name, "downloaded"))
        except RuntimeError as error:
            failed.append((paper_id, title, str(error)))

    zip_path = Path(args.zip_path)
    zip_directory(output_dir, zip_path)

    print()
    print("Done.")
    print(f"Downloaded/existing PDFs: {len(downloaded)}")
    print(f"Skipped: {len(skipped)}")
    print(f"Failed: {len(failed)}")
    print(f"Zip: {zip_path.resolve()}")

    if failed:
        print()
        print("Failed rows:")
        for paper_id, title, error in failed:
            print(f"- {paper_id}: {title}")
            print(f"  {error}")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())