#!/usr/bin/env python3
"""Build the manuscript PDF through the canonical shell pipeline.

Usage:
    python3 scripts/build_pdf.py
"""

from __future__ import annotations

import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
BUILD_SCRIPT = REPO_ROOT / "scripts" / "build_pdf.sh"


def main() -> int:
    """Run the shared LaTeX and bibliography build pipeline."""
    result = subprocess.run(
        ["bash", str(BUILD_SCRIPT)],
        cwd=REPO_ROOT,
        check=False,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
