# Historical Baseline Retrieval Audit

## Purpose

This audit tests whether the 71-study historical baseline can be rediscovered
from the dated search records currently retained in the project. It does not
infer that a study was retrieved by the original search merely because it can
be located by title on the web. A positive match requires an identifier or
normalized-title match in a retained candidate export.

## Inputs

- Historical inventory: `data/historical-baseline-inventory.csv`
- Exact arXiv run: `data/search/arxiv-candidates.csv`
- Partial external export:
  `data/search/external-supplied-candidate-records-2026-08-02.csv`
- Query definitions and counts: `method/search-run-log.csv`
- Retrospective external-source runs:
  `data/search/historical-baseline-external-audit.csv`

The arXiv run comprises the three queries documented as Q1--Q3 and covers
2021-01-01 through 2026-08-02. The external export is explicitly
non-exhaustive and therefore cannot establish a negative result for any
publisher database.

## Results

| Retrieval status | Studies | Count |
|---|---|---:|
| Rediscovered in the retained arXiv result pool | P01--P08, P10--P13, P15, P17--P22, P26, P35, P41, P53--P61, P63--P68, P71 | 38 |
| Rediscovered only in the partial external export | P25 | 1 |
| Rediscovered by retrospective OpenAlex queries | P14, P16, P29, P30, P33, P34, P36, P44 | 8 |
| Rediscovered by the retrospective Crossref query, but not the OpenAlex queries | P48 | 1 |
| Rediscovered by additional conceptual OpenAlex queries | P09, P37, P39, P42, P43, P46, P70 | 7 |
| Rediscovered by additional conceptual web queries | P23, P24, P27, P28, P31, P38, P40, P45, P49, P51 | 10 |
| Rediscovered by final conceptual queries | P32, P47, P50, P52, P62, P69 | 6 |
| Not located | -- | 0 |

The 38 arXiv matches represent 53.5% of the historical baseline. Across all
topic-level searches, all 71 studies were rediscovered without using exact
titles, identifiers, system names, or author names as queries. P63 is treated as
a match to arXiv `2603.18740`: the historical sheet truncates the final zero and
uses an earlier title variant, while the retained candidate metadata records
the current title and versioned identifier.

The first Semantic Scholar bulk-API attempt returned HTTP 403, but a later
rate-limited rerun completed with 963 raw query hits and 427 unique records.
Exact normalized-title reconciliation rediscovered 39 of the 71 historical
baseline studies. The OpenAlex and
Crossref interfaces returned ranked result sets rather than database-native
Boolean searches, so their matches demonstrate independent retrievability but
do not reconstruct the original publisher-database runs.

## Interpretation

The audit shows that a multi-source, multi-query strategy can independently
rediscover nearly all of the baseline. The direct Q1--Q3 code-review searches
alone are insufficient. High coverage requires separate query families for
review-comment generation, evaluator validity and LLM-as-a-Judge, modern code
review and reviewability, LLM4SE surveys, security and static analysis, code
refinement, model misalignment, code-efficiency evaluation, industrial
productivity studies, and semantic review-comment evaluation.

Accordingly, the defensible claim is **100% topic-query rediscovery of the
historical baseline**, not reconstruction of its original search and screening
history. Full reconstruction would additionally require executing and retaining
database-native searches, pre-registering the supplementary query families and
citation-chaining rules, and screening the complete result sets under the
recorded eligibility criteria.
