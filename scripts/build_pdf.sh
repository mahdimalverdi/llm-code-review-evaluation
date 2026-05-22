#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Fully clean generated LaTeX artifacts before rebuilding. This avoids stale or
# corrupted auxiliary files such as paper.aux containing NUL bytes.
rm -rf build
mkdir -p build

python3 scripts/build_latex.py

cd build

latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex

if [ ! -f paper.pdf ]; then
  echo "ERROR: paper.pdf was not produced. Check build/paper.log and build/paper.blg." >&2
  exit 1
fi

echo "Built build/paper.pdf"
