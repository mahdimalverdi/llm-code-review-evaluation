#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

python3 scripts/build_latex.py

cd build

rm -f paper.aux paper.bbl paper.blg paper.fdb_latexmk paper.fls paper.log paper.out paper.pdf paper.synctex.gz

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
