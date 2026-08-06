# Results

The results describe evidence coverage and reporting within the 121-study corpus. Unless stated otherwise, each count is the number of included studies with coded evidence for a field. These study counts do not estimate comment-level prevalence or comparative effects. Missing reporting is not interpreted as a zero effect.

## RQ1: Problematic-comment Types

The literature does not support treating all weak comments as hallucinations. Reported failures include unsupported or context-misaligned claims, incorrect technical claims, wrong location or cause, irrelevance, vagueness, non-actionability, invalid fixes, redundancy, low-value nitpicks, severity miscalibration, and context-dependent cases [@p02_tantithamthavorn2026_hallujudge; @p19_nguyen2025_fine_grained_classification; @p21_peng2025_icodereviewer; @p58_jin2026_reliable_code_reviewers]. The synthesis further separates input/context failures, workflow failures, and evaluator failures because these require different remedies.

Study-level coding found the broadest evidence coverage for incorrect claims (25 studies), irrelevance (23), spurious or false-positive findings (16), low-value or nitpick feedback (14), unsupported or hallucinated claims (13), and vague or generic feedback (12).

<!-- table: caption="Most frequently coded problematic-comment or related failure categories." label="tab:rq1-failures" longtable="false" -->
| Failure category | Studies with coded evidence |
|---|---:|
| Incorrect claim | 25 |
| Irrelevant | 23 |
| Spurious or false positive | 16 |
| Low-value or nitpick | 14 |
| Unsupported or hallucinated | 13 |
| Vague or generic | 12 |
| Missed issue or false negative | 6 |
| Adversarial or biased judgment | 5 |

## RQ2: Evaluation Dimensions

Evaluation has moved beyond BLEU and exact matching toward semantic, human-centered, and workflow dimensions [@p01_lu2025_deepcrceval; @p14_li2022_codereviewer; @p69_jiang2025_deep_assessment_crg]. However, correctness, grounding, relevance, usefulness, actionability, explanation quality, acceptance, and downstream revision remain distinct constructs. Relevance labels do not establish correctness, and direct acceptance can underestimate perceived value [@p07_olewicki2024_revmate; @p39_bosu2015_useful_reviews; @p57_heumuller2025_relevance_reviews; @p60_ahmed2025_feedback_useful]. No single metric in the corpus captures comment quality, coverage, workflow value, and evaluator validity together.

Coverage appears in 28 coded records, followed by lexical similarity (23), evaluator validity and usefulness (22 each), correctness and cost/latency (19 each), and acceptance/adoption (14). Grounding is explicitly coded in four records, even though grounding-related failures occur elsewhere. This difference illustrates why failure categories and evaluation dimensions must be extracted separately.

<!-- table: caption="Most frequently coded evaluation dimensions." label="tab:rq2-dimensions" longtable="false" -->
| Evaluation dimension | Studies with coded evidence |
|---|---:|
| Coverage | 28 |
| Lexical similarity | 23 |
| Evaluator validity | 22 |
| Usefulness | 22 |
| Correctness | 19 |
| Cost or latency | 19 |
| Acceptance or adoption | 14 |
| Workflow impact | 12 |
| Explanation quality | 11 |

## RQ3: Mitigation Families

Mitigations intervene before generation, during generation, after generation, or before display. Pre-generation approaches include data cleaning, reviewability or context gates, and context selection. Generation-time approaches include prompting, fine-tuning, retrieval, specification grounding, static-analysis support, routing, and multi-agent generation. Post-generation approaches include critics, grounding checks, relevance or actionability filters, repair validation, rewriting, aggregation, and staged verification. Pre-display decisions include suppression and human escalation [@p08_liu2025_too_noisy; @p10_sun2025_bitsai_cr; @p11_zhang2025_laura; @p35_mcaleese2024_llm_critics].

