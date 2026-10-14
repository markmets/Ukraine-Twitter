# Ukraine-Twitter Storywrangler Pipeline

Fetches language data about "Ukraine" from the [Storywrangler API](https://storywrangling.org) across 28 languages on Twitter, aggregates frequency time-series at daily and weekly granularity, and produces analysis-ready CSVs and publication figures.



### RenkuLab / workshop version (this `renkulab` branch)

This branch is the RenkuLab copy of the code (https://renkulab.io/p/mark.mets/ukraine-twitter). The `main` branch is the version linked to the article.

Differences from `main`:
- The processed data the figure notebooks read is already included in `data/processed/` (generated 14 Oct 2026), so the API download is not needed. Start with any figure notebook.
- `requirements.txt` pins the package versions the paper figures were made with.

Steps 1 and 2 below still work if you want to see how the data was made. Running the full `01_api_query.ipynb` takes about 20–30 minutes. Note that running `02_combine_data.ipynb` overwrites the included files in `data/processed/` with whatever API data you downloaded.



### Pipeline execution order

1. `01_api_query.ipynb` — Fetch from Storywrangler API
- Can run multiple times, will reuse existing queries
- `01_api_query_filtered_onlychosenngrams.ipynb` is a smaller alternative that fetches only the chosen n-grams

2. `02_combine_data.ipynb` — Aggregate and process to weekly CSVs
- Will use the latest API query run folder

3. Figure notebooks — Generate publication plots (in any order)



### Project Structure

UA_Twitter_Code_repository/

├── config.py                           ← All paths and settings
├── requirements.txt                    
├── README.txt                          
├── notebooks/                          ← Jupyter notebooks
│   ├── 01_api_query.ipynb              ← Stage 1: Fetch from API
│   ├── 01_api_query_filtered_onlychosenngrams.ipynb ← Stage 1 (alternative): chosen n-grams only
│   ├── 02_combine_data.ipynb           ← Stage 2: Aggregate & process
│   └── Figure notebooks:
│       ├── Fig.1 Over-Underexpression_Short_WITHINlanguage_SUM.ipynb
│       ├── Fig.2 Over-Underexpression_Short_betweenlanguage_SUM.ipynb
│       ├── Fig.S1 Raw freq heatmap.ipynb
│       ├── Fig.S2 Over-Underexpression_Short_WITHINlanguage_SUM_no smoothing.ipynb
│       ├── Fig.S3 Over-Underexpression_Short_betweenlanguage_SUM_no smoothing.ipynb
│       ├── Fig.3_4_S4_Trends_and_Clustering.ipynb
│       ├── Fig.5a_Vectors_UMAPs.ipynb
│       ├── Fig.5b_Vectors_matrix.ipynb
│       ├── Fig.S5_Dendrograms.ipynb
│       ├── Fig.S6_Manual_Clusters.ipynb
│       └── Fig.S7_Comparing-word-forms_together.ipynb
│
├── data/
│   ├── input/                          ← Master query lists
│   │   └── all_forms_manuscript_version.csv                  
│   │
│   ├── raw/                            ← API responses (timestamped runs)
│   │   └── run_YYYYMMDD_HHMMSS/
│   │       ├── timeseries_data.csv     (raw daily API data)
│   │       ├── query_metadata.csv      (query metadata)
│   │       └── jsons/                  (one JSON per query-language pair)
│   │
│   └── processed/                      ← Analysis-ready outputs
│       ├── query_metadata.csv          (lookup table)
│       ├── all_words_daily.csv         (all queries, daily)
│       ├── all_words_weekly.csv        (all queries, weekly)
│       ├── chosen_words_daily.csv      (chosen words only, daily)
│       ├── chosen_words_weekly.csv     (chosen words only, weekly)
│       └── chosen_words_weekly_pivoted.csv (wide pivot: languages × weeks)
│                          
└── outputs/        
    ├── tables/                         ← Saved tables (peak_ratios_2014_2022.csv)
    └── figures/                        ← Saved plots (pdf, png, svg, html, eps)
        ├── Fig.1_within-language/     
        ├── Fig.2_between-language/
        ├── Fig.S1_raw_freq_heatmap/   
        ├── Fig.S2_within-language-nosmooth/
        ├── Fig.S3_between-language-nosmooth/
        ├── Fig.3_kmeans_clustering_2014/
        ├── Fig.3_kmeans_clustering_2022/
        ├── Fig.4_trends_2014_vs_2022/
        ├── Fig.5a_Vectors_UMAPs/
        ├── Fig.5b_Vectors_matrix/
        ├── Fig.S4_cluster_evaluations/
        ├── Fig.S5_dendrograms/
        ├── Fig.S6_manual_clusters/
        └── Fig.S7_word_forms_together/



### Version

The tag `epj-submission` is the code version matching the manuscript submitted to EPJ Data Science (September 2026).

- `data/raw/`, `data/processed/` and `outputs/` are not tracked; run the pipeline (stages 1-2) to recreate them.
- Days on which a keyword does not appear are kept as missing (not zero) when computing the window means used to normalize the Fig. 3 / S4 time series.
- Fig. 3 (2022): Italian lies on the boundary between "Shock & Sustain 2" and "Noisy Shock & Sustain" (the two solutions differ by about 1% in KMeans inertia). The notebook uses `random_state=24` for the 2022 clustering to reproduce the published figure; with `random_state=0` and scikit-learn 1.6, Italian is assigned to "Noisy Shock & Sustain". All other cluster assignments are identical.
