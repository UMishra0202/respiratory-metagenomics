# Respiratory Metagenomics Pathogen Screening

## Overview

This project analyzes paired-end shotgun metagenomic sequencing data to investigate evidence of respiratory pathogens through targeted reference-based read mapping.

The analysis uses a curated reference panel containing representative genomes from:

- Streptococcus pneumoniae
- Haemophilus influenzae
- Staphylococcus aureus
- Pseudomonas aeruginosa
- Moraxella catarrhalis
- Rhinovirus C
- SARS-CoV-2
- Respiratory syncytial virus A
- Human metapneumovirus

## Dataset

- Sample: ERR970398
- Sequencing strategy: paired-end shotgun metagenomic reads
- Reference-based analysis performed using BWA-MEM
- Alignment processing performed using SAMtools

## Analysis Workflow

1. Downloaded representative pathogen reference genomes from NCBI.
2. Built a combined reference genome index.
3. Performed paired-end read alignment.
4. Converted and sorted SAM/BAM alignment files.
5. Generated alignment statistics.
6. Applied MAPQ >= 20 filtering for high-confidence alignments.
7. Calculated genome-wide coverage and read depth.
8. Compared pathogen-specific mapping evidence.
9. Generated summary tables and visualization figures.

## Results

After MAPQ >= 20 filtering:

| Pathogen | Genome Coverage | >=5x Coverage | >=10x Coverage | Mean Depth |
|---|---:|---:|---:|---:|
| Streptococcus pneumoniae | 71.98% | 47.56% | 25.93% | 9.81x |
| Haemophilus influenzae | 24.95% | 4.90% | 0.94% | 0.73x |

Other screened pathogens did not show comparable high-confidence mapping evidence in this analysis.

### Interpretation

Streptococcus pneumoniae showed the strongest genomic mapping signal, with substantial genome coverage and higher read depth.

Haemophilus influenzae showed substantially weaker coverage and depth and is therefore treated as low-level or tentative mapping evidence rather than an equivalent detection.

These results represent computational mapping evidence and should not be interpreted as a clinical diagnosis.

## Outputs

Key outputs include:

- `results/final_pathogen_coverage_summary.csv`
- `results/figures/pathogen_screening_read_counts.png`
- `results/figures/pathogen_genome_coverage.png`
- `results/figures/streptococcus_pneumoniae_coverage.png`
- `results/figures/final_pathogen_evidence.png`

## Reproducibility

Analysis scripts are provided in the `scripts/` directory.

The workflow is designed to document the computational steps from raw sequencing reads through pathogen-specific mapping, filtering, coverage analysis and visualization.

## Limitations

This analysis uses a targeted reference panel rather than an unrestricted microbial reference database. Mapping evidence alone does not establish clinical infection. Low-depth or low-coverage signals require additional validation.

## Tools

- BWA
- SAMtools
- Python
- pandas
- matplotlib
- NCBI reference genomes

