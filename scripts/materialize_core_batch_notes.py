#!/usr/bin/env python3
"""Create canonical-schema provisional notes for a selected core batch."""

from __future__ import annotations

import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def rows(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def safe(value: str) -> str:
    return value or "Not reported"


def main() -> None:
    queue = {r["provisional_project_id"]: r for r in rows(ROOT / "data/search/core-reconciliation-queue.csv")}
    screening = {r["candidate_id"]: r for r in rows(ROOT / "data/search/arxiv-full-text-screening.csv")}
    selected = [f"P{i:02d}" for i in range(72, 89)]
    out_dir = ROOT / "papers/provisional"
    for pid in selected:
        q = queue[pid]
        s = screening[q["candidate_id"]]
        title = q["title"]
        slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")[:60]
        first = q["authors"].split(";")[0].split()[-1].lower() or "unknown"
        key = f"p{pid[1:]}_{first}{q['submitted'][:4]}_{re.sub(r'[^a-z0-9]+', '_', title.lower()).strip('_')[:30]}"
        text = f"""# {pid} — {title}

## 1. Identification

- Project ID: `{pid}` (provisional)
- Citation key: `{key}`
- Full reference: {safe(q['authors'])}. “{title}.” arXiv, {q['submitted'][:4]}.
- DOI/URL: `https://arxiv.org/abs/{q['arxiv_id']}`
- Review date: {s['screening_date']}
- Source/database: arXiv amendment, full-text screening
- Search string used, if applicable: Recorded in `method/search-run-log.csv`.
- Selection stage: included for reconciliation; canonical corpus integration pending
- Duplicate or companion publication: Not reported; verify before final inclusion.

## 2. Screening

- Decision: `Include`
- Relevance: `High`
- Decision rationale: {s['decision_rationale']}
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: taxonomy / annotation protocol / mitigation design / trade-off framework
- Exact inclusion criterion: {s['exact_criterion']}

## 3. Study overview

- Purpose: {title}
- Research questions: Not reported as a separate list.
- Method: Not reported in the screening ledger; verify from the full text.
- Evaluated system/artifact: Not reported; screening evidence indicates direct code-review relevance.
- Dataset/benchmark: Not reported.
- Input context: Not reported.
- Main findings: {s['decision_rationale']}

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Review-specific failure or quality evidence is indicated by the screening rationale; detailed extraction pending. | Reported | {s['evidence_location']} |
| RQ2 | Evaluation dimensions require full-text extraction. | Not reported | {s['evidence_location']} |
| RQ3 | Mitigation or generation intervention requires full-text extraction. | Not reported | {s['evidence_location']} |
| RQ4 | Trade-off evidence requires full-text extraction. | Not reported | {s['evidence_location']} |
| RQ5 | Context, dataset, and annotation validity require full-text extraction. | Not reported | {s['evidence_location']} |
| RQ6 | Direct core relevance supports later framework mapping. | Inferred | {s['evidence_location']} |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Not yet coded | Detailed failure categories require canonical full-text extraction. | Not reported | {s['evidence_location']} |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Not yet coded | Metrics and rubrics require full-text extraction. | Not reported | {s['evidence_location']} |

## 7. Mitigation and trade-offs

- Mitigation family: Not reported.
- Intervention point: Not reported.
- What it reduces: Not reported.
- Useful feedback potentially lost: Not reported.
- Coverage effect: Not reported.
- Human escalation effect: Not reported.
- Computational/operational cost: Not reported.
- New failure modes: Not reported.

## 8. Annotation and evaluator validity

- Judge/annotator: Not reported.
- Rubric: Not reported.
- Agreement/reliability: Not reported.
- Validity checks: Not reported.
- Possible bias: Full-text extraction pending.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 1 | Artifact relevance is identified; full details pending. |
| Q2 | 0 | Input context not extracted. |
| Q3 | 0 | Dataset not extracted. |
| Q4 | 0 | Metrics not extracted. |
| Q5 | 0 | Judging protocol not extracted. |
| Q6 | 0 | Reliability not extracted. |
| Q7 | 0 | Annotation details not extracted. |
| Q8 | 0 | Validity checks not extracted. |
| Q9 | 0 | Mitigation not extracted. |
| Q10 | 0 | Cost not extracted. |
| Q11 | 0 | Limitations not extracted. |
| Q12 | 1 | Direct review relevance is recorded in screening. |

- Total: `2/24` provisional
- Quality interpretation: Screening-complete intake record; not ready for synthesis citation.

## 10. Review-process reliability and bias

- Missing data: Most extraction fields remain pending.
- Publication-bias concern: Not reported.
- Selection uncertainty: Included by full-text screening; duplicate/version check pending.
- Extraction uncertainty: High until canonical reading is complete.
- Second-reviewer agreement: Not available.
- Duplicate-publication handling: Pending.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Candidate core evidence requiring full extraction.
- What the paper does not establish: Cannot be determined until full-text extraction is complete.
- Research gap supported: Not yet determined.
- Candidate synthesis claims: None beyond the bounded screening rationale.
- Follow-up verification needed: Complete full-text extraction, quality appraisal, duplicate resolution, and metadata verification.
"""
        (out_dir / f"{pid}-{slug}.md").write_text(text, encoding="utf-8")
    print(f"wrote {len(selected)} provisional canonical-schema notes")


if __name__ == "__main__":
    main()
