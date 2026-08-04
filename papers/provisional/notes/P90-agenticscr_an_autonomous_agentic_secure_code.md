# P90 — AgenticSCR: An Autonomous Agentic Secure Code Review for Immature Vulnerabilities Detection

## 1. Identification

- Project ID: `P90` (provisional)
- Citation key: `p90_charoenwet2026_agenticscr_an_autonomous_agent`
- Full reference: Wachiraphan Charoenwet; Kla Tantithamthavorn; Patanamon Thongtanunam; Hong Yi Lin; Minwoo Jeong; Ming Wu. “AgenticSCR: An Autonomous Agentic Secure Code Review for Immature Vulnerabilities Detection.” FSE 2026; arXiv:2601.19138v1.
- DOI/URL: `https://arxiv.org/abs/2601.19138v1`
- Review date: 2026-08-04
- Source/database: arXiv/full-text screening
- Selection stage: included for reconciliation; canonical corpus integration pending
- Duplicate or companion publication: ACM DOI is placeholder; verify final record.

## 2. Screening

- Decision: `Include`
- Relevance: `High`
- Decision rationale: Directly evaluates an agentic secure-review system for immature, context-dependent vulnerabilities at pre-commit stage against static LLM and SAST baselines.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: taxonomy / annotation protocol / mitigation design / trade-off framework
- Exact inclusion criterion: Core inclusion: secure review, vulnerability detection, false-positive mitigation, and context-aware evaluation.

## 3. Study overview

- Purpose: Detect and explain immature vulnerabilities in small pre-commit changes before they become mature PR-level defects.
- Research questions: RQ1 overall localization/detection/explanation performance; RQ2 vulnerability-type performance; RQ3 contributions of SAST/CWE semantic memory and guidelines.
- Method: Detector–validator agentic architecture with repository tools, security-focused semantic memory, SAST rules, CWE tree, and iterative validation.
- Evaluated system/artifact: AgenticSCR built on RovoDev CLI and Claude Sonnet 4 (2025-05-14); detector finds/localizes/explains, validator filters false positives.
- Dataset/benchmark: SCRBench: 144 pre-commit changes from 107 CVEs, 92 repositories, 33 CWE types, and three languages; human-verified line-level labels.
- Input context: Git repository, diff-centric changes, tools, CodeQL/SAST rules, CWE knowledge, secure-review guidelines, and intermediate traces.
- Main findings: AgenticSCR yields 17.5% correct localized/relevant/type-valid comments, at least 153% relative improvement over static LLM baseline, with 2–5× fewer comments; strongest for injection/authentication and weakest for control/information categories.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | AgenticSCR generates fewer but more relevant, localized, correctly typed comments than static LLM/SAST baselines; Table 2 reports 17.5% overall correct comments. | Reported | Section 4 |
| RQ2 | Injection and authentication achieve 23.4%/21.4% correct comments; information 6.2%, control 0%. | Reported | Section 4 |
| RQ3 | SAST rules add 5.7 percentage points over base; CWE tree adds 4.5 points; combined semantic memory improves validation and false-positive control. | Reported | Section 4 |
| RQ4 | Security memory and validation trade broad candidate discovery against noise; guideline-only augmentation can reduce performance. | Inferred | Section 4 |
| RQ5 | Human-verified line labels, CVE history, and judge validation support evaluation, but domain/business context may remain unavailable. | Reported limitation | Sections 4–5 |
| RQ6 | Directly supports agentic, security-grounded review for early-stage vulnerabilities. | Inferred | Sections 1–5 |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Immature vulnerability miss | Latent/context-dependent weakness in incremental pre-commit change not detected. | Target failure | Sections 1–2 |
| Invalid security warning | Candidate comment lacks genuine CWE-grounded security issue. | Mitigated failure | Section 3 |
| Context gap | Issue requires repository/business/dependency context unavailable to agent. | Reported limitation | Sections 3, 5 |
| CWE/type error | Agent identifies code concern but assigns wrong vulnerability category. | Evaluation failure | Section 4 |
| Alert fatigue | Excessive false-positive comments cause developers to ignore security checks. | Motivation/failure | Sections 1, 3 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Localization | Correct vulnerable line identified. | Included in 17.5% combined success. | Section 4 |
| Detection/relevance | Comment corresponds to genuine immature vulnerability. | Agentic comments substantially fewer and less noisy. | Section 4 |
| Type explanation | Predicted CWE/high-level vulnerability type is valid. | Four of five types outperform baselines. | Section 4 |
| False positives | Irrelevant/invalid security comments. | Agentic produces 71.3–85% fewer than comparative systems. | Section 4 |
| Judge validity | GPT-4.1 judge on comment quality. | F1 0.86, precision 0.88, recall 0.86. | Validity section |

