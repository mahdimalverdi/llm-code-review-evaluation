# P92 — AILinkPreviewer: Enhancing Code Reviews with LLM-Powered Link Previews

## 1. Identification

- Project ID: `P92` (provisional)
- Citation key: `p92_trakoolgerntong2025_ailinkpreviewer_enhancing_code`
- Full reference: Panya Trakoolgerntong; Tao Xiao; Masanari Kondo; Chaiyong Ragkhitwetsagul; Morakot Choetkiertikul; Pattaraporn Sangaroonsilp; Yasutaka Kamei. “AILinkPreviewer: Enhancing Code Reviews with LLM-Powered Link Previews.” arXiv:2511.09223v1, 2025.
- DOI/URL: `https://arxiv.org/abs/2511.09223v1`; tool: `https://github.com/c4rtune/AILinkPreviewer`
- Review date: 2026-08-04
- Source/database: arXiv/full-text screening
- Selection stage: included for reconciliation; canonical corpus integration pending
- Duplicate or companion publication: Verify final metadata.

## 2. Screening

- Decision: `Include`
- Relevance: `Medium-High`
- Decision rationale: Improves review context by summarizing hyperlinks embedded in PRs; directly evaluates reviewer usability but not comment correctness.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: context quality / workflow mitigation / trade-off framework
- Exact inclusion criterion: Context augmentation for code review workflows.

## 3. Study overview

- Purpose: Reduce context switching by providing contextual previews of PR links inside the review interface.
- Research questions: Compare contextual LLM, non-contextual LLM, and metadata snippets on summary quality and perceived usability.
- Method: Chrome extension plus automatic summarization evaluation on 50 engineered repositories and a seven-person usability study (five submitted usable evaluations).
- Evaluated system/artifact: AILinkPreviewer extracts PR title/description/comments and linked-page content, then uses DeepSeek to generate a context-sensitive preview.
- Dataset/benchmark: Top 50 active/mature GitHub repositories; links filtered by descriptive label length, with eight words reducing trivial-label false positives to 15.07%.
- Input context: Link body alone, link body plus PR metadata/position, or metadata-based snippet.
- Main findings: Contextual summaries outperform alternatives on BLEU/BERTScore/compression, but most participants prefer non-contextual summaries; ease-of-use average is 4.4/5.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Contextual summaries preserve more PR/link information than isolated or metadata-only summaries. | Reported | Sections III–IV |
| RQ2 | Link previews reduce need to leave PR page and may reduce cognitive switching; review correctness is not tested. | Design/limited evidence | Sections I–III |
| RQ3 | Context is supplied based on hyperlink location in PR description, comment, or review comment. | Reported | Section III |
| RQ4 | Automatic metric quality and perceived usability diverge: non-contextual summaries are preferred despite lower scores. | Reported trade-off | Section IV |
| RQ5 | Seven participants evaluate preference/ease; sample is small and only five submitted complete results. | Reported limitation | Section IV |
| RQ6 | Supports retaining link context in automated review pipelines, but not direct comment-generation quality. | Inferred | Sections I, IV |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Context omission | Link content discarded from automated review/summarization. | Motivation | Sections I–II |
| Context-switch burden | Reviewer must open and interpret many links manually. | Workflow problem | Sections I, III |
| Trivial link label | Link label lacks enough descriptive content for meaningful reference. | Dataset filtering | Section IV |
| Metric–usability mismatch | Higher lexical/semantic scores do not imply user preference. | Reported limitation | Section IV |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Summary similarity | BLEU, ROUGE-1/2, METEOR, BERTScore, TF-IDF similarity. | Contextual method consistently best. | Section IV, Table I |
| Compression/readability | Compression ratio and Flesch Reading Ease. | Metadata snippets slightly more readable but less informative. | Section IV |
| User preference | Preferred preview method across PR examples. | Most users preferred non-contextual summaries. | Section IV |
| Ease of use | 1–5 Likert rating. | Average 4.4/5. | Section IV |

## 7. Mitigation and trade-offs

- Mitigation family: In-interface context augmentation and link summarization.
- Intervention point: During PR review, before a developer opens an external link.
- What it reduces: Context switching and loss of linked issue/documentation information.
- Useful feedback potentially lost: Summarization can omit details or misrepresent linked evidence; technical review correctness is not evaluated.
- Coverage effect: Retains link-level context but does not measure issue/defect coverage.
- Human escalation effect: Not measured.
- Computational/operational cost: Requires link retrieval and DeepSeek inference; latency/cost is not reported.
- New failure modes: Summary hallucination, stale/blocked links, privacy/security exposure, and user preference for less contextual output.

## 8. Annotation and evaluator validity

- Judge/annotator: Link labels/references provide automatic comparison targets; seven participants provide usability feedback.
- Rubric: NLP similarity/readability/compression plus preference and Likert ease-of-use.
- Agreement/reliability: No inter-rater reliability reported; usability sample is very small.
- Validity checks: Three-method comparison, 50-repository selection, link-label length filtering, and mixed automatic/human evaluation.
- Possible bias: Reference label may not represent ideal summary; engineered repositories and small participant sample limit generalization.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Tool and context problem are explicit. |
| Q2 | 2 | 50 repositories and link-filter procedure reported. |
| Q3 | 2 | Three approaches and extension workflow described. |
| Q4 | 2 | Similarity, readability, compression, preference, and ease metrics explicit. |
| Q5 | 1 | Link labels are a weak summary reference. |
| Q6 | 0 | No reliability statistic. |
| Q7 | 2 | Automatic and user comparisons included. |
| Q8 | 1 | Seven-person usability sample and label-reference limits. |
| Q9 | 2 | Context-preview intervention explicit. |
| Q10 | 1 | Runtime cost not quantified. |
| Q11 | 2 | Metric–preference mismatch and sampling limits discussed. |
| Q12 | 1 | Review-context relevance is direct, but comment quality is indirect. |

- Total: `18/24` provisional
- Quality interpretation: Useful context-augmentation prototype with preliminary usability evidence, not a review-quality benchmark.

## 10. Review-process reliability and bias

- Missing data: Review correctness, defect detection, long-term workflow effect, latency, cost, and summary factuality.
- Publication-bias concern: Not assessed; prototype evaluation and small user sample.
- Selection uncertainty: Included as context/workflow evidence; final metadata pending.
- Extraction uncertainty: Moderate due to automatic reference summaries and incomplete user responses.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Pending reconciliation.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Shows that retaining PR hyperlinks and presenting in-place previews can enrich review context and reduce navigation burden.
- What the paper does not establish: It does not establish improved review correctness, comment usefulness, or safe factual summarization.
- Research gap supported: Context augmentation should evaluate factuality and downstream review decisions alongside similarity and usability.
- Candidate synthesis claims: Contextual summaries can score better automatically while being less preferred by users, demonstrating a metric–usability trade-off.
- Follow-up verification needed: Inspect user-study protocol, summary references, and factuality/error analysis.
