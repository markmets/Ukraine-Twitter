# Processed Data

This directory holds cleaned and aggregated datasets that are produced by the preprocessing notebook (`02_preprocessing.ipynb`) and used as inputs by the analysis notebooks.

## Files

| File | Produced by | Description |
|---|---|---|
| `tweets_clean.csv` | `02_preprocessing.ipynb` | Deduplicated, language-filtered tweet dataset |
| `monthly_counts.csv` | `03_descriptive_analysis.ipynb` | Monthly tweet volume aggregated by language |
| `crisis_periods.xlsx` | `04_crisis_attention.ipynb` | Tweet metrics broken down by defined crisis period |
