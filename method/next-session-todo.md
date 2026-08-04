# Next-Session SLR Worklist

## Current position

The review remains a targeted structured review. A dated supplementary identification stage has been recorded, but the planned external-source searches do not yet provide exhaustive native result sets or counts. No new externally discovered study may be cited as included evidence until independent screening and full-text assessment are complete.

## Resume in this order

1. **Reconcile the completed arXiv full-text screening with the baseline corpus.**
   - `data/search/arxiv-full-text-screening-reviewed.csv` contains 140 reviewed records: 132 included and 8 excluded; no records remain pending.
   - Match included records against P01–P71 and external candidates by arXiv ID, DOI, normalized title, and version/companion relationship.
   - Assign new project IDs only after duplicate resolution; do not count the 132 screening inclusions as final studies yet.
   - Preserve the recorded eligibility criterion, evidence location, rationale, tier, reviewer, and date.
   - The initial exact-ID/title pass found 1 direct match to an existing paper (P05) and 131 unmatched candidates: 52 `core` and 79 `supporting`. Review the 52 core candidates first; this ledger is a triage aid, not a final duplicate decision.
   - The 52-record core queue is materialized in `data/search/core-reconciliation-queue.csv` with provisional IDs P72–P123. Two records (P108/EXT-0028 and P116/EXT-0030) are now flagged as external duplicate/companion candidates; 50 remain for independent version and metadata verification. These IDs must not be cited or treated as final until verification is complete.

2. **Resolve the supplied external-source candidates.**
   - `data/search/external-candidate-screening.csv` contains 30 identifier-level records: 9 already in the corpus, 8 already in the arXiv queue, and 13 still requiring independent title/abstract verification.
   - Do not adopt supplied labels as decisions. Check the title, abstract, and official metadata; then obtain and assess the full text for studies that pass.
   - `data/search/external-pdf-acquisition.csv` records acquired PDFs and mappings to existing preprints. Find legitimate open versions for the remaining eligible records; log unavailable/paywalled cases rather than using unaudited copies.

3. **Complete external source coverage where access becomes available.**
   - Re-run Semantic Scholar after rate limits clear.
   - Execute the documented queries in ACM Digital Library, IEEE Xplore, ScienceDirect, SpringerLink, Google Scholar, and Scopus through authorised/manual access where possible.
   - Record exact query, date, native retrieved count, deduplication result, and source-access limitation. The supplied external export is partial and cannot be used to claim exhaustive coverage.

4. **Freeze the eligible set and integrate evidence.**
   - Assign stable project IDs only after full-text inclusion and duplicate/companion resolution.
   - Add verified bibliography records, create uniform paper notes, update extraction data, and rerun structural validation.
   - Recalculate every reported count by evidence tier and denominator; keep reported evidence distinct from inference.

5. **Reassess review status.**
   - The work may be described as an SLR only once search coverage, selection decisions, quality assessment, extraction, and final study set are fully documented. Until then retain the targeted-structured-review framing.

## Operational safeguards

- Preserve raw search exports and generated worksheets; do not overwrite screening decisions.
- Treat a preprint and published version as one study, preferring the version of record for citation after confirming equivalence.
- Validate every downloaded file as a PDF before review.
- Do not add a new paper merely because its title is relevant; apply the protocol’s eligibility criteria and record exclusions.
