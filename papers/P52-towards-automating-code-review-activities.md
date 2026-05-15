# P52 — Towards Automating Code Review Activities

## Metadata

- **ID:** P52
- **Title:** Towards Automating Code Review Activities
- **Authors:** Rosalia Tufano, Luca Pascarella, Michele Tufano, Denys Poshyvanyk, Gabriele Bavota
- **Year:** 2021
- **Venue:** IEEE Xplore / ICSE 2021
- **Official URL:** https://ieeexplore.ieee.org/abstract/document/9402025/
- **DOI:** TODO: extract from IEEE metadata
- **arXiv:** 2101.02518
- **Drive PDF:** https://drive.google.com/file/d/1X6BiupUKfz7raX9xn1Rkg_skyirno5fF
- **Drive PDF filename:** P52_towards_automating_code_review_activities.pdf
- **BibTeX key:** `p52_tufano2021_automating_code_review_activities`

## Status

- **Review status:** Deep read completed
- **Verification status:** Official IEEE Xplore page verified from user-provided link; Drive PDF available and read; DOI still needs extraction.
- **Priority:** High

## One-Sentence Takeaway

This paper is a key pre-LLM/early-DL automation baseline: it shows that code review automation was motivated by reducing manual review cost, but also explicitly avoids replacing developers because review has knowledge-sharing value.

## What the Paper Does

Tufano et al. make a first step toward partially automating code review activities using transformer-based models. They study two related tasks:

1. **Contributor-side automation**: given code submitted for review, generate a revised version of the code that implements changes a reviewer might request.
2. **Reviewer-side automation**: given submitted code and a natural-language reviewer comment, generate revised code that implements the comment.

The paper frames automation as assistance, not replacement. This is important for our paper because we also argue that evaluation should preserve useful human-review value rather than blindly optimize automation.

## Motivation and Framing

The paper starts from the observation that code review improves code quality and reduces bug likelihood, but it is costly because it requires developer time and context switching. It cites evidence that developers spend substantial time reviewing code and that large industrial projects may process thousands of reviews per month.

The authors' stated long-term goal is to reduce review cost by partially automating time-consuming review activities. However, they explicitly say that the goal is **not** to replace developers. They note that complete automation is unrealistic and would also remove one of the benefits of code review: knowledge sharing among developers.

This distinction is directly useful for our paper:

- automation should support reviewers and authors;
- human review value includes knowledge sharing;
- evaluation should measure more than whether automation can produce a syntactically plausible output.

## Dataset and Mining Pipeline

The authors mine code review data from GitHub and Gerrit. They collect review rounds containing:

- code submitted for review;
- reviewer comments linked to code lines;
- revised code submitted after the review round.

They focus on Java methods. Submitted and revised methods are abstracted to reduce vocabulary size, following prior neural machine translation work on source code.

The core training data is built from triplets:

```text
submitted method + reviewer comment -> revised method
```

and pairs:

```text
submitted method -> revised method
```

The final dataset contains 17,194 triplets and corresponding pairs.

## Noise Filtering and Data Quality

The paper includes a useful discussion of noisy review comments. Not all review comments linked to code are likely to trigger code changes. Examples include approval comments, thanks, clarification requests, requests for tests, and comments that refer to previous discussion.

The authors first attempted machine-learning classification of relevant vs irrelevant comments, but then used simpler keyword-based heuristics because they achieved slightly better precision for identifying relevant comments.

The final heuristic precision is around 93% for classifying relevant comments.

This matters for our paper because it shows that **dataset construction is already a mitigation problem**. The evaluation of generated review comments depends heavily on whether the mined review signal actually represents an actionable code-change request.

## Evaluation Setup

The paper evaluates the two models using:

- exact/perfect prediction counts;
- BLEU-4;
- normalized Levenshtein distance;
- qualitative analysis of perfect and non-perfect predictions.

For the contributor-side task, the model generates the exact revised code in 3% to 16% of cases depending on beam size.

For the reviewer-side task, where the model also receives the reviewer comment, the model generates the exact revised code in 12% to 31% of cases depending on beam size.

