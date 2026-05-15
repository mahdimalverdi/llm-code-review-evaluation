#!/usr/bin/env python3
r"""Build a single LaTeX journal-style manuscript from Markdown sections.

This script is intentionally lightweight. It supports the Markdown subset used in
`drafts/paper/sections/` and converts it into a single LaTeX file. It is not a
full Markdown or Pandoc replacement.

Usage:
    python3 scripts/build_latex.py

Output:
    build/paper.tex
    build/references.bib

Supported table metadata syntax:
    <!-- table: caption="Caption text" label="tab:example" -->
    | Column A | Column B |
    | --- | --- |
    | Value A | Value B |

    Long tables can be requested explicitly:
    <!-- table: caption="Caption text" label="tab:example" longtable="true" -->

    The script also promotes tables to longtable automatically when they are
    long enough or wide enough that a floating tabularx table is likely to be
    hard to read or impossible to keep on one page.
"""

from __future__ import annotations

import argparse
import html
import re
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ORDER_FILE = REPO_ROOT / "drafts" / "paper" / "sections_order.txt"
DEFAULT_OUTPUT_FILE = REPO_ROOT / "build" / "paper.tex"
REFERENCES_FILE = REPO_ROOT / "references" / "references.bib"
BUILD_REFERENCES_FILE_NAME = "references.bib"

TITLE = "Evaluating Problematic LLM-Generated Code Review Comments: An Operational Taxonomy and a Trade-off-Aware Framework"

LATEX_HEADER = rf"""\documentclass[12pt]{{article}}

\usepackage{{cmap}}
\usepackage[T1]{{fontenc}}
\usepackage[utf8]{{inputenc}}
\usepackage{{lmodern}}
\usepackage[a4paper,margin=1in]{{geometry}}
\usepackage{{amsmath}}
\usepackage{{array}}
\usepackage{{booktabs}}
\usepackage{{cite}}
\usepackage{{float}}
\usepackage{{longtable}}
\usepackage{{microtype}}
\usepackage{{tabularx}}
\usepackage{{url}}
\usepackage{{listings}}
\usepackage{{xcolor}}
\usepackage[hidelinks]{{hyperref}}

\linespread{{1.08}}
\setlength{{\parindent}}{{0pt}}
\setlength{{\parskip}}{{0.65em}}

\lstset{{
  basicstyle=\ttfamily\small,
  breaklines=true,
  columns=fullflexible,
  frame=single
}}

\newcommand{{\keywords}}[1]{{%
  \vspace{{0.75em}}
  \noindent\textbf{{Keywords: }}#1
}}

\title{{\textbf{{{TITLE}}}}}
\author{{%
Mahdi Malverdi\\
Department of Computer Science and Engineering\\
Shahid Beheshti University, Tehran, Iran\\
\url{{m.malverdi@mail.sbu.ac.ir}}
\and
Hassan Haghighi\\
Department of Computer Science and Engineering\\
Shahid Beheshti University, Tehran, Iran\\
\url{{h_haghighi@sbu.ac.ir}}
}}
\date{{}}

\begin{{document}}
\maketitle
"""

LATEX_FOOTER = r"""
\bibliographystyle{plain}
\bibliography{references}

\end{document}
"""

UNICODE_TEXT_REPLACEMENTS = {
    "“": "``",
    "”": "''",
    "‘": "`",
    "’": "'",
    "–": "--",
    "—": "---",
    "‑": "-",
    "‐": "-",
    "−": "-",
    "…": r"\ldots{}",
    "→": r"$\rightarrow$",
    "←": r"$\leftarrow$",
    "⇒": r"$\Rightarrow$",
    "≤": r"$\leq$",
    "≥": r"$\geq$",
    "×": r"$\times$",
}

UNICODE_VERBATIM_REPLACEMENTS = {
    "“": '"',
    "”": '"',
    "‘": "'",
    "’": "'",
    "–": "-",
    "—": "--",
    "‑": "-",
    "‐": "-",
    "−": "-",
    "…": "...",
    "→": "->",
    "←": "<-",
    "⇒": "=>",
    "≤": "<=",
    "≥": ">=",
    "×": "x",
}

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

LONGTABLE_ROW_THRESHOLD = 6
LONGTABLE_COLUMN_THRESHOLD = 4

TABLE_METADATA_PATTERN = re.compile(r"^<!--\s*table:\s*(.*?)\s*-->\s*$")
TABLE_ATTRIBUTE_PATTERN = re.compile(r"(caption|label|longtable)\s*=\s*(['\"])(.*?)\2")
RAW_LATEX_INLINE_PATTERN = re.compile(r"\\(?:ref|autoref|pageref)\{[^}]+\}")


