# Ukraine-Twitter

Code and data repository for the academic article:

**"Crisis-induced differences in attention towards Ukraine in Twitter 2008–2023"**

## Overview

This repository contains the datasets used for the analysis presented in the article. The study examines how crisis events (e.g., the 2014 Euromaidan revolution, the 2022 full-scale invasion) drive shifts in the volume, sentiment, and geographic distribution of Twitter attention towards Ukraine over the period 2008–2023.

## Repository Structure

```
Ukraine-Twitter/
├── notebooks/
│   ├── StorywranglerData - Fig.1 Over-Underexpression_Short_WITHINlanguage_SUM.ipynb
│   ├── StorywranglerData - Fig.2 Over-Underexpression_Short_betweenlanguage_SUM.ipynb
│   ├── StorywranglerData - Fig.3,4,S4_offset-onsets_2014_2022 comparison_Okt2024.ipynb
│   ├── StorywranglerData - Fig.5a_Vectors_UMAPs.ipynb
│   ├── StorywranglerData - Fig.5b_Vectors_matrix.ipynb
│   ├── StorywranglerData - Fig.S1 Raw freq heatmap.ipynb
│   ├── StorywranglerData - Fig.S2 Over-Underexpression_Short_WITHINlanguage_SUM_no smoothing.ipynb
│   ├── StorywranglerData - Fig.S3 Over-Underexpression_Short_betweenlanguage_SUM_no smoothing.ipynb
│   ├── StorywranglerData - Fig.S5_Dendrograms.ipynb
│   ├── StorywranglerData - Fig.S6_2014_2022_4 manual clusters.ipynb
│   └── StorywranglerData - Fig.S7_Comparing-word-forms_together.ipynb
├── data/
│   ├── 28languagesUA.csv                    # Daily freq/rank per language, Ukraine (2008–2023)
│   ├── original_language_query_dict.json    # Language → search keyword mapping (28 languages)
│   ├── pivotUkraine_SUM_excelInput_weekly.csv  # Weekly freq sums pivoted by language
│   └── All_cases_allmetadata.csv               # Per-form metadata for comparative analysis
├── results/
│   ├── figures/        # Output figures (PNG, PDF)
│   └── tables/         # Output tables (CSV, Excel)
├── requirements.txt    # Python package dependencies
└── README.md
```

## Data

All data is sourced from the [Storywrangler](https://storywrangler.org/) API, which tracks word frequencies across Twitter/X by language and day. All files are stored directly in `data/`.

| File | Description |
|---|---|
| `28languagesUA.csv` | Daily count, rank, and frequency statistics for Ukraine-related keywords across 28 languages (2008–2023). Columns: `date`, `count`, `count_no_rt`, `rank`, `rank_no_rt`, `freq`, `freq_no_rt`, `odds`, `odds_no_rt`, `language`, `country`. |
| `original_language_query_dict.json` | JSON mapping of language name to the search keyword used for that language (e.g. `"English": "Ukraine"`, `"Arabic": "أوكرانيا"`). |
| `pivotUkraine_SUM_excelInput_weekly.csv` | Pivoted version of `28languagesUA.csv`. Rows = languages, columns = ISO week-start dates. Values are weekly sums of the `freq` column. |
| `All_cases_allmetadata.csv` | Per-query-form dataset combining frequency data with full linguistic metadata (grammatical case, gender, plurality, demonym status, etc.) used to generate the comparative plot. |

See `data/README.md` for detailed column descriptions.

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
3. Place data files in `data/` (see `data/README.md`).
4. Open notebooks from the `notebooks/` folder (e.g. with Jupyter Lab or Jupyter Notebook):
   ```bash
   jupyter lab notebooks/
   ```

## Citation

If you use this code or data in your own work, please cite:

> Markmets (2023). *Crisis-induced differences in attention towards Ukraine in Twitter 2008–2023*. [Journal / Preprint details TBD]

## License

This repository is made available for academic and research purposes. See [LICENSE](LICENSE) for details.
