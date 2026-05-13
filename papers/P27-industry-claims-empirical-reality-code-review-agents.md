# P27 — From Industry Claims to Empirical Reality: An Empirical Study of Code Review Agents in Pull Requests

> [!NOTE]
> Compact v2 analysis. P27 is important for our workflow-aware evaluation argument because it connects code review agent feedback quality with pull-request outcomes and introduces a signal-to-noise framing for automated review comments.

## Status

- Paper ID: `P27`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup`
- Priority: `Medium / High`
- Reading depth: `Read once from PDF`
- Confidence: `High`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | From Industry Claims to Empirical Reality: An Empirical Study of Code Review Agents in Pull Requests |
| Authors | Kowshik Chowdhury, Dipayan Banik, K M Ferdous, Shazibul Islam Shamim |
| Year | 2026 |
| Venue / Source | MSR 2026 / arXiv |
| DOI / arXiv | 10.1145/3793302.3793614 / arXiv:2604.03196 |
| Artifact | Figshare analysis code and datasets |

```bibtex
% TODO: Add checked ACM BibTeX.
```

## One-Sentence Summary

> P27 shows that code review agent-only pull requests have substantially lower merge rates and higher abandonment than human-only reviews, and that many abandoned CRA-only PRs contain mostly low-signal automated feedback.

## Main Contribution

The paper challenges optimistic industry claims that code review agents can handle most PRs without human involvement. It empirically analyzes reviewer composition and the signal quality of code review agent comments, linking these signals to merge and abandonment outcomes.

## Dataset / Study Context

| Field | Value |
|---|---|
| Source dataset | AIDev PRReviewComment data from HuggingFace |
| Raw review comments | 19,450 PR review comments |
| Analytical PRs | 3,109 unique PRs after filtering for actual code review agents |
| Core comparison subset | 2,456 PRs in `Commented` review state |
| Closed CRA-only subset for signal analysis | 98 PRs |
| Reviewer types | CRA-only, human-only, Mixed(CRA), Mixed(Human), Mixed |

## Method

| Component | Details |
|---|---|
| Reviewer composition | Classifies PRs by whether comments are from humans, CRAs, or mixed groups. |
| Outcome labels | Merged, Closed/abandoned, Stalled. |
| Statistical test | Chi-squared test between reviewer type and PR outcome. |
| Signal-to-noise | Tier 1 critical signals + Tier 2 important signals divided by total comments. |
| Signal coding | Keyword-based framework plus open coding; Cohen’s kappa = 0.75. |

## Key Findings

| Finding | Summary |
|---|---|
| F1 | CRA-only reviewed PRs appear only in the `Commented` condition; CRAs do not independently approve/dismiss/request changes. |
| F2 | CRA-only PR merge rate is 45.20%, compared with 68.37% for human-only PRs. |
| F3 | CRA-only PR abandonment/closure rate is 34.88%, compared with 21.60% for human-only PRs. |
| F4 | Reviewer type and PR outcome are significantly associated: chi-square = 83.0319, p < 0.001. |
| F5 | Mixed(Human) PRs reach 67.99% merge rate; Mixed(CRA) reaches 63.25%, suggesting human involvement improves outcomes. |
| F6 | Among 98 closed CRA-only PRs, 60.2% fall into the 0–30% signal range. |
| F7 | 12 of 13 CRAs have average signal ratios below 60%. |
| F8 | Specialized/narrow agents appear more promising than general-purpose agents, but evidence is limited by small counts. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Merge outcome | High | Compares reviewer composition. |
| Abandonment | High | Closed but unmerged PRs. |
| Signal-to-noise | High | Central comment-quality metric. |
| Actionability | Medium / High | Approximated through Tier 1 and Tier 2 signals. |
| Human oversight | High | Human involvement linked to better outcomes. |
| Review composition | High | CRA-only vs human-only vs mixed. |
| Causality | Low | Correlation, not causal proof. |

## Problematic Comment / Review Types

- Low-signal CRA comment.
- Noisy automated feedback.
- Generic or non-actionable CRA comment.
- High-volume low-value comment set.
- CRA-only review with no human decision authority.
- Feedback that increases cognitive load without a clear improvement path.
- General-purpose CRA review where a narrow specialized checker would be more suitable.

## Context-Quality Evidence

P27 suggests that code review comments should be evaluated not only by correctness but by their **signal density** and their downstream workflow effect. A comment stream with low actionable signal can increase abandonment even if the agent is technically present in the workflow.

## Trade-off Extraction

| Strategy / Signal | Benefit | Risk / Cost |
|---|---|---|
| CRA-only review | Scales review coverage and early feedback. | Lower merge rate, higher abandonment, noisy feedback. |
| Human-only review | Higher merge outcome and contextual judgment. | More human time and review load. |
| Mixed review | Balances automation with human judgment. | Needs coordination and clear responsibility. |
| Signal-to-noise metric | Interpretable proxy for actionable feedback. | Keyword/open-coding heuristic may miss implicit useful comments. |
| Narrow specialized CRAs | Potentially higher precision. | Lower coverage and domain-specific setup. |

## Relevance to Our Paper

P27 strongly supports the claim that AI review should not be evaluated by comment presence alone. We need outcome-aware and signal-aware evaluation: merge rate, abandonment, human oversight, and actionable signal density.

## Limitations from Our Perspective

- Uses AIDev/GitHub data; may not generalize to enterprise workflows.
- Signal-to-noise is keyword-based and may miss semantic usefulness.
- Correlation does not prove CRAs caused abandonment.
- Only 98 closed CRA-only PRs for signal analysis.
- PR outcome is influenced by many factors beyond review comments.

## Follow-up TODOs

- [ ] Add signal-to-noise ratio to evaluation dimensions.
- [ ] Add CRA-only abandonment and human oversight to workflow synthesis.
- [ ] Add low-signal CRA comments to problematic-comment taxonomy.
- [ ] Update `matrices/cross-paper-synthesis.md` with P27 evidence.
