## Results and Interpretation

### Overview

The reference-based screening identified substantial read mapping to two bacterial respiratory pathogens, with markedly different levels of genome-wide support.

| Pathogen | Mapped Reads | Mapped Read Share | Genome Coverage | Mean Depth | Evidence |
|---|---:|---:|---:|---:|---|
| *Streptococcus pneumoniae* | 168,138 | 92.65% | 71.98% | 9.81× | Strong computational evidence |
| *Haemophilus influenzae* | 10,557 | 5.82% | 24.95% | 0.73× | Secondary / tentative evidence |
| *Staphylococcus aureus* | 1,875 | 1.03% | NA | NA | Minimal mapped-read signal |
| *Pseudomonas aeruginosa* | 711 | 0.39% | NA | NA | Minimal mapped-read signal |
| *Moraxella catarrhalis* | 195 | 0.11% | NA | NA | Minimal mapped-read signal |

### Genome-wide evidence

*Streptococcus pneumoniae* showed the strongest computational support across the evaluated evidence dimensions. Approximately 71.98% of the reference genome was covered after MAPQ ≥20 filtering, with a mean read depth of approximately 9.81×.

Importantly, coverage was not restricted to a small number of highly represented regions. Approximately 47.56% of the genome reached at least 5× coverage and 25.93% reached at least 10× coverage, providing broader genome-wide support for the mapped-read signal.

*Haemophilus influenzae* showed a substantially weaker signal. Although 10,557 reads mapped to the reference, only approximately 24.95% of the genome was covered after MAPQ filtering, with a mean depth of approximately 0.73×. Only approximately 4.90% of the genome reached 5× coverage and less than 1% reached 10× coverage.

The remaining bacterial targets produced relatively small mapped-read signals and did not show sufficient genome-wide coverage or depth for the same level of evidence assessment.

### Interpretation

The results demonstrate why mapped-read abundance alone should not be used as the sole criterion for pathogen evidence in shotgun metagenomic data.

The *S. pneumoniae* signal is supported simultaneously by:

- high mapped-read abundance,
- high relative mapped-read share,
- broad genome-wide coverage,
- substantial read depth,
- and coverage at both 5× and 10× thresholds.

In contrast, the *H. influenzae* signal illustrates a case where a non-trivial number of reads can map to a reference while genome-wide support remains comparatively limited.

The lower-abundance targets produced only minimal mapped-read signals and lacked sufficient downstream coverage/depth evidence for stronger computational interpretation.

### Important limitation

These findings represent **reference-based computational evidence**, not clinical diagnosis or confirmation of active infection.

Read mapping can be influenced by reference selection, sequence similarity between organisms, genome representation, sequencing depth, and alignment characteristics. Therefore, mapped reads and genome coverage should be interpreted as computational evidence within this analysis rather than direct evidence of disease causation.

Additional validation using broader taxonomic classification, strain-level analysis, negative/positive controls, and independent biological or clinical evidence would be required for diagnostic interpretation.
