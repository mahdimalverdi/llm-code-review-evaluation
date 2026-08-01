# Results

## RQ1: Problematic-comment Types

The literature does not support treating all weak comments as hallucinations. Reported failures include unsupported or context-misaligned claims, incorrect technical claims, wrong location or cause, irrelevance, vagueness, non-actionability, invalid fixes, redundancy, low-value nitpicks, severity miscalibration, and context-dependent cases [@p02_tantithamthavorn2026_hallujudge; @p08_liu2025_too_noisy; @p19_nguyen2025_fine_grained_classification; @p21_peng2025_icodereviewer; @p35_mcaleese2024_llm_critics; @p58_jin2026_reliable_code_reviewers]. The synthesis further separates input/context failures, workflow failures, and evaluator failures because these require different remedies.

## RQ2: Evaluation Dimensions

Evaluation has moved beyond BLEU and exact matching toward semantic, human-centered, and workflow dimensions [@p01_lu2025_deepcrceval; @p14_li2022_codereviewer; @p69_jiang2025_deep_assessment_crg]. However, correctness, grounding, relevance, usefulness, actionability, explanation quality, acceptance, and downstream revision remain distinct constructs. Relevance labels do not establish correctness, and direct acceptance can underestimate perceived value [@p07_olewicki2024_revmate; @p39_bosu2015_useful_reviews; @p57_heumuller2025_relevance_reviews; @p60_ahmed2025_feedback_useful]. No single metric in the corpus captures comment quality, coverage, workflow value, and evaluator validity together.

## RQ3: Mitigation Families

Mitigations intervene before generation, during generation, after generation, or before display. Pre-generation approaches include data cleaning, reviewability or context gates, and context selection. Generation-time approaches include prompting, fine-tuning, retrieval, specification grounding, static-analysis support, routing, and multi-agent generation. Post-generation approaches include critics, grounding checks, relevance or actionability filters, repair validation, rewriting, aggregation, and staged verification. Pre-display decisions include suppression and human escalation [@p08_liu2025_too_noisy; @p09_ren2025_hydra_reviewer; @p10_sun2025_bitsai_cr; @p11_zhang2025_laura; @p12_wang2025_sgcr; @p22_jaoua2025_static_analyzers; @p35_mcaleese2024_llm_critics; @p65_ameen2026_qasecclaw].

## RQ4: Trade-off Evidence

The strongest recurring gap is asymmetric reporting. Studies commonly report improved quality, precision, acceptance, issue coverage, or reduced false positives, but less often report useful comments wrongly removed, retained review coverage, escalation burden, or end-to-end cost. Evidence nevertheless shows that more context can degrade performance, filtering can favor precision over recall, reformulation can change intent, comprehensive critiques can add nitpicks, and verification can increase routing and model-call cost [@p04_kumar2026_swe_prbench; @p10_sun2025_bitsai_cr; @p18_bensghaier2025_curated_reviews; @p35_mcaleese2024_llm_critics; @p58_jin2026_reliable_code_reviewers; @p65_ameen2026_qasecclaw]. The evidence therefore supports reporting error reduction and preservation as separate outcomes.

## RQ5: Context, Dataset, and Annotation Validity

Context quality includes relevance, completeness, specificity, consistency, freshness, reviewability, provenance, integrity, and attention load. More context is not necessarily more usable context [@p04_kumar2026_swe_prbench; @p06_hu2025_contextcrbench; @p16_icoz2026_context_aware]. Human review references are realistic but can be noisy, incomplete, or dependent on reviewer experience [@p08_liu2025_too_noisy; @p18_bensghaier2025_curated_reviews; @p23_lin2026_reviewer_experience]. Context can also manipulate evaluators through confirmation cues, adversarial comments, familiar patterns, or obfuscation [@p63_mitropoulos2026_confirmation_bias; @p64_thornton2026_adversarial_comments; @p67_bernstein2025_trust_me_function; @p68_li2025_cotdeceptor]. Annotation reliability and evidence provenance must therefore be reported as part of validity rather than treated as implementation details.

## RQ6: Support for the Framework

Core studies directly support the failure taxonomy, evaluation dimensions, benchmark limitations, mitigation families, and workflow outcomes. Supporting studies ground human-review value, evaluator robustness, annotation, and context interpretation. Peripheral studies contribute only bounded transfer claims. Across these tiers, no single identified framework operationalizes comment quality, context quality, preservation, coverage, cost, workflow, and evaluator validity together. This corpus-bounded gap motivates the integrated framework presented in the next section.
