# P101 — Uncovering Systematic Failures of LLMs in Verifying Code Against Natural Language Specifications

> **Provisional intake record.** This is not a canonical paper note.

| Field | Value |
|---|---|
| Project ID | `P101` (provisional) |
| Citation key | `p101_jin2025_uncovering_systematic_failures` |
| Authors | Haolin Jin; Huaming Chen |
| Year | 2025 |
| Source | arXiv |
| arXiv | `2508.12358v1` |
| Screening tier | `core` |
| Reconciliation status | New candidate after initial local matching |
| Metadata status | local_arxiv_metadata |
| Evidence status | Full-text eligibility recorded; extraction not yet completed |

## 1. Identification

- Duplicate or companion publication: The PDF carries ASE’25/2018 placeholder metadata and an invalid DOI; verify the official record before citation.

## 2. Screening
- Decision: `Include`; Relevance: `High`
- Decision rationale: Directly evaluates LLM judgments of code conformance to natural-language specifications, prompt-induced false negatives, and mitigation prompts relevant to automated review.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: evaluator validity / problematic-comment taxonomy / mitigation design

## 3. Study overview
- Purpose: Determine whether LLMs can reliably judge correct code against natural-language requirements without tests, and expose systematic misjudgment patterns.
- Research questions: Baseline conformance reliability (RQ1), prompt-design effects (RQ2), and causes/mitigations for false-negative judgments (RQ3).
- Method: Evaluate GPT-4o, Gemini-2.0-Flash, and Claude-3.5-Sonnet on HumanEval, MBPP, and QuixBugs using direct, explanation, and repair prompts; then test reflective and behavioral-comparison prompts.
- Evaluated system/artifact: LLM code-verification assistant answering whether implementations satisfy requirements.
- Dataset/benchmark: HumanEval, MBPP, and QuixBugs; experiments use correct implementations and RCRR (Requirement-Conformance Recognition Rate) as the primary metric.
- Input context: Natural-language task specification plus code implementation; no test cases or reference implementation are supplied to the model.
- Main findings: Direct-prompt RCRR ranges 52.4–78.0%. GPT-4o falls from 52.4 to 11.0% on HumanEval under the full judgment+explanation+fix prompt. Behavioral Comparison improves GPT-4o to 85.4% on HumanEval, 68.9% MBPP, and 90.0% QuixBugs.

## 4. Evidence mapped to review questions
| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Without tests, models show limited and uneven conformance recognition, with many correct implementations judged non-compliant. | Reported | Sections 3–4.1, Table 1 |
| RQ2 | Adding explanation and repair steps substantially reduces RCRR, often by 20–40 percentage points. | Reported | Section 4.2, Table 1 |
| RQ3 | The main failure is over-correction: reasoning/fix prompts encourage models to assume defects and propose unnecessary changes. | Reported | Section 4.3 |
| RQ4 | Two-Phase Reflective and Behavioral Comparison prompts improve performance by separating requirement understanding from code auditing. | Reported | Section 4.3, Table 2 |
| RQ5 | A plausible explanation or patch is not evidence that the original code was faulty; evaluator outputs can create false defects. | Inferred | Sections 3–5 |
| RQ6 | Code-review evaluation should measure false positives/negatives under prompt variation and verify proposed fixes against requirements. | Inferred | Sections 4–5 |

## 5. Failure and problematic-comment categories
| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| False negative conformance judgment | Correct code is classified as not satisfying the requirement. | Reported failure | Abstract, Section 4.1 |
| Over-correction | Model assumes a defect exists, explains a nonexistent problem, and proposes an unnecessary fix. | Reported failure | Section 4.3 |
| Explanation-induced error | Requiring rationale decreases recognition accuracy compared with direct judgment. | Reported failure | Sections 3–4.2 |
| Premature repair | Mandatory fix step shifts attention toward finding something to patch. | Inferred mechanism | Section 4.3 |
| Specification/code mismatch confusion | Model fails to compare functional obligations and implemented behavior point-by-point. | Target failure | Section 4.3.1 |

