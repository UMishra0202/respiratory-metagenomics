# Respiratory Metagenomics: Pathogen Evidence Analysis

## Overview

This project analyzes paired-end shotgun metagenomic sequencing data from a respiratory sample to investigate computational evidence for respiratory pathogens using reference-based read mapping.

Rather than treating read alignment alone as evidence of infection, the workflow evaluates pathogen-specific mapping using alignment quality, genome-wide coverage, and read depth to distinguish stronger signals from low-level or tentative mapping evidence.

## Research Question

Can pathogen-specific reference mapping and genome-wide coverage analysis identify robust sequencing evidence for respiratory pathogens in shotgun metagenomic data?

## Dataset

- **Sample:** ERR970398
- **Sequencing strategy:** Paired-end shotgun metagenomic sequencing
- **Reference source:** NCBI representative pathogen genomes
- **Alignment:** BWA-MEM
- **Alignment processing:** SAMtools
- **Analysis:** Python, pandas, matplotlib

## Targeted Pathogen Panel

The reference panel included representative genomes from:

- Streptococcus pneumoniae
- Haemophilus influenzae
- Staphylococcus aureus
- Pseudomonas aeruginosa
- Moraxella catarrhalis
- Rhinovirus C
- SARS-CoV-2
- Respiratory syncytial virus A
- Human metapneumovirus

## Analysis Workflow

```text
Paired-end metagenomic reads
            |
            v
         Read QC
            |
            v
    Read preprocessing
            |
            v
      Host depletion
            |
            v
 Target pathogen references
            |
            v
      BWA-MEM alignment
            |
            v
       SAM/BAM sorting
            |
            v
       MAPQ >= 20 filtering
            |
            v
 Genome-wide coverage + depth
            |
            v
   Pathogen evidence ranking
            |
            v
 Visualization + interpretation
