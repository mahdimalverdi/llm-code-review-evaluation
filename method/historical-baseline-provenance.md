# Historical Baseline Provenance

The 71-study historical baseline (P01--P71) was assembled through an earlier
search and tracked in a working Google Sheet before the dated supplementary
search amendment:

<https://docs.google.com/spreadsheets/d/14tTs2nwIwS40JU-na5bbwBNgyPYkZv9IPXVPfbPUR1I/edit?gid=2069431606#gid=2069431606>

The source tab was exported on 6 August 2026. At export time, it contained ten
methodological records (M01--M10) and 71 substantive records (P01--P71). The
sheet records bibliographic identity, topic, intended relevance, evaluation
dimensions, limitations, verification notes, and other planning metadata.

`data/historical-baseline-inventory.csv` preserves a compact snapshot of the
substantive records. It retains only the fields needed to identify each study
and understand its original role in the project:

- project ID and bibliography key;
- title and year;
- main topic area;
- stated relevance to the paper;
- gap or limitation type; and
- verification status.

This snapshot is provenance, not a canonical extraction dataset. Fields prefixed
with `Source` preserve the values present in the sheet at export time. The
current study-level coding remains in `data/slr-extraction.csv`, and bibliography
data remain in `references/references.bib`. If values conflict, those canonical
files take precedence.

Comparison with the current extraction found complete ID and citation-key
coverage for P01--P71. It also found source-year differences for P06 (2025 in
the sheet; 2026 in the canonical record), P31 (2025; 2026), and P34 (2025;
2026). Several titles differ only in capitalization or explanatory suffixes;
P34 also uses a different current bibliographic title. These differences are
retained here because the file records the historical sheet rather than
silently replacing it with current metadata.

The sheet helps document how the search results retained in the baseline were
organized and why their studies were considered relevant. It does not contain the original
database-specific queries, retrieval dates and counts, deduplication trail, or
excluded-record log. It therefore does not reconstruct the search and screening
history of the historical baseline.

A retrospective comparison with the dated 2026-08-02 search is recorded in
[`historical-baseline-retrieval-audit.md`](historical-baseline-retrieval-audit.md).
That audit independently rediscovers all 71 baseline studies through topic-level
queries. It therefore supports corpus retrievability without reconstructing the
original result sets or selection process.
