# Ukraine-Twitter

Code and data repository for the academic article:

**"Crisis-induced differences in attention towards Ukraine in Twitter 2008–2023"**

## Overview

This repository contains the Jupyter notebooks and datasets used for the analysis presented in the article. The study examines how crisis events (e.g., the 2014 Euromaidan revolution, the 2022 full-scale invasion) drive shifts in the volume, sentiment, and geographic distribution of Twitter attention towards Ukraine over the period 2008–2023.

## Repository Structure

```
Ukraine-Twitter/
├── notebooks/          # Jupyter notebooks for data collection, processing, and analysis
├── data/
│   ├── raw/            # Raw Twitter data (CSV / Excel), as collected
│   └── processed/      # Cleaned and aggregated datasets ready for analysis
├── results/
│   ├── figures/        # Output figures (PNG, PDF)
│   └── tables/         # Output tables (CSV, Excel)
├── requirements.txt    # Python package dependencies
└── README.md
```

## Data

Data files are stored in `data/raw/` (original exports) and `data/processed/` (cleaned versions).  
Formats: **CSV** and **Excel (.xlsx)**.

> **Note:** Large raw data files may not be tracked by Git. See `data/raw/README.md` for instructions on obtaining the full dataset.

## Notebooks

| Notebook | Description |
|---|---|
| `01_data_collection.ipynb` | Twitter API data collection and export |
| `02_preprocessing.ipynb` | Data cleaning, deduplication, and feature engineering |
| `03_descriptive_analysis.ipynb` | Descriptive statistics and time-series plots |
| `04_crisis_attention.ipynb` | Crisis-period attention analysis and comparisons |
| `05_visualizations.ipynb` | Publication-quality figures |

## Requirements

Python 3.9+ is recommended. Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/markmets/Ukraine-Twitter.git
   cd Ukraine-Twitter
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place raw data files in `data/raw/` (see `data/raw/README.md`).
4. Run notebooks in order from `notebooks/01_data_collection.ipynb` onwards.

## Citation

If you use this code or data in your own work, please cite:

> Markmets (2023). *Crisis-induced differences in attention towards Ukraine in Twitter 2008–2023*. [Journal / Preprint details TBD]

## License

This repository is made available for academic and research purposes. See [LICENSE](LICENSE) for details.
