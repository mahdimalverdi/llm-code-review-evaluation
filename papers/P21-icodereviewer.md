# P21 — iCodeReviewer: Improving Secure Code Review with Mixture of Prompts

> [!NOTE]
> Compact v2 analysis. P21 is important for our secure-code-review, routing, prompt-specialization, and production-evaluation arguments because it defines secure code review as category + location + comment generation, uses a mixture-of-prompts architecture to balance precision and coverage, and evaluates helpfulness with I/H/M/U plus production acceptance rates.

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
| Year | 2025 / arXiv preprint |
| Venue / Source | arXiv |
| DOI / arXiv | arXiv:2510.12186; DOI not verified |
| Publication type | Industrial secure-code-review system + production evaluation |
| Artifact | Not verified; internal company deployment |

```bibtex
% TODO: Add checked arXiv BibTeX / final venue metadata if available.
```

## One-Sentence Summary

> P21 proposes iCodeReviewer, a secure code review system that routes code features to specialized prompt experts for CWE issue identification, localization, and review generation, improving security issue F1, localization accuracy, review helpfulness, and production acceptance rates.

## Main Contribution

The paper shifts LLM-based code review from generic comment generation to structured secure review: `program -> (category, location, comment)`. It uses a mixture-of-prompts architecture with feature extraction, prompt expert routing, issue identification, and review generation.

## Our Research Questions

| RQ | Relevance |
|---|---|
| RQ1 — problematic comments | High. Adds false positives, false negatives, hallucinated CWE reports, wrong locations, misleading security comments, and missing high-severity issues. |
| RQ2 — context quality | Very high. Uses AST features, symbol tables, lightweight type/taint/value inference, dynamic context retrieval, and expert-specific prompts. |
| RQ3 — evaluation dimensions | Very high. Evaluates issue identification, localization, I/H/M/U, I-Score/IH-Score/M-Score, and production acceptance rate. |
| RQ4 — trade-offs | Very high. Routing reduces false positives but risks missed issues; expert prompts improve coverage but add maintenance and routing complexity. |
| RQ5 — framework design | High. Supports secure-review-specific evaluation, routing trade-offs, and multi-goal review output. |

## Dataset / Study Context

| Field | Value |
|---|---|
| Dataset | Internal company secure code review dataset |
| Positive samples | 345 programs with real-world security issues detected by developers |
| Benign samples | 337 benign programs confirmed by developers as false positives |
| Languages | 360 C/C++, 181 Java, 101 Python, 40 Shell programs |
| Categories | Memory security, number processing, sensitive information exposure, DoS attack, injection, benign |
| CWE coverage | 38 prompt experts covering multiple CWE families |
| Production evaluation | Two production lines; acceptance rates measured before/after deployment |
| Data availability | Private/internal |

## Method

| Phase | Description |
|---|---|
| Phase I — Feature Extraction | Parses code with tree-sitter, builds symbol table, extracts API, statement, expression, and special-type features. |
| Phase II — Prompt Expert Routing | Activates only prompt experts whose suspicious entities/operations match code features, with context-free and context-sensitive matching. |
| Phase III — Issue Identification | Runs activated dynamic prompt pipelines; uses analysis prompts and determination prompts. |
| Phase IV — Review Generation | Aggregates confirmed issues and generates review comments with categories, locations, descriptions, explanations, and severity prioritization. |

## Prompt Expert Design

- Prompt experts are designed by senior developers for specific security issues.
- Prompt pipelines can include value inference, type inference, value-check inference, taint-variable inference, data/control-flow path inference, and call-relationship inference.
- Complex security issues can use multiple-proposition determination to decompose logic and reduce hallucinated binary judgments.

## Evaluation Method

| Dimension | Metric / Evidence |
|---|---|
| Security issue identification | Multi-class weighted precision, recall, F1 |
| Localization | Accuracy; location is correct if within distance 1 from ground truth |
| Comment helpfulness | Instrumental, Helpful, Misleading, Uncertain categories |
| Comment scores | I-Score, IH-Score, M-Score |
| Production value | Acceptance rate before/after deployment in two production lines |
| Ablation | Remove analysis prompts, multiple propositions, and prompt experts |

## Key Findings