def normalize_text_unicode(text: str) -> str:
    """Replace common Unicode punctuation with pdflatex-friendly text."""
    for source, target in UNICODE_TEXT_REPLACEMENTS.items():
        text = text.replace(source, target)
    return text


def normalize_verbatim_unicode(text: str) -> str:
    """Replace Unicode characters that break listings under pdflatex."""
    for source, target in UNICODE_VERBATIM_REPLACEMENTS.items():
        text = text.replace(source, target)
    return text


def escape_latex(text: str) -> str:
    """Escape LaTeX special characters outside generated LaTeX commands."""
    text = normalize_text_unicode(text)
    return "".join(SPECIAL_CHARS.get(char, char) for char in text)


def citation_to_latex(match: re.Match[str]) -> str:
    r"""Convert one Pandoc-style citation group to a LaTeX \cite command.

    Example:
        [@a; @b] -> \cite{a,b}
    """
    body = match.group(1)
    keys = []
    for part in body.split(";"):
        part = part.strip()
        if part.startswith("@"):
            keys.append(part[1:])
    if not keys:
        return match.group(0)
    return r"\cite{" + ",".join(keys) + "}"


def convert_inline_markdown(text: str) -> str:
    """Convert a small subset of inline Markdown to LaTeX."""
    placeholders: dict[str, str] = {}

    def protect(pattern: str, repl_func) -> None:
        nonlocal text

        def repl(match: re.Match[str]) -> str:
            key = f"@@PLACEHOLDER_{len(placeholders)}@@"
            placeholders[key] = repl_func(match)
            return key

        text = re.sub(pattern, repl, text)

    protect(r"\[((?:@[^\]]+?)(?:;\s*@[^\]]+?)*)\]", citation_to_latex)
    protect(RAW_LATEX_INLINE_PATTERN.pattern, lambda m: m.group(0))
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


def parse_table_metadata(line: str) -> dict[str, str] | None:
    """Parse optional Markdown table metadata from an HTML comment."""
    match = TABLE_METADATA_PATTERN.match(line.strip())
    if not match:
        return None
    metadata = {key: value for key, _, value in TABLE_ATTRIBUTE_PATTERN.findall(match.group(1))}
    return metadata


def split_markdown_table_row(line: str) -> list[str]:
    """Split a simple Markdown table row into cells."""
    stripped = line.strip()
    if stripped.startswith("|"):
        stripped = stripped[1:]
    if stripped.endswith("|"):
        stripped = stripped[:-1]
    return [cell.strip() for cell in stripped.split("|")]


def is_table_separator(cells: list[str]) -> bool:
    """Return true for Markdown table separator rows such as --- or :---:."""
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in cells)


def normalize_table_rows(rows: list[list[str]]) -> list[list[str]]:
    """Pad rows so the LaTeX table has a consistent column count."""
    if not rows:
        return []
    column_count = max(len(row) for row in rows)
    return [row + [""] * (column_count - len(row)) for row in rows]


def table_column_spec(column_count: int) -> str:
    """Return a readable tabularx column specification."""
    ragged = r">{\raggedright\arraybackslash}"
    if column_count == 3:
        return rf"@{{}}{ragged}p{{0.23\linewidth}}{ragged}X{ragged}X@{{}}"
    return "@{}" + "".join(ragged + "X" for _ in range(column_count)) + "@{}"


def longtable_column_spec(column_count: int) -> str:
    """Return a page-breakable longtable column specification."""
    ragged = r">{\raggedright\arraybackslash}"
    if column_count == 2:
        widths = [0.34, 0.58]
    elif column_count == 3:
        widths = [0.22, 0.34, 0.34]
    elif column_count == 4:
        widths = [0.20, 0.23, 0.23, 0.23]
    elif column_count == 5:
        widths = [0.15, 0.17, 0.19, 0.23, 0.18]
    else:
        width = min(0.92 / max(column_count, 1), 0.18)
        widths = [width] * column_count
    columns = "".join(rf"{ragged}p{{{width:.2f}\textwidth}}" for width in widths)
    return rf"@{{}}{columns}@{{}}"


def metadata_longtable_setting(metadata: dict[str, str] | None) -> bool | None:
    """Return explicit longtable metadata, or None when not configured."""
    if not metadata or "longtable" not in metadata:
        return None
    value = metadata["longtable"].strip().lower()
    if value in {"1", "true", "yes", "y"}:
        return True
    if value in {"0", "false", "no", "n"}:
        return False
    return None