Filtering/suppression is the most frequently coded family (30 studies), followed by human escalation (27), fine-tuning (20), verification/critics (15), retrieval/RAG (14), and prompting (11). Benchmark/rubric interventions appear in ten studies. Less frequent families include data cleaning, reward optimization, rewriting, static-analysis hybrids, multi-agent generation, specification grounding, and routing. Frequency does not establish effectiveness because the studies use different artifacts and outcomes.

<!-- table: caption="Most frequently coded mitigation families." label="tab:rq3-mitigation" longtable="false" first-column-width="2.75in" -->
| Mitigation family | Studies with coded evidence |
|---|---:|
| Filtering or suppression | 30 |
| Human escalation | 27 |
| Fine-tuning | 20 |
| Verification or critic | 15 |
| Retrieval or RAG | 14 |
| Prompting | 11 |
| Benchmark or rubric as evaluation intervention | 10 |
| Data cleaning | 5 |
| Reward optimization | 4 |

## RQ4: Trade-off Evidence

The strongest recurring gap is asymmetric reporting. Studies commonly report improved quality, precision, acceptance, issue coverage, or reduced false positives, but less often report useful comments wrongly removed, retained review coverage, escalation burden, or end-to-end cost. Evidence nevertheless shows that more context can degrade performance, filtering can favor precision over recall, reformulation can change intent, and verification can increase routing and model-call cost [@p04_kumar2026_swe_prbench; @p10_sun2025_bitsai_cr; @p18_bensghaier2025_curated_reviews; @p65_ameen2026_qasecclaw]. The evidence therefore supports reporting error reduction and preservation as separate outcomes.

The reporting asymmetry is visible in the extracted counts. Preservation-related evidence appears in 45 records, coverage in 46, human-escalation evidence in 27, and cost evidence in 34. These fields often appear as design implications, limitations, or partial measurements rather than complete deployment outcomes. The counts show where a trade-off is addressed, not whether it was measured with a common protocol or resolved favorably.

Figure \ref{fig:rq4-tradeoff-evidence} shows the imbalance across these four reporting fields.

<!-- figure: path="figures/rq4_tradeoff_evidence.tex" caption="Availability of reported trade-off evidence in the 121-study corpus. Values are counts of included studies with coded evidence for each field; they are not effect sizes, success rates, or estimates of intervention effectiveness." label="fig:rq4-tradeoff-evidence" -->

<!-- table: caption="Availability of trade-off evidence in the 121 included studies." label="tab:rq4-reporting" -->
| Trade-off field | Reported | No extractable evidence identified | Unclear or not applicable |
|---|---:|---:|---:|
| Useful-feedback preservation | 45 | 76 | 0 |
| Review or issue coverage | 46 | 75 | 0 |
| Human escalation | 27 | 91 | 3 |
| Cost | 34 | 87 | 0 |

`No extractable evidence identified` means that the available full text did not report or measure the outcome. `Unclear or not applicable` means that the field was missing or its applicability could not be determined.

## RQ5: Context, Dataset, and Annotation Validity

Context quality includes relevance, completeness, specificity, consistency, freshness, reviewability, provenance, integrity, and attention load. More context is not necessarily more usable context [@p04_kumar2026_swe_prbench; @p06_hu2025_contextcrbench; @p16_icoz2026_context_aware]. Human review references are realistic but can be noisy, incomplete, or dependent on reviewer experience [@p08_liu2025_too_noisy; @p18_bensghaier2025_curated_reviews; @p23_lin2026_reviewer_experience]. Context can also manipulate evaluators through confirmation cues, adversarial comments, familiar patterns, or obfuscation [@p63_mitropoulos2026_confirmation_bias; @p64_thornton2026_adversarial_comments; @p67_bernstein2025_trust_me_function; @p68_li2025_cotdeceptor]. Annotation reliability and evidence provenance must therefore be reported as part of validity rather than treated as implementation details.