## 7. Mitigation and trade-offs

- Mitigation family: Detector–validator agents with security semantic memory and repository tool use.
- Intervention point: Pre-commit secure review before code is committed.
- What it reduces: Static-tool noise, generic LLM hallucination, and missing repository/security context.
- Useful feedback potentially lost: Strict validation may filter genuine but novel vulnerabilities; business-context issues remain difficult.
- Coverage effect: Improves correct comments and reduces output volume, but performance varies sharply by CWE type.
- Human escalation effect: Produces explanations/type labels for developers; actual adoption/escalation is not measured.
- Computational/operational cost: Multi-agent tool use, retrieval, and semantic memory increase complexity; latency/dollar cost is not reported.
- New failure modes: Memory bias, wrong CWE validation, over-filtering, and context gaps.

## 8. Annotation and evaluator validity

- Judge/annotator: SCRBench labels are human verified; baseline outputs are standardized by warning line, relevance, and type; GPT-4.1 judges review quality.
- Rubric: Line localization, vulnerability relevance, and valid CWE/high-level type; judge assesses comment quality.
- Agreement/reliability: GPT-4.1 judge F1 0.86/precision 0.88/recall 0.86; human annotation agreement details are not prominent in extracted text.
- Validity checks: Historical CVEs, pre-commit filtering, manual line verification, four baseline families, component ablations, and judge validation.
- Possible bias: Curated public CVEs, three languages, chosen SAST rules, model/scaffold versions, and missing business context.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Agent, task, and security goal are explicit. |
| Q2 | 2 | SCRBench size, CVEs, repositories, languages, and CWEs reported. |
| Q3 | 2 | Agent/model/tools and baselines specified. |
| Q4 | 2 | Localization, relevance, type, false positives, and judge metrics explicit. |
| Q5 | 2 | Line-level/CWE rubric is defined. |
| Q6 | 1 | Judge metrics reported; human agreement unclear. |
| Q7 | 2 | Baselines, ablations, and filtering are included. |
| Q8 | 1 | Curated CVEs and missing business context limit validity. |
| Q9 | 2 | Detector–validator and semantic memory interventions are tested. |
| Q10 | 1 | Complexity is evident; cost/latency absent. |
| Q11 | 2 | Context, dataset, memory, and generalization limits discussed. |
| Q12 | 2 | Direct secure code-review relevance. |

- Total: `21/24` provisional
- Quality interpretation: Strong controlled secure-review evidence, with cost and external-validity limitations.

## 10. Review-process reliability and bias

- Missing data: Developer usefulness, long-term adoption, cost/latency, recall over benign changes, and broader language coverage are not established.
- Publication-bias concern: Not assessed; curated vulnerability dataset and selected baselines may favor the system.
- Selection uncertainty: Included by full-text screening; final FSE metadata should be reconciled.
- Extraction uncertainty: Moderate due to metric normalization and limited contextual setting.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Pending final-version reconciliation.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Shows that agentic repository exploration plus security memory can produce fewer, more relevant pre-commit security comments than static LLM/SAST baselines.
- What the paper does not establish: It does not establish complete vulnerability recall, low operational cost, or developer acceptance.
- Research gap supported: Secure review evaluation should combine line localization, vulnerability grounding, false-positive burden, CWE coverage, and pre-commit latency.
- Candidate synthesis claims: Detector–validator structure and authoritative security memory can improve precision, but may trade coverage for defensibility and remain vulnerable to context gaps.
- Follow-up verification needed: Inspect SCRBench labels, exact Table 2 metrics, and human/judge agreement protocol.
