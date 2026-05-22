#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Fully clean generated LaTeX artifacts before rebuilding. This avoids stale or
# corrupted auxiliary files such as paper.aux from a failed previous run.
rm -rf build
mkdir -p build

python3 scripts/build_latex.py

if [[ ! -f build/paper.tex ]]; then
  echo "ERROR: build/paper.tex was not produced." >&2
  exit 1
fi

if [[ ! -f build/references.bib ]]; then
  echo "ERROR: build/references.bib was not produced." >&2
  exit 1
fi

cd build

if command -v latexmk >/dev/null 2>&1; then
  latexmk -pdf -interaction=nonstopmode -halt-on-error paper.tex
else
  pdflatex -interaction=nonstopmode -halt-on-error paper.tex
  bibtex paper
  pdflatex -interaction=nonstopmode -halt-on-error paper.tex
  pdflatex -interaction=nonstopmode -halt-on-error paper.tex
fi

cd "$REPO_ROOT"

if [[ ! -f build/paper.pdf ]]; then
  echo "ERROR: build/paper.pdf was not produced. Check build/paper.log and build/paper.blg." >&2
  exit 1
fi

DIAGNOSTICS="$(python3 scripts/diagnose_latex.py)"
if grep -Eq "Undefined citation keys:|Undefined LaTeX references:" <<<"$DIAGNOSTICS"; then
  echo "$DIAGNOSTICS" >&2
  echo "ERROR: unresolved citations or LaTeX references remain." >&2
  exit 1
fi

echo "Built build/paper.pdf"
