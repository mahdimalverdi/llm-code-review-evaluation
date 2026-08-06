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

# Render draft TODO markers as visible red boxes in the generated PDF.
# In Markdown, write them as plain paragraphs starting with: DRAFTTODO:
python3 - <<'PY'
from pathlib import Path
import re

tex_path = Path("build/paper.tex")
content = tex_path.read_text(encoding="utf-8")
pattern = re.compile(r"^DRAFTTODO:\s*(.*)$", re.MULTILINE)

def render(match: re.Match[str]) -> str:
    text = match.group(1)
    return "\n".join([
        r"\begin{center}",
        r"\fcolorbox{red}{red!4}{%",
        r"\begin{minipage}{0.93\linewidth}",
        r"\textbf{\textcolor{red}{TODO:}} " + text,
        r"\end{minipage}%",
        r"}",
        r"\end{center}",
    ])

tex_path.write_text(pattern.sub(render, content), encoding="utf-8")
PY

cd build

run_pdflatex() {
  local log_file="paper.log"
  if pdflatex -interaction=nonstopmode -halt-on-error paper.tex; then
    return 0
  fi

  if [[ -f "$log_file" ]] && grep -q "File ended while scanning use of" "$log_file"; then
    echo "WARN: pdflatex found a truncated aux file; removing aux state for a clean pipeline retry." >&2
    rm -f paper.aux paper.bbl paper.blg paper.brf paper.out paper.toc
    return 1
  fi

  echo "ERROR: pdflatex failed. Check build/paper.log if it is still present." >&2
  return 1
}

run_bibtex() {
  local bibliography_name="$1"
  # The complete study bibliography contains non-ASCII author names. bibtexu
  # preserves UTF-8 metadata that classic BibTeX can corrupt in the BBL output.
  if ! bibtexu "$bibliography_name"; then
    echo "ERROR: BibTeX failed. Check build/${bibliography_name}.blg." >&2
    return 1
  fi

  if [[ ! -s "${bibliography_name}.bbl" ]] \
    || grep -Eq "I found no \\\\(citation|bibdata|bibstyle) command" "${bibliography_name}.blg"; then
    echo "ERROR: BibTeX did not produce a usable bibliography. Check build/${bibliography_name}.aux and build/${bibliography_name}.blg." >&2
    return 1
  fi
}

build_pdf_pipeline() {
  # Defensively remove auxiliary files immediately before the first LaTeX pass.
  # This protects manual rebuilds where an old paper.aux may have survived
  # outside the normal clean path.
  rm -f paper.aux paper.bbl paper.blg paper.brf paper.fdb_latexmk paper.fls \
    paper.lof paper.log paper.lot paper.out paper.toc

  # Use an explicit, deterministic LaTeX/BibTeX sequence instead of relying on
  # latexmk's dependency detection. This keeps citation and reference resolution
  # predictable across local TeX installations.
  # Two initial passes populate the bibliography and cross-reference state
  # reliably from a clean build directory.
  run_pdflatex || return 1
  run_pdflatex || return 1
  run_bibtex paper || return 1
  run_pdflatex || return 1
  run_pdflatex || return 1
  run_pdflatex || return 1
}

pipeline_succeeded=0
for attempt in 1 2 3; do
  if build_pdf_pipeline; then
    pipeline_succeeded=1
    break
  fi

  echo "WARN: LaTeX/BibTeX pipeline failed on attempt ${attempt}; retrying from a clean aux state." >&2
done

if [[ "$pipeline_succeeded" -ne 1 ]]; then
  echo "ERROR: LaTeX/BibTeX pipeline failed after repeated clean attempts." >&2
  exit 1
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