Reviewer/workflow context is the most common controlled context code (68 studies), followed by PR/issue context (32), repository/project context (30), diff/hunk context (22), and retrieved history (15). Six records contain adversarial-context evidence. The prominence of workflow context supports treating code review as a socio-technical process, while the smaller but distinct adversarial group motivates an integrity dimension in context-quality assessment.

### Sensitivity to the Non-canonical Supporting Reserve

The separate analysis of 53 substantively extracted supporting-reserve records did not require a new top-level evaluation, context, human-workflow, data-validity, or trade-off component. The reserve most often corroborated human-review or workflow value (29 records), evaluation or evaluator validity (26), context or grounding quality (25), and trade-off or mitigation design (23); two records mapped explicitly to annotation or dataset validity. These overlapping thematic mappings are not comparable with the study frequencies in the 121-study tables. They provide a limited robustness check, but do not establish lower-level saturation. Sixteen reserve candidates have only preliminary records, ten have none, and one reviewer performed the mapping.

## Derivation and Traceability of the Proposed Framework

Core studies inform the failure taxonomy, evaluation dimensions, benchmark limitations, mitigation families, and workflow outcomes. Supporting studies inform human-review value, evaluator robustness, annotation, and context interpretation. Peripheral studies contribute only limited transfer claims. These links explain the derivation of the framework. Within this corpus, no single framework combines comment quality, context quality, preservation, coverage, cost, workflow, and evaluator validity. This gap motivates the integrated framework presented in the next section.

<!-- table: caption="Evidence trace for the proposed framework layers." label="tab:framework-traceability" -->
| Framework component | Direct evidence | Supporting or transfer evidence | Qualification or tension |
|---|---|---|---|
| Input and context quality | PR-level and context-aware benchmarks [@p04_kumar2026_swe_prbench; @p06_hu2025_contextcrbench; @p16_icoz2026_context_aware] | Reviewability and provenance studies [@p23_lin2026_reviewer_experience; @p40_ram2018_reviewability] | Additional context can add noise or reduce performance; quantity is not a proxy for quality. |
| Generated-comment quality | Multi-dimensional review evaluation [@p01_lu2025_deepcrceval; @p18_bensghaier2025_curated_reviews; @p69_jiang2025_deep_assessment_crg] | Human usefulness evidence [@p39_bosu2015_useful_reviews; @p60_ahmed2025_feedback_useful] | Correctness, relevance, usefulness, and acceptance are non-equivalent constructs. |
| Problematic-comment type | Hallucination, noise, relevance, and failure studies [@p02_tantithamthavorn2026_hallujudge; @p08_liu2025_too_noisy; @p19_nguyen2025_fine_grained_classification] | Evaluator-bias and adversarial evidence [@p32_zhao2026_bias_loop; @p64_thornton2026_adversarial_comments] | The integrated taxonomy is author-derived and has not yet undergone independent reliability testing. |
| Mitigation decision | Filtering, retrieval, verification, and staged review [@p10_sun2025_bitsai_cr; @p11_zhang2025_laura; @p35_mcaleese2024_llm_critics; @p65_ameen2026_qasecclaw] | Human--AI workflow evidence [@p07_olewicki2024_revmate] | The four-way show/suppress/rewrite/escalate policy is proposed here rather than directly validated by one study. |
| Preservation and coverage | Precision, issue coverage, reformulation, and critique evidence [@p10_sun2025_bitsai_cr; @p18_bensghaier2025_curated_reviews; @p58_jin2026_reliable_code_reviewers] | Human-review value and workflow studies [@p37_sadowski2018_google_mcr; @p38_bacchelli2013_expectations_mcr] | Most studies mention or partially measure these outcomes rather than evaluating both with a common protocol. |
| Cost and evaluator validity | Cost-aware and judge-validity studies [@p01_lu2025_deepcrceval; @p29_wang2025_human_evaluators; @p31_jiang2025_codejudgebench] | General LLM-judge methodology [@p33_he2025_llmjudge_se; @p36_li2024_llms_as_judges] | Judge scores and cost proxies are task-dependent and require calibration against human evidence. |
