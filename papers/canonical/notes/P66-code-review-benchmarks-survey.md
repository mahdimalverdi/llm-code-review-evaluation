# P66 — Survey of Code Review Benchmarks and Evaluation Practices

## Screening and proposal alignment

- **Decision:** Include
- **Group:** Supporting/Core
- **Relevance:** High
- **Scope:** Survey of 99 papers, covering 58 pre-LLM and 41 LLM-era studies.
- **Citation key:** `p66_khan2026_code_review_benchmarks_survey`

## Proposal RQ mapping

- **RQ1–RQ3:** Provides benchmark/task taxonomy and evaluation-practice map.
- **RQ4:** Identifies gaps in dynamic evaluation and realistic benchmark coverage.
- **RQ5:** Directly supports dataset validity and benchmark-design analysis.
- **RQ6:** Strong support for taxonomy, benchmark, and evaluation-framework design.

## Synthesis-ready summary

P66 organizes code-review research into five domains and 18 tasks, documenting datasets, metrics, sources, and target tasks. It provides important secondary evidence for benchmark fragmentation, limited capability coverage, and the need for taxonomy-guided fine-grained evaluation. It should be distinguished from primary empirical studies.

**Provisional quality score: 21/24.** Verify search protocol, inclusion process, and survey reliability.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p66_khan2026_code_review_benchmarks_survey`; Supporting/Core; Include; High relevance.
- Study overview: Survey of 99 pre-LLM and LLM-era code-review papers, datasets, metrics, and tasks.
- RQ1: Benchmark/task failure and coverage gaps (Reported).
- RQ2: Benchmark context, data sources, metrics, and evaluation practices (Reported).
- RQ3: Five domains and 18 fine-grained tasks; generative-review shift (Reported).
- RQ4: Realism, dynamic evaluation, task coverage, and metric trade-offs (Reported).
- RQ5: Dataset/benchmark validity and taxonomy gaps (Reported).
- RQ6: Strong direct support for benchmark taxonomy and SLR synthesis.
- Failure taxonomy: task undercoverage; static evaluation; fragmented datasets; weak context; metric mismatch.
- Metrics: benchmark/task metadata, dataset source, evaluation metric, and task coverage.
- Mitigation/trade-off: richer/dynamic benchmarks; realism and coverage add collection/annotation cost.
- Validity: survey search, inclusion, and coding reliability require verification.
- Quality: 21/24 provisional; strong secondary evidence.
- Synthesis conclusion: supports a benchmark-aware evaluation framework and explicit evidence mapping.

### 1. Identification
- P66; `p66_khan2026_code_review_benchmarks_survey`; local full PDF extracted and reviewed; authoritative record.
### 2. Screening and proposal alignment
- Include as supporting. `p66_khan2026_code_review_benchmarks_survey`; Supporting/Core; Include; High relevance.
### 3. Study overview
Survey of 99 pre-LLM and LLM-era code-review papers, datasets, metrics, and tasks.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Benchmark/task failure and coverage gaps (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Benchmark context, data sources, metrics, and evaluation practices (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Five domains and 18 fine-grained tasks; generative-review shift (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Realism, dynamic evaluation, task coverage, and metric trade-offs (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Dataset/benchmark validity and taxonomy gaps (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Strong direct support for benchmark taxonomy and SLR synthesis. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| task undercoverage | Reported/Inferred | Full PDF |
| static evaluation | Reported/Inferred | Full PDF |
| fragmented datasets | Reported/Inferred | Full PDF |
| weak context | Reported/Inferred | Full PDF |
| metric mismatch. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| benchmark/task metadata | Transfer/deployment limits remain | Full PDF |
| dataset source | Transfer/deployment limits remain | Full PDF |
| evaluation metric | Transfer/deployment limits remain | Full PDF |
| and task coverage. | Transfer/deployment limits remain | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: richer/dynamic benchmarks; realism and coverage add collection/annotation cost.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: task-specific; retained useful-issue coverage is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- survey search, inclusion, and coding reliability require verification.
- Q7–Q8 encode judging and reliability depth.
### 9. Quality appraisal
| Criterion | Score | Evidence note |
|---|---:|---|
| Q1 | 2 | goal at scored depth. |
| Q2 | 2 | artifact at scored depth. |
| Q3 | 2 | dataset/context at scored depth. |
| Q4 | 2 | procedure at scored depth. |
| Q5 | 2 | metrics at scored depth. |
| Q6 | 1 | failures at scored depth. |
| Q7 | 2 | judging at scored depth. |
| Q8 | 2 | reliability at scored depth. |
| Q9 | 0 | intervention at scored depth. |
| Q10 | 2 | trade-offs at scored depth. |
| Q11 | 2 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 21/24; calibrated reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence, transfer limits, and selection/publication bias remain explicit; independent second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Survey of 99 pre-LLM and LLM-era code-review papers, datasets, metrics, and tasks.
- Boundary: supports a benchmark-aware evaluation framework and explicit evidence mapping.