| Finding | Summary |
|---|---|
| F1 | iCodeReviewer achieves 63.98% F1 for security issue identification, outperforming the best baseline by 32.11%. |
| F2 | iCodeReviewer achieves 47.58% localization accuracy, outperforming the best baseline by 26.51%. |
| F3 | Static analyzers have high precision but extremely low recall in this dataset. |
| F4 | Generic LLM prompting has higher recall but produces false positives and wrong locations. |
| F5 | iCodeReviewer achieves I-Score 53.94%, IH-Score 59.70%, and M-Score 40.30%, best among compared approaches. |
| F6 | Production acceptance rises to 84% for C/C++ and 71% for Java in production line #1. |
| F7 | In production line #2, improvement is about 36.84%, but domain specificity still limits performance. |
| F8 | Removing prompt experts drops F1 from 63.98% to 47.17%, showing prompt experts are the key component. |
| F9 | Removing multiple-proposition answers reduces localization accuracy, showing decomposed reasoning helps location quality. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Technical correctness | High | Security category identification and localization. |
| Relevance | High | Activated experts are routed by code features. |
| Grounding | High | Output includes CWE category and location. |
| Localization | Very high | Dedicated localization metric. |
| Helpfulness | High | I/H/M/U categories. |
| Misleadingness | High | M-Score captures misleading comments. |
| False positives | High | Central motivation and metric implication. |
| False negatives / coverage | High | Central motivation and recall metric. |
| Actionability | Medium / High | Comments include category, location, and description. |
| Production usefulness | High | Acceptance rate in production lines. |
| Cost/latency | Medium / Low | Routing reduces unnecessary prompts, but no detailed latency/cost numbers. |
| Maintainability | Medium | New prompt experts must be designed for new security issues. |

## Problematic Comment / Review Types

- Hallucinated security issue.
- False-positive CWE report.
- False-negative/missed security issue.
- Wrong-location security comment.
- Misleading comment that reports a false positive or claims no issue.
- Generic non-security review comment for security-critical code.
- Helpful but not fully accurate security concern.
- Uncertain comment pointing to another possible security issue.
- Severity-prioritization error.

## Context-Quality Evidence

P21 is strong evidence that secure code review needs structured and issue-specific context. Instead of sending all possible CWE categories to the LLM, iCodeReviewer extracts concrete program features and activates only applicable prompt experts. Context quality here means that the prompt is not only longer or more informed; it is routed, issue-specific, feature-grounded, and security-category-aware.

## Trade-off Extraction

| Strategy | Benefit | Risk / Cost |
|---|---|---|
| Prompt expert routing | Reduces false positives by avoiding irrelevant security checks. | Wrong routing can miss relevant experts and create false negatives. |
| Multiple prompt experts | Improves coverage across CWE families. | Requires expert design and maintenance. |
| Analysis prompt pipelines | Simulate reviewer reasoning and improve coverage. | More LLM calls and prompt complexity. |
| Multiple-proposition determination | Reduces hallucinated direct judgments and improves localization. | Requires careful proposition design. |
| Lightweight static analysis | Grounds routing in code features and reduces hallucination. | Not sound/complete; unknown properties are left to LLM. |
| Production acceptance rate | Captures practical value. | Bundles correctness, trust, severity, and workflow factors. |
| I/H/M/U categories | Captures usefulness and misleadingness beyond BLEU. | Still subjective and project/context-dependent. |

## Relevance to Our Paper

P21 should be used as a key source for secure-code-review evaluation and routing-based mitigation. It directly supports our argument that code review evaluation should include category, location, helpfulness, misleadingness, acceptance, false-positive/false-negative balance, and domain-specific context quality.

## Limitations from the Paper’s Own Perspective

- Human evaluation of review comments is subjective.
- Only Qwen-2.5 is used as the base LLM due to company policy and computation budget.
- Generalization to other companies may require new prompt experts.
- Existing security issues are general CWE issues, but company-specific issue coverage may differ.

## Limitations from Our Perspective

- Private internal dataset limits reproducibility.
- Acceptance rate is useful but not a pure correctness metric.
- Production deployment lasts one week; longer-term trust/retention effects are not deeply measured.
- Prompt expert maintenance cost is not quantified.
- Routing false negatives are possible but not deeply decomposed.
- No direct useful-feedback preservation metric for deactivated experts.
- Cost/latency per review is not reported in detail.

## Extracted Evidence for Our Framework

| Argument Need | Evidence |
|---|---|
| Secure review needs structured output | P21 evaluates category, location, and comment separately. |
| Filtering/routing has trade-offs | Routing reduces false positives but can miss experts. |
| Helpfulness needs richer metrics | I/H/M/U and M-Score distinguish helpful vs misleading comments. |
| Production proxies matter | Acceptance rate shows practical usefulness but needs proxy-validity caution. |
| Context quality is issue-specific | AST features and prompt experts create targeted security context. |
| Domain expertise matters | Prompt experts are designed by senior developers. |

## Follow-up TODOs

- [ ] Verify arXiv BibTeX and whether final venue exists.
- [ ] Add secure-review category/location evaluation to `synthesis/evaluation-dimensions.md`.
- [ ] Add routing-vs-coverage trade-off to `synthesis/trade-off-framework.md`.
- [ ] Add hallucinated CWE, wrong-location security comments, and misleading security comments to taxonomy.
- [ ] Add feature-grounded prompt routing to `synthesis/context-quality.md`.
- [ ] Update `matrices/cross-paper-synthesis.md` with P21 evidence.
