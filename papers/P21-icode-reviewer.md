# P21 — iCodeReviewer: Improving Secure Code Review with Mixture of Prompts

> [!NOTE]
> Compact v2 analysis. P21 is important for our trade-off-aware evaluation framework because it defines secure code review as a multi-output task `(category, location, comment)`, combines static feature extraction with LLM prompt experts, and evaluates both objective security issue identification/localization and developer-facing comment usefulness/acceptance.

## Status

- Paper ID: `P21`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup`
- Priority: `High`
- Reading depth: `Read once from PDF`
- Last updated: `2026-05-14`
- Confidence in extraction: `High`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | iCodeReviewer: Improving Secure Code Review with Mixture of Prompts |
| Authors | Yun Peng, Kisub Kim, Linghan Meng, Kui Liu |
| Year | 2025 |
| Venue / Source | arXiv preprint |
| DOI / arXiv | arXiv:2510.12186 |
| Artifact | Not verified; industrial/internal deployment |

```bibtex
% TODO: Add checked arXiv BibTeX.
```

## One-Sentence Summary

> P21 proposes iCodeReviewer, a secure code review system that routes code snippets to specialized prompt experts using static code features, improving security issue identification, localization, generated-comment usefulness, and production acceptance rates.

## Main Contribution

The paper reframes secure code review as a structured task: given a program, output the security issue category, the vulnerable location, and a natural-language review comment. This structured framing allows more objective evaluation than comment generation alone.

## Research Questions of the Paper

| RQ | Summary |
|---|---|
| RQ1 | How effective is iCodeReviewer for security issue identification and localization compared with static analysis, code review models, and prompting baselines? |
| RQ2 | How helpful are the generated review comments in practice? |
| RQ3 | What is the contribution of different iCodeReviewer components? |

## Dataset / Study Context

| Field | Value |
|---|---|
| Dataset | Internal company secure-code-review dataset |
| Positive cases | 345 programs with real-world security issues detected by developers |
| Benign cases | 337 programs confirmed as false positives / benign by developers |
| Languages | C/C++ 360, Java 181, Python 101, Shell 40 |
| Issue categories | Memory security, number processing, sensitive information exposure, DoS attack, injection, benign |
| CWE coverage | 38 prompt experts covering selected CWE categories |
| Production evaluation | Two production lines, one-week deployment window |

## Method

| Component | Role |
|---|---|
| Phase I — Feature extraction | Uses tree-sitter and lightweight code analysis to build a symbol table and extract code features. |
| Phase II — Prompt expert routing | Activates only relevant prompt experts based on suspicious entities/operations and context-sensitive matching. |
| Phase III — Issue identification | Runs dynamic prompt pipelines for specific security issues. |
| Multiple-proposition answers | Decomposes complex security logic into simpler propositions to reduce hallucination and reasoning errors. |
| Phase IV — Review generation | Aggregates confirmed issues, double-checks/ranks them, and generates final review comments with category, location, and explanation. |

## Models / Baselines

| Baseline Type | Systems |
|---|---|
| Static analysis | Cppcheck, Flawfinder |
| Code review models | CodeReviewer, T5-Review |
| Prompting baselines | Qwen-2.5 with instruction prompt; Qwen-2.5 with CWE info; DeepSeek R1 with instruction prompt; DeepSeek R1 with CWE info |
| Main model | Qwen-2.5 72B for iCodeReviewer |

## Evaluation Method

| Output | Metrics / Labels |
|---|---|
| Issue identification | Multi-class weighted precision, recall, F1 |
| Issue localization | Accuracy; correct if predicted location is within distance 1 of ground truth |
| Review comment quality | Instrumental, Helpful, Misleading, Uncertain; I-Score, IH-Score, M-Score |
| Production value | Acceptance Rate in two production lines |
| Ablation | Without analysis prompts, without multiple propositions, without prompt experts |

## Key Findings

| Finding | Summary |
|---|---|
| F1 | iCodeReviewer achieves the best issue-identification F1: 63.98%. |
| F2 | iCodeReviewer achieves issue-localization accuracy of 47.58%. |
| F3 | It outperforms the best baseline by 32.11% in issue identification and 26.51% in localization. |
| F4 | iCodeReviewer achieves I-Score 53.94%, IH-Score 59.70%, and M-Score 40.30%. |
| F5 | Instruction prompts can achieve higher F1 but produce more misleading information, showing a metric-quality trade-off. |
| F6 | Production acceptance reaches 84% for C/C++ and 71% for Java in one production line. |
| F7 | Prompt experts are the most important component; removing them drops F1 from 63.98% to 47.17%. |
| F8 | Multiple-proposition prompting improves identification and localization for complex security issues. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Technical correctness | High | Issue category and localization give objective labels. |
| Localization | High | Location accuracy is explicitly measured. |
| Security severity/category | High | CWE/category-level detection is central. |
| Comment usefulness | High | I/H/M/U labels and I/IH/M scores. |
| False positives | High | Routing is designed to reduce false positives from hallucination. |
| False negatives / coverage | High | Prompt experts improve coverage across CWE categories. |
| Acceptance/adoption | High | Production acceptance rate is reported. |
| Context quality | High | Feature extraction and context-sensitive routing select relevant prompt experts. |
| Cost/latency | Medium | Parallel prompt experts and routing imply cost trade-offs, but direct cost/latency is not reported. |
| Generalizability | Medium | Internal dataset and selected CWE coverage limit generalization. |

## Problematic Comment / Error Types

- False-positive security issue caused by LLM hallucination.
- False-negative security issue missed by generic prompts or static analyzers.
- Wrong security category / wrong CWE.
- Wrong issue location.
- Misleading security review comment.
- Helpful but not fully accurate/specific comment.
- Uncertain comment that points to a different possible security issue.
- Low-value non-security comment from general code review models.
- Prompt-overcoverage: asking an LLM to check irrelevant CWE categories increases false positives.
- Prompt-undercoverage: fixed prompts miss security issues requiring specialized program-state analysis.

## Context-Quality Evidence

P21 provides strong evidence that context quality can be operationalized through *routing*. Instead of giving the LLM all possible security categories, iCodeReviewer uses lightweight program analysis to extract code features and activates only relevant prompt experts.

Important context-quality mechanisms:

- AST parsing and symbol table construction.
- Type, taint, and value inference used only as lightweight feature support.
- Suspicious entity and suspicious operation matching.
- Context-sensitive dynamic retrieval of relevant external calls.
- Macro expansion to avoid missing security-relevant features.
- Prompt expert selection as context filtering.

## Trade-off Extraction

| Strategy | Benefit | Risk / Cost |
|---|---|---|
| Mixture of prompts | Improves coverage while keeping prompts specialized. | Requires manually designed prompt experts. |
| Prompt routing | Reduces false positives by not asking irrelevant questions. | Router errors can suppress relevant experts and cause false negatives. |
| Lightweight static analysis | Provides precise features without requiring full compilation. | Not sound or complete; may miss hidden context. |
| Multiple propositions | Reduces hallucination and improves complex issue reasoning. | Adds prompt engineering complexity. |
| Production acceptance rate | Captures practical value. | Does not isolate correctness, severity, trust, or convenience. |
| I/H/M/U labels | Better than BLEU for review comment usefulness. | Manual classification is subjective and costly. |

## Relevance to Our RQs

| Our RQ | Relevance |
|---|---|
| RQ1 — problematic comments | High: adds false-positive security comments, misleading comments, wrong category/location, and uncertain security comments. |
| RQ2 — context quality | High: routing based on code features is a concrete context-quality mechanism. |
| RQ3 — evaluation dimensions | Very high: category, location, I/H/M/U, acceptance rate. |
| RQ4 — trade-offs | Very high: precision-vs-coverage, routing false positives vs false negatives, prompt expert coverage vs maintenance. |
| RQ5 — framework design | High: supports structured evaluation for generated reviews beyond natural-language quality. |

## Limitations from the Paper’s Own Perspective

- Human review-comment classification is subjective.
- Generalization to other LLMs is not fully evaluated because the system uses Qwen-2.5 due to company policy and compute constraints.
- Generalization to other companies may require new prompt experts because security priorities differ.

## Limitations from Our Perspective

- Internal/private dataset limits reproducibility.
- Acceptance rate is useful but still a proxy for correctness/usefulness.
- One-week production deployment is relatively short.
- Prompt experts require manual expert design and maintenance.
- Router false negatives are a major risk but are not fully analyzed as useful-feedback loss.
- Security-specific evaluation may not directly transfer to general code review.
- No explicit dollar/token/latency evaluation for multiple prompt experts.

## Extracted Evidence for Our Argument

| Argument Need | Evidence |
|---|---|
| Need for structured evaluation | Secure review is evaluated as category + location + comment, not just comment text. |
| Need for context-quality model | Feature-based prompt routing prevents irrelevant prompt experts and reduces false positives. |
| Need for trade-off-aware evaluation | Instruction prompting has higher F1 in some settings but worse misleading-comment behavior. |
| Need for usefulness labels | I/H/M/U captures comment quality better than BLEU/ROUGE. |
| Need for production proxy caution | Acceptance rate is useful but still not a pure correctness label. |
| Need for maintenance-cost dimension | Prompt experts must be designed and updated by senior developers. |

## Follow-up TODOs

- [ ] Verify arXiv BibTeX.
- [ ] Add mixture-of-prompts and routing to `synthesis/trade-off-framework.md`.
- [ ] Add secure-review structured outputs to `synthesis/evaluation-dimensions.md`.
- [ ] Add wrong category/location and misleading security review to `synthesis/problematic-comment-taxonomy.md`.
- [ ] Add feature-based prompt routing to `synthesis/context-quality.md`.
- [ ] Update `matrices/cross-paper-synthesis.md` with P21 evidence.
