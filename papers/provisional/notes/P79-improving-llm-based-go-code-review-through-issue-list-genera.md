# P79 — Improving LLM-Based Go Code Review through Issue-List Generation and Context Augmentation

## 1. Identification

- Project ID: `P79` (provisional)
- Citation key: `p79_sun2026_improving_llm_based_go_code_re`
- Full reference: Kexin Sun; Yucong Guan; Jiaqi Sun; Hongyu Kuang; Guoping Rong; Dong Shao; He Zhang; Xiaoxing Ma; Christoph Treude. “Improving LLM-Based Go Code Review through Issue-List Generation and Context Augmentation.” arXiv:2606.01859v1, 2026.
- DOI/URL: `https://arxiv.org/abs/2606.01859v1`
- Review date: 2026-08-04
- Source/database: arXiv full-text screening
- Selection stage: included for reconciliation; canonical corpus integration pending
- Duplicate or companion publication: Not reported; verify final metadata.

## 2. Screening

- Decision: `Include`
- Relevance: `High`
- Decision rationale: Directly evaluates generation strategy, context augmentation, review coverage, and downstream code-refinement usefulness.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: taxonomy / annotation protocol / mitigation design / trade-off framework
- Exact inclusion criterion: Core inclusion: LLM code-review generation and context/coverage trade-offs.

## 3. Study overview

- Purpose: Improve review issue discovery without making candidate lists impractical to inspect.
- Research questions: RQ1 issue-list vs. primary-issue review; RQ2 neighboring/LSP/similar co-change context; RQ3 integration and pruning of candidate lists.
- Method: Controlled evaluation on 1,438 Go review instances, using review-text metrics and downstream refinement exact match.
- Evaluated system/artifact: Prompted LLM issue-list review with neighboring, LSP-based semantic, and IR-based similar co-change context; CodeReviewer is a baseline.
- Dataset/benchmark: 1,438 recovered Go review/refinement instances; a manual sample of 100 human comments found 97% centered on one issue.
- Input context: Changed hunk plus optional enclosing function, LSP definitions/references/types, and similar co-modified files. Candidate comments are ranked and optionally merged/pruned.
- Main findings: Best integrated configuration reaches 28.00% RefineEM vs. 17.15% primary/no-context, 15.02% CodeReviewer, and 36.09% human-oracle ceiling; pruning reduces average candidates 7.2→3.1 at top-5 with nearly full benefit.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Listing all potential issues improves downstream refinement over reporting one primary issue: no-context issue-list 21.83% RefineEM vs. primary 17.15%. | Reported | Abstract, Sections IV–V |
| RQ2 | Neighboring + similar co-change context is strongest; semantic context does not always add benefit and can distract. | Reported | Abstract, Section V |
| RQ3 | Merging no-context and context-enhanced candidates improves coverage; refinement-guided pruning controls inspection burden. | Reported | Abstract, Sections III–V |
| RQ4 | Candidate breadth improves coverage but increases verbosity/inspection burden; pruning retains utility with fewer candidates. | Inferred | Sections III, V |
| RQ5 | Human revisions provide the downstream oracle; metrics include RefineEM, RefineBLEU, ReviewBLEU, and ReviewBERT. | Reported | Section IV |
| RQ6 | Context retrieval is useful but non-monotonic: more context can blind the model to issues it would otherwise find. | Inferred | Sections I, V |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Missed secondary issue | Primary-issue prompt omits a human-aligned concern that issue-list generation surfaces. | Reported failure | Sections I, V |
| Irrelevant context distraction | Additional semantic/context blocks reduce focus or fail to improve discovery. | Reported failure | Sections I, V |
| Candidate redundancy/low impact | Multiple comments induce equivalent or no refinement and can be pruned. | Operational category | Section III-C |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Downstream usefulness | RefineEM: candidate induces exact same code change as final human revision. | 28.00% best; human oracle 36.09%. | Abstract, Section IV |
| Review text similarity | ReviewBLEU and ReviewBERT against human comments. | Used as secondary/selection metrics; similarity is not sufficient for usefulness. | Section IV |
| Coverage | Candidate pool contains a comment inducing target refinement. | Issue-list and candidate integration improve coverage. | Sections V-A, V-C |
| Inspection burden | Number of candidate comments, especially top-5. | 7.2→3.1 after pruning with nearly full benefit. | Abstract, Section V |

