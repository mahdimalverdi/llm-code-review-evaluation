#!/usr/bin/env python3
"""Build a single LaTeX paper draft from Markdown section files.

This script is intentionally lightweight. It supports the Markdown subset used in
`drafts/paper/sections/` and converts it into a single LaTeX file. It is not a
full Markdown or Pandoc replacement.

Usage:
    python scripts/build_latex.py

Output:
    build/paper.tex
"""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ORDER_FILE = REPO_ROOT / "drafts" / "paper" / "sections_order.txt"
DEFAULT_OUTPUT_FILE = REPO_ROOT / "build" / "paper.tex"

LATEX_HEADER = r"""\documentclass[10pt,conference]{IEEEtran}

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{cite}
\usepackage{url}
\usepackage{booktabs}
\usepackage{enumitem}
\usepackage{listings}
\usepackage{xcolor}

\lstset{
  basicstyle=\ttfamily\small,
  breaklines=true,
  columns=fullflexible,
  frame=single
}

\title{Evaluating Problematic LLM-Generated Code Review Comments: An Operational Taxonomy and a Trade-off-Aware Framework}

\author{%
  \IEEEauthorblockN{TODO: Author Name(s)}
  \IEEEauthorblockA{TODO: Affiliation\\
  TODO: Email}
}

\begin{document}
\maketitle
"""

LATEX_FOOTER = r"""
\bibliographystyle{IEEEtran}
\bibliography{../references/references}

\end{document}
"""

SPECIAL_CHARS = {
    "&": r"\&",
    "%": r"\%",
    "$": r"\$",
    "#": r"\#",
    "_": r"\_",
    "{": r"\{",
    "}": r"\}",
    "~": r"\textasciitilde{}",
    "^": r"\textasciicircum{}",
}


def escape_latex(text: str) -> str:
    """Escape LaTeX special characters outside inline commands we generate."""
    escaped = []
    for char in text:
        escaped.append(SPECIAL_CHARS.get(char, char))
    return "".join(escaped)


def convert_citations(text: str) -> str:
    """Convert Pandoc-style citations to LaTeX citep commands.

    Example:
        [@a; @b] -> \citep{a,b}
    """

    def replace(match: re.Match[str]) -> str:
        body = match.group(1)
        keys = []
        for part in body.split(";"):
            part = part.strip()
            if part.startswith("@"):
                keys.append(part[1:])
        if not keys:
            return match.group(0)
        return r"\citep{" + ",".join(keys) + "}"

    return re.sub(r"\[((?:@[^\]]+?)(?:;\s*@[^\]]+?)*)\]", replace, text)


def convert_inline_markdown(text: str) -> str:
    """Convert a small subset of inline Markdown to LaTeX."""
    placeholders: dict[str, str] = {}

    def protect(pattern: str, repl_func):
        nonlocal text

        def repl(match: re.Match[str]) -> str:
            key = f"@@PLACEHOLDER_{len(placeholders)}@@"
            placeholders[key] = repl_func(match)
            return key

        text = re.sub(pattern, repl, text)

    text = convert_citations(text)

    protect(r"`([^`]+)`", lambda m: r"\texttt{" + escape_latex(m.group(1)) + "}")
    text = escape_latex(text)

    text = re.sub(r"\*\*([^*]+)\*\*", r"\\textbf{\1}", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"\\emph{\1}", text)

    for key, value in placeholders.items():
        text = text.replace(escape_latex(key), value)
        text = text.replace(key, value)

    return text


def heading_to_latex(line: str) -> str | None:
    match = re.match(r"^(#{1,6})\s+(.*)$", line)
    if not match:
        return None
    level = len(match.group(1))
    title = convert_inline_markdown(match.group(2).strip())
    if level == 1:
        return rf"\section{{{title}}}"
    if level == 2:
        return rf"\subsection{{{title}}}"
    if level == 3:
        return rf"\subsubsection{{{title}}}"
    return rf"\paragraph{{{title}}}"


