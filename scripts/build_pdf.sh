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

pdflatex -interaction=nonstopmode -halt-on-error paper.tex
bibtex paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex

if grep -q "Citation .* undefined" paper.log; then
  echo "ERROR: unresolved citations remain. Check build/paper.log and build/paper.blg." >&2
  exit 1
fi

if grep -q "There were undefined references" paper.log; then
  echo "ERROR: undefined references remain. Check build/paper.log and build/paper.blg." >&2
  exit 1
fi

echo "Built build/paper.pdf"