## 7. Mitigation and trade-offs

- Mitigation family: Issue-list generation, repository context retrieval, candidate integration, and refinement-guided pruning.
- Intervention point: Review generation and candidate ranking before developer inspection.
- What it reduces: Missed secondary concerns caused by forcing a single primary issue and context-insufficient generation.
- Useful feedback potentially lost: Pruning and ranking may remove valid but non-refinement-inducing concerns; human usefulness beyond the target revision is not measured.
- Coverage effect: Improves downstream refinement coverage, with best integrated RefineEM 28.00%.
- Human escalation effect: Not measured; candidate count is used as an inspection proxy.
- Computational/operational cost: LSP/IR retrieval and multiple candidate generation add context and inference cost; monetary cost is not reported.
- New failure modes: Context distraction, redundant candidates, and excessive candidate lists.

## 8. Annotation and evaluator validity

- Judge/annotator: Human final revisions provide the refinement oracle; 100 human comments are manually inspected for issue-list motivation.
- Rubric: Exact-match induced code change, BLEU/BERTScore similarity, and candidate count.
- Agreement/reliability: No inter-annotator statistic is reported for the 100-comment inspection.
- Validity checks: Three-run experiments, McNemar exact tests for significance, human-oracle upper bound, CodeReviewer baseline, and refinement-guided filtering.
- Possible bias: RefineEM favors comments aligned with one final revision and may undercount valid alternatives; Go-only data limits generalization.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Generation/context interventions are explicit. |
| Q2 | 2 | 1,438 Go instances and data recovery are described. |
| Q3 | 2 | Model, context types, baseline, and runs are specified. |
| Q4 | 2 | RefineEM, text metrics, and candidate count are operationalized. |
| Q5 | 2 | Human revision oracle and context construction are defined. |
| Q6 | 0 | No inter-annotator reliability statistic. |
| Q7 | 2 | Ablations, baselines, and statistical testing are included. |
| Q8 | 2 | Human oracle and downstream executable refinement strengthen validity. |
| Q9 | 2 | Issue-list, context augmentation, integration, and pruning are tested. |
| Q10 | 1 | Candidate burden is measured, but monetary cost is not. |
| Q11 | 2 | Non-monotonic context and metric limitations are discussed. |
| Q12 | 2 | Directly evaluates review coverage and downstream usefulness. |

- Total: `21/24` provisional
- Quality interpretation: Strong controlled evidence for coverage/usefulness trade-offs, with limitations from exact-match oracle and Go-only scope.

## 10. Review-process reliability and bias

- Missing data: Human acceptance, comment correctness independent of refinement, recall of all valid issues, and generation cost are not measured.
- Publication-bias concern: Not assessed; results may favor the authors’ prompt/context design.
- Selection uncertainty: Included by full-text screening; final metadata should be reconciled.
- Extraction uncertainty: Moderate because downstream exact match is a narrow proxy.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Pending version reconciliation.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Shows that broader issue discovery and selective context augmentation can improve downstream review usefulness, but additional context is not uniformly beneficial.
- What the paper does not establish: It does not establish developer-perceived usefulness, complete issue recall, or safe removal of lower-ranked comments.
- Research gap supported: Review evaluation should jointly measure coverage, downstream actionability, inspection burden, and context-retrieval cost.
- Candidate synthesis claims: Candidate-list breadth can recover human-aligned issues missed by primary-issue prompting, while refinement-guided pruning offers a practical coverage–burden trade-off.
- Follow-up verification needed: Inspect exact dataset split, prompts, and released artifacts before corpus integration.