The reviewer comment substantially improves performance. This is useful evidence that natural-language review context can help automation, but does not solve the task.

## Qualitative Findings

The qualitative analysis is especially useful for our paper because it moves beyond aggregate metrics.

For the contributor-side model, perfect predictions include:

- method visibility changes;
- readability improvements;
- variable type changes;
- code removal;
- method invocation changes;
- exception-handling changes;
- inheritance-related changes;
- concurrency-related changes;
- some bug-fixing changes.

For the reviewer-side model, the reviewer comment helps the model learn some additional change types, such as:

- simplifying if conditions;
- removing unneeded null checks;
- modifying return types or values;
- modifying thrown exceptions;
- using try-with-resources;
- removing concurrency locks;
- changing boolean values;
- adding missing returns.

The paper also reports that some non-perfect predictions are still meaningful and semantically acceptable, even when they differ from the developer's actual change. This is important for our critique of exact-match evaluation: exact match can undercount useful outputs.

## Threats and Limitations

The paper itself identifies several limitations relevant to our work:

1. **Noisy comments remain** despite filtering.
2. **BLEU and Levenshtein can be misleading** because generated code is often close to the input code.
3. **Manual qualitative analysis is subjective**, though mitigated by multiple authors.
4. **External validity is limited** because the study focuses on Java.
5. The approach is still not ready for real developer use.

These limitations support our argument that evaluation needs multiple dimensions, including output correctness, usefulness, dataset quality, and cost/effort.

## Relevance to Our Paper

### Background

P52 helps show that code review automation predates the current LLM wave and was originally motivated by reducing review effort and cost. It also supports the idea that automation should be framed as assistance rather than replacement.

### Related Work

P52 is an important baseline for early DL-based code review automation. It should appear in the cluster on automated code review generation and review-comment-to-code tasks.

### Framework

P52 supports several framework dimensions:

- **cost/human effort**: automation is motivated by reducing manual review cost;
- **support vs replacement**: automation should preserve the knowledge-sharing value of review;
- **context usefulness**: reviewer comments improve code-generation performance;
- **metric limitations**: exact-match and BLEU do not fully capture meaningful outputs;
- **data quality**: mined review comments contain noise and require filtering.

### Taxonomy

P52 provides early categories of code changes that automation can or cannot handle. These categories can help seed our problematic-comment taxonomy, especially around:

- actionable vs non-actionable review comments;
- comments that trigger code changes vs comments that do not;
- valid vs noisy mined review comments;
- simple local changes vs complex/context-dependent changes.

## Concrete Claims We Can Reuse

- Code review automation is motivated by high review cost and developer context switching.
- Code review automation should support developers, not fully replace them, because review also supports knowledge sharing.
- Reviewer natural-language comments can improve the ability of a model to generate revised code.
- Exact-match evaluation can miss meaningful outputs that differ from the developer's actual implementation.
- Data mined from review systems contains noisy comments that may not correspond to actionable code-change requests.
- Qualitative analysis is necessary to understand what kinds of changes a model can actually automate.

## Connection to Our Core Argument

P52 supports the historical and technical background of our paper. It shows that the field has already moved beyond simple offline scores by using qualitative analysis to inspect successful and failed predictions. It also gives us evidence for a key trade-off: automation can reduce cost, but careless automation or evaluation can undermine human-review value such as knowledge sharing, understanding, and meaningful feedback.

## Limitations of Using This Paper

- It focuses on generating revised code, not directly on generated review comments shown to reviewers.
- It uses Java method-level data, limiting generalizability.
- It predates recent general-purpose LLMs and more advanced RAG/context-aware review systems.
- It does not provide a full workflow evaluation with developers.

## Reading Outcome

- **Use in Introduction:** already useful for pre-LLM/early-DL automation framing.
- **Use in Background:** high priority.
- **Use in Related Work:** high priority.
- **Use in Taxonomy:** medium priority.
- **Use in Framework:** high priority for cost, data quality, and metric-limitations arguments.