def convert_markdown_to_latex(markdown: str) -> str:
    """Convert repository Markdown draft sections into rough LaTeX."""
    lines = markdown.splitlines()
    output: list[str] = []
    in_code_block = False
    in_itemize = False
    in_enumerate = False
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            output.append(convert_inline_markdown(" ".join(paragraph).strip()))
            output.append("")
            paragraph = []

    def close_lists() -> None:
        nonlocal in_itemize, in_enumerate
        if in_itemize:
            output.append(r"\end{itemize}")
            output.append("")
            in_itemize = False
        if in_enumerate:
            output.append(r"\end{enumerate}")
            output.append("")
            in_enumerate = False

    for raw_line in lines:
        line = raw_line.rstrip()

        if line.strip().startswith("<!--"):
            flush_paragraph()
            close_lists()
            continue

        if line.strip().startswith("> [!"):
            flush_paragraph()
            close_lists()
            continue

        if line.strip().startswith(">"):
            flush_paragraph()
            close_lists()
            continue

        if line.strip().startswith("```"):
            flush_paragraph()
            close_lists()
            if in_code_block:
                output.append(r"\end{lstlisting}")
                output.append("")
                in_code_block = False
            else:
                output.append(r"\begin{lstlisting}")
                in_code_block = True
            continue

        if in_code_block:
            output.append(html.unescape(line))
            continue

        if not line.strip():
            flush_paragraph()
            close_lists()
            continue

        heading = heading_to_latex(line)
        if heading is not None:
            flush_paragraph()
            close_lists()
            output.append(heading)
            output.append("")
            continue

        bullet_match = re.match(r"^[-*]\s+(.*)$", line)
        if bullet_match:
            flush_paragraph()
            if in_enumerate:
                output.append(r"\end{enumerate}")
                in_enumerate = False
            if not in_itemize:
                output.append(r"\begin{itemize}[leftmargin=*]")
                in_itemize = True
            output.append(r"\item " + convert_inline_markdown(bullet_match.group(1).strip()))
            continue

        enum_match = re.match(r"^\d+\.\s+(.*)$", line)
        if enum_match:
            flush_paragraph()
            if in_itemize:
                output.append(r"\end{itemize}")
                in_itemize = False
            if not in_enumerate:
                output.append(r"\begin{enumerate}[leftmargin=*]")
                in_enumerate = True
            output.append(r"\item " + convert_inline_markdown(enum_match.group(1).strip()))
            continue

        # Markdown tables are kept as verbatim blocks for now.
        if line.lstrip().startswith("|"):
            flush_paragraph()
            close_lists()
            output.append(r"\begin{lstlisting}")
            output.append(line)
            output.append(r"\end{lstlisting}")
            output.append("")
            continue

        paragraph.append(line.strip())

    flush_paragraph()
    close_lists()

    return "\n".join(output).strip() + "\n"


def read_order(order_file: Path) -> list[Path]:
    base_dir = order_file.parent
    sections = []
    for raw_line in order_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        sections.append(base_dir / line)
    return sections


def build_latex(order_file: Path, output_file: Path) -> None:
    sections = read_order(order_file)
    missing = [str(path) for path in sections if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing section files:\n" + "\n".join(missing))

    parts = [LATEX_HEADER]
    for section_path in sections:
        markdown = section_path.read_text(encoding="utf-8")
        parts.append(f"% Source: {section_path.relative_to(REPO_ROOT)}\n")
        parts.append(convert_markdown_to_latex(markdown))
        parts.append("\n")
    parts.append(LATEX_FOOTER)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote {output_file.relative_to(REPO_ROOT)}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--order-file",
        type=Path,
        default=DEFAULT_ORDER_FILE,
        help="Path to section order file.",
    )
    parser.add_argument(
        "--output-file",
        type=Path,
        default=DEFAULT_OUTPUT_FILE,
        help="Path to generated LaTeX output.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    build_latex(args.order_file, args.output_file)


if __name__ == "__main__":
    main()
