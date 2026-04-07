# Ukraine-Twitter Storywrangler Pipeline

Fetches language data about "Ukraine" from the [Storywrangler API](https://storywrangling.org) across 28 languages on Twitter, aggregates frequency time-series at daily and weekly granularity, and produces analysis-ready CSVs and publication figures.



### Pipeline execution order

1. `01_api_query.ipynb` — Fetch from Storywrangler API
- Can run multiple times, will reuse existing queries

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
│   ├── 02_combine_data.ipynb           ← Stage 2: Aggregate & process
│   └── Figure notebooks:
│       ├── Fig.1 Over-Underexpression_Short_WITHINlanguage_SUM.ipynb
│       ├── Fig.2 Over-Underexpression_Short_betweenlanguage_SUM.ipynb
│       ├── Fig.S1 Raw freq heatmap.ipynb---cd notebooks
│       ├── Fig.S2 Over-Underexpression_Short_WITHINlanguage_SUM_no smoothing.ipynb
│       ├── Fig.S3 Over-Underexpression_Short_betweenlanguage_SUM_no smoothing.ipynb
│       ├── Fig.3_4_S4_Trends_and_Clustering.ipynb
│       ├── Fig.5a_Vectors_UMAPs.ipynb## Project Structurejupyter lab```bash
│       ├── Fig.5b_Vectors_matrix.ipynb
│       ├── Fig.S5_Dendrograms.ipynb
│       ├── Fig.S6_Manual_Clusters.ipynb
│       └── Fig.S7_Comparing-word-forms_together.ipynb
│
├── data/pipeline/
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