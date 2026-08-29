# Respiratory Metagenomics: Pathogen Evidence Analysis

A reference-based shotgun metagenomics workflow for evaluating computational evidence of respiratory pathogens from paired-end sequencing data.

## Overview

This project analyzes paired-end shotgun metagenomic sequencing data using targeted pathogen reference mapping, alignment filtering, genome-wide coverage, and read-depth analysis.

The workflow evaluates whether mapped-read signals are supported by broader genome-wide evidence rather than relying on read counts alone.

## Dataset

- **Sample:** ERR970398
- **Sequencing:** Paired-end shotgun metagenomic sequencing
- **Reference:** NCBI representative pathogen genomes
- **Alignment:** BWA-MEM
- **Alignment processing:** SAMtools
- **Analysis:** Python, pandas, matplotlib

## Targeted Pathogens

- *Streptococcus pneumoniae*
- *Haemophilus influenzae*
- *Staphylococcus aureus*
- *Pseudomonas aeruginosa*
- *Moraxella catarrhalis*
- Rhinovirus C
- SARS-CoV-2
- Respiratory syncytial virus A
- Human metapneumovirus

## Workflow

```text
Paired-end reads
      ↓
Target pathogen references
      ↓
BWA-MEM alignment
      ↓
SAM/BAM processing
      ↓
MAPQ ≥ 20 filtering
      ↓
Genome-wide coverage + read depth
      ↓
Pathogen evidence ranking
      ↓
Visualization
