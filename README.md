# Respiratory Metagenomics: Pathogen Evidence Analysis

A reference-based shotgun metagenomics workflow for evaluating computational evidence of respiratory pathogens from paired-end sequencing data.

## Research Question

Can pathogen-associated read signals in shotgun metagenomic sequencing be distinguished using genome-wide coverage and read-depth evidence rather than relying on mapped-read counts alone?

## Overview

This project analyzes paired-end shotgun metagenomic sequencing data using targeted pathogen reference mapping, alignment filtering, genome-wide coverage, read-depth analysis, and mapped-read abundance.

The analysis integrates multiple evidence dimensions to distinguish strong computational evidence from lower-confidence or minimal mapping signals.

Importantly, the results represent **reference-based computational evidence** and should not be interpreted as definitive clinical diagnosis or confirmation of active infection.

## Dataset

- **Sample:** ERR970398
- **Sequencing:** Paired-end shotgun metagenomic sequencing
- **Reference:** NCBI representative pathogen genomes
- **Alignment:** BWA-MEM
- **Alignment processing:** SAMtools
- **Analysis:** Python, pandas, matplotlib

## Target Pathogens

### Bacterial targets
- *Streptococcus pneumoniae*
- *Haemophilus influenzae*
- *Staphylococcus aureus*
- *Pseudomonas aeruginosa*
- *Moraxella catarrhalis*

### Viral targets
- Rhinovirus C
- SARS-CoV-2
- Respiratory syncytial virus A
- Human metapneumovirus

## Workflow

```text
Paired-end sequencing reads
          ↓
Target pathogen reference genomes
          ↓
BWA-MEM alignment
          ↓
SAM/BAM processing
          ↓
MAPQ ≥ 20 filtering
          ↓
Genome-wide coverage + read depth
          ↓
Mapped-read abundance/distribution
          ↓
Integrated pathogen evidence ranking
          ↓
Visualization and summary