def should_use_longtable(body_row_count: int, column_count: int, metadata: dict[str, str] | None) -> bool:
    """Return true when a Markdown table should be rendered as a breakable longtable."""
    explicit_setting = metadata_longtable_setting(metadata)
    if explicit_setting is not None:
        return explicit_setting
    return body_row_count > LONGTABLE_ROW_THRESHOLD or column_count >= LONGTABLE_COLUMN_THRESHOLD


def format_latex_table_row(cells: list[str], *, bold: bool = False) -> str:
    """Format one row of table cells as LaTeX."""
    if bold:
        converted_cells = [r"\textbf{" + convert_inline_markdown(cell) + "}" for cell in cells]
    else:
        converted_cells = [convert_inline_markdown(cell) for cell in cells]
    return " & ".join(converted_cells) + r" \\"


def convert_table_to_tabularx(rows: list[list[str]], caption: str | None, label: str | None) -> list[str]:
    """Convert normalized rows into a floating tabularx table."""
    column_spec = table_column_spec(len(rows[0]))
    output = [r"\begin{table}[H]", r"\centering"]
    if caption:
        output.append(r"\caption{" + convert_inline_markdown(caption) + "}")
    if label:
        output.append(r"\label{" + label + "}")
    output.extend([
        r"\footnotesize",
        r"\renewcommand{\arraystretch}{1.18}",
        rf"\begin{{tabularx}}{{\linewidth}}{{{column_spec}}}",
        r"\toprule",
        format_latex_table_row(rows[0], bold=True),
        r"\midrule",
    ])
    for row in rows[1:]:
        output.append(format_latex_table_row(row))
    output.extend([r"\bottomrule", r"\end{tabularx}", r"\end{table}", ""])
    return output