## 6. Evaluation dimensions and metrics
| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Conformance recognition | RCRR = correct judgments / correct-code samples. | Direct: GPT-4o 52.4/63.7/62.5 on HumanEval/MBPP/QuixBugs; Claude 78.0/56.9/80.0. | Table 1 |
| Prompt sensitivity | Compare Direct, Direct+Explain, Full; then two mitigation prompts. | Full prompt sharply degrades accuracy; alternatives recover/improve it. | Tables 1–2 |
| False-positive analysis | Inspect incorrect “not satisfied” labels and proposed rationales/fixes. | Over-correction identified as primary factor. | Section 4 |
| Robustness across models | GPT-4o, Gemini-2.0-Flash, Claude-3.5-Sonnet. | Sensitivity differs; all show some degradation with complex prompts. | Sections 3–4 |
| Generalization | Three established Python/code benchmarks. | No production repository or developer-outcome evaluation. | Sections 2–4 |
| Cost/effort | Prompt complexity and additional generation steps. | Compute/API cost and latency are not reported. | Paper-wide |

## 7. Mitigation and trade-offs
- Mitigation family: Two-Phase Reflective Prompt and Behavioral Comparison Prompt.
- Intervention point: Prompt design, requirement decomposition, and verdict formation.
- What it reduces: Over-correction, false-negative conformance judgments, and premature repair suggestions.
- Useful feedback potentially lost: Removing explanation/fix steps may reduce diagnostic detail or actionable repair guidance when a real defect exists.
- Coverage effect: Explicit obligation and behavior comparison can improve functional coverage, but the study does not test repository-level context.
- Human escalation effect: Safer prompts may reduce false alarms, but human review/acceptance is not measured.
- Computational/operational cost: Behavioral/reflective prompts add turns and tokens; no cost or latency data are reported.
- New failure modes: Prompt-specific biases, incomplete obligation extraction, and residual misjudgments despite mitigation.

## 8. Annotation and evaluator validity
- Judge/annotator: Benchmark ground truth is based on correct implementations; LLMs provide judgments, explanations, and fixes.
- Rubric: Binary conformance plus RCRR; error analysis examines whether rationales identify real defects.
- Agreement/reliability: No human annotation or inter-rater agreement is reported.
- Validity checks: Three models, three benchmarks, multiple prompt strategies, and two mitigation designs.
- Possible bias: Correct-code-only emphasis, benchmark distribution, model/version choice, and invalid placeholder publication metadata.

## 9. Quality appraisal
| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Questions and failure phenomenon are explicit. |
| Q2 | 2 | Three established benchmarks and input setting reported. |
| Q3 | 2 | Models and prompt variants described. |
| Q4 | 2 | RCRR and prompt/model comparisons reported. |
| Q5 | 1 | Binary conformance rubric is narrow. |
| Q6 | 0 | No human annotation/agreement protocol. |
| Q7 | 2 | Multiple models, datasets, and prompt ablations. |
| Q8 | 1 | Benchmark-only, correct-code-focused evaluation limits validity. |
| Q9 | 2 | Two mitigation prompts are evaluated. |
| Q10 | 1 | Token/latency/cost absent. |
| Q11 | 2 | Over-correction and prompt sensitivity discussed. |
| Q12 | 2 | Direct evidence concerns code verification/review judgments. |
- Total: `19/24` provisional
- Quality interpretation: Clear evidence of prompt-induced evaluator failure, but limited human/production validation and metadata uncertainty.

## 10. Review-process reliability and bias
- Missing data: Human agreement, false-positive rates on defective code, developer impact, latency, cost, and repository-context performance.
- Publication-bias concern: Small benchmark/model study and author-reported mitigation results.
- Selection uncertainty: Full text available, but venue/DOI metadata are malformed placeholders.
- Extraction uncertainty: Moderate; some detailed results are table-based and the PDF metadata is inconsistent.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Confirm whether this is the ASE’25 version before final bibliography integration.

## 11. Synthesis-ready conclusion
- Contribution to the SLR: Demonstrates that adding explanation and repair instructions can worsen LLM code-conformance judgments through systematic over-correction.
- What the paper does not establish: It does not establish production review impact, robustness on defective implementations, or generalization beyond benchmark programs.
- Research gap supported: Evaluator validation should test prompt sensitivity, false-positive/negative asymmetry, explanation-induced bias, and agreement with human judgments.
- Candidate synthesis claims: More elaborate reasoning prompts are not uniformly beneficial for code review; separating requirement extraction from behavioral comparison can reduce false alarms.
- Follow-up verification needed: Verify official ASE metadata, inspect exact benchmark samples, and evaluate mitigation prompts on both correct and defective code.
