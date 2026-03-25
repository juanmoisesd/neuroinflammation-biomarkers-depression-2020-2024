# Neuroinflammation Biomarkers in Depression and Mental Disorders: Global Data 2020-2024

[![DOI](https://img.shields.io/badge/DOI-10.7910%2FDVN%2FQBQXKL-blue)](https://doi.org/10.7910/DVN/QBQXKL)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Harvard Dataverse](https://img.shields.io/badge/Harvard-Dataverse-red)](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/QBQXKL)
[![ORCID](https://img.shields.io/badge/ORCID-0000--0002--8401--8018-green)](https://orcid.org/0000-0002-8401-8018)

## Overview

This dataset compiles global statistics and research data on **neuroinflammation biomarkers** (IL-6, TNF-alpha, CRP) in patients with **depression and major depressive disorder (MDD)**, drawn from meta-analyses covering up to 58,256 participants (2020–2024).

## Key Findings

| Biomarker | AUC | MDD Mean | Control Mean | Sensitivity | Specificity |
|---|---|---|---|---|---|
| IL-6 | **0.724** | 8.42 pg/mL | 3.18 pg/mL | 0.71 | 0.68 |
| TNF-alpha | **0.861** | 15.7 pg/mL | 8.2 pg/mL | 0.84 | 0.79 |
| CRP | **0.678** | 4.12 mg/L | 1.93 mg/L | 0.65 | 0.72 |
| BDNF | **0.731** | 18.4 ng/mL | 27.6 ng/mL | 0.70 | 0.74 |

- Depression prevalence in high-inflammation cohorts: **65%** (nursing students study)
- Bidirectional links confirmed: higher CRP/IL-6 at baseline predicted future depressive symptoms (meta-analysis N=58,256)
- TNF-alpha has the **highest diagnostic AUC (0.861)**

## Dataset Contents (20 files)

| File | Description |
|---|---|
| `biomarker_levels_depression.csv` | Biomarker levels in MDD vs controls (15 studies, 14 countries) |
| `auc_diagnostic_values.csv` | ROC/AUC diagnostic performance of each biomarker |
| `prevalence_by_cohort.csv` | Depression prevalence by cohort type and inflammation level |
| `symptom_biomarker_correlation.csv` | Symptom-biomarker correlation matrix |
| `meta_analysis_summary.csv` | Summary of 8 key meta-analyses (2020-2024) |
| `treatment_response_inflammation.csv` | Anti-inflammatory treatment response data (8 RCTs) |
| `genetic_risk_IL6.csv` | UK Biobank genetic variants (N=368,341) |
| `longitudinal_crp_depression.csv` | Longitudinal CRP/IL-6 predicting depression (8 cohorts) |
| `analysis_biomarkers.ipynb` | Jupyter notebook for full analysis and visualization |
| `biomarkers_data.json` | JSON structured data |
| `biomarker_summary.tsv` | TSV summary table |
| `dataset_description.json` | BIDS 1.8.0 metadata |
| `CITATION.cff` | Citation metadata (CFF format) |
| `METHODOLOGY.md` | Full methodology documentation |
| `codebook.md` | Variable descriptions |
| `country_metadata.csv` | Country-level contextual data (14 countries) |
| `summary_statistics.csv` | Descriptive statistics across all variables |
| `data_formats_readme.txt` | Guide to Parquet/HDF5 conversion |
| `data_sources.bib` | BibTeX bibliography |
| `README.md` | This file |

## Data Sources

- PubMed/PMC meta-analyses (2020-2024)
- UK Biobank neuroinflammation studies (N=368,341)
- WHO Global Depression Prevalence Reports
- Bibliometric analyses on neuroinflammation research trends

## Citation

> de la Serna, Juan Moises, 2026, "Neuroinflammation Biomarkers in Depression and Mental Disorders: Global Data 2020-2024", Harvard Dataverse, V1. https://doi.org/10.7910/DVN/QBQXKL

## Author

**Juan Moises de la Serna** | ORCID: [0000-0002-8401-8018](https://orcid.org/0000-0002-8401-8018)  
International University of La Rioja (UNIR) | Behavioral Epigenetics & Neuroeducation Researcher

## License

[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