def convert_table_to_longtable(rows: list[list[str]], caption: str | None, label: str | None) -> list[str]:
    """Convert normalized rows into a page-breakable longtable."""
    column_count = len(rows[0])
    column_spec = longtable_column_spec(column_count)
    header_row = format_latex_table_row(rows[0], bold=True)
    output = [
        r"\begingroup",
        r"\footnotesize",
        r"\renewcommand{\arraystretch}{1.18}",
        rf"\begin{{longtable}}{{{column_spec}}}",
    ]

    if caption:
        caption_line = r"\caption{" + convert_inline_markdown(caption) + "}"
        if label:
            caption_line += r"\label{" + label + "}"
        output.append(caption_line + r" \")

    output.extend([
        r"\toprule",
        header_row,
        r"\midrule",
        r"\endfirsthead",
    ])

    if caption:
        output.append(r"\caption[]{" + convert_inline_markdown(caption) + r" (continued)} \")
    output.extend([
        r"\toprule",
        header_row,
        r"\midrule",
        r"\endhead",
        r"\midrule",
        rf"\multicolumn{{{column_count}}}{{r}}{{Continued on next page}} \",
        r"\endfoot",
        r"\bottomrule",
        r"\endlastfoot",
    ])

    for row in rows[1:]:
        output.append(format_latex_table_row(row))
    output.extend([r"\end{longtable}", r"\endgroup", ""])
    return output


def convert_markdown_table_to_latex(table_lines: list[str], metadata: dict[str, str] | None) -> list[str]:
    """Convert a simple Markdown table to a labeled LaTeX table."""
    parsed_rows = [split_markdown_table_row(line) for line in table_lines]
    parsed_rows = [row for row in parsed_rows if row]
    if len(parsed_rows) < 2:
        return [r"\begin{lstlisting}", *[normalize_verbatim_unicode(line) for line in table_lines], r"\end{lstlisting}", ""]

    header = parsed_rows[0]
    body_rows = parsed_rows[1:]
    if body_rows and is_table_separator(body_rows[0]):
        body_rows = body_rows[1:]

    rows = normalize_table_rows([header, *body_rows])
    if not rows:
        return []

    column_count = len(rows[0])
    caption = metadata.get("caption") if metadata else None
    label = metadata.get("label") if metadata else None

    if should_use_longtable(len(rows) - 1, column_count, metadata):
        return convert_table_to_longtable(rows, caption, label)
    return convert_table_to_tabularx(rows, caption, label)


def convert_markdown_to_latex(markdown: str) -> str:
    """Convert repository Markdown draft sections into rough LaTeX."""
    lines = markdown.splitlines()
    output: list[str] = []
    in_code_block = False
    in_itemize = False
    in_enumerate = False
    paragraph: list[str] = []
    table_lines: list[str] = []
    pending_table_metadata: dict[str, str] | None = None

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

    def flush_table() -> None:
        nonlocal table_lines, pending_table_metadata
        if table_lines:
            output.extend(convert_markdown_table_to_latex(table_lines, pending_table_metadata))
            table_lines = []
            pending_table_metadata = None

    for raw_line in lines:
        line = raw_line.rstrip()

        if table_lines and not line.lstrip().startswith("|"):
            flush_table()

        table_metadata = parse_table_metadata(line)
        if table_metadata is not None:
            flush_paragraph()
            close_lists()
            flush_table()
            pending_table_metadata = table_metadata
            continue

        if line.strip().startswith("<!--"):
            flush_paragraph()
            close_lists()
            flush_table()
            continue

        if line.strip().startswith(">"):
            flush_paragraph()
            close_lists()
            flush_table()
            continue

        if line.strip().startswith("```"):
            flush_paragraph()
            close_lists()
            flush_table()
            if in_code_block:
                output.append(r"\end{lstlisting}")
                output.append("")
                in_code_block = False
            else:
                output.append(r"\begin{lstlisting}")
                in_code_block = True
            continue

        if in_code_block:
            output.append(normalize_verbatim_unicode(html.unescape(line)))
            continue

        if not line.strip():
            flush_paragraph()
            close_lists()
            flush_table()
            continue

        heading = heading_to_latex(line)
        if heading is not None:
            flush_paragraph()
            close_lists()
            flush_table()
            output.append(heading)
            output.append("")
            continue

        bullet_match = re.match(r"^[-*]\s+(.*)$", line)
        if bullet_match:
            flush_paragraph()
            flush_table()
            if in_enumerate:
                output.append(r"\end{enumerate}")
                in_enumerate = False
            if not in_itemize:
                output.append(r"\begin{itemize}")
                in_itemize = True
            output.append(r"\item " + convert_inline_markdown(bullet_match.group(1).strip()))
            continue

        enum_match = re.match(r"^\d+\.\s+(.*)$", line)
        if enum_match:
            flush_paragraph()
            flush_table()
            if in_itemize:
                output.append(r"\end{itemize}")
                in_itemize = False
            if not in_enumerate:
                output.append(r"\begin{enumerate}")
                in_enumerate = True
            output.append(r"\item " + convert_inline_markdown(enum_match.group(1).strip()))
            continue

        if line.lstrip().startswith("|"):
            flush_paragraph()
            close_lists()
            table_lines.append(line)
            continue

        paragraph.append(line.strip())

    flush_paragraph()
    close_lists()
    flush_table()

    return "\n".join(output).strip() + "\n"


def convert_abstract_section(markdown: str) -> str:
    """Convert the abstract Markdown section into a LaTeX abstract block."""
    body_lines = []
    for line in markdown.splitlines():
        if re.match(r"^#\s+Abstract\s*$", line.strip(), flags=re.IGNORECASE):
            continue
        body_lines.append(line)
    body = convert_markdown_to_latex("\n".join(body_lines)).strip()
    if not body:
        body = "TODO: Write the abstract after the framework and illustrative study are stable."
    return "\n".join([
        r"\begin{abstract}",
        body,
        r"\end{abstract}",
        r"\keywords{LLM-based code review; automated code review; evaluation framework; problematic comments; context quality; LLM-as-a-Judge}",
        "",
    ])


def read_order(order_file: Path) -> list[Path]:
    base_dir = order_file.parent
    sections = []
    for raw_line in order_file.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        sections.append(base_dir / line)
    return sections


def copy_references(output_file: Path) -> None:
    """Copy references.bib next to the generated paper.tex for reliable BibTeX resolution."""
    if not REFERENCES_FILE.exists():
        raise FileNotFoundError(f"Missing bibliography file: {REFERENCES_FILE}")
    output_file.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(REFERENCES_FILE, output_file.parent / BUILD_REFERENCES_FILE_NAME)


def build_latex(order_file: Path, output_file: Path) -> None:
    sections = read_order(order_file)
    missing = [str(path) for path in sections if not path.exists()]
    if missing:
        raise FileNotFoundError("Missing section files:\n" + "\n".join(missing))

    parts = [LATEX_HEADER]
    for section_path in sections:
        markdown = section_path.read_text(encoding="utf-8")
        parts.append(f"% Source: {section_path.relative_to(REPO_ROOT)}\n")
        if section_path.name.startswith("00-abstract"):
            parts.append(convert_abstract_section(markdown))
        else:
            parts.append(convert_markdown_to_latex(markdown))
        parts.append("\n")
    parts.append(LATEX_FOOTER)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text("\n".join(parts), encoding="utf-8")
    copy_references(output_file)
    print(f"Wrote {output_file.relative_to(REPO_ROOT)}")
    print(f"Copied {REFERENCES_FILE.relative_to(REPO_ROOT)} to {output_file.parent.relative_to(REPO_ROOT) / BUILD_REFERENCES_FILE_NAME}")


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
