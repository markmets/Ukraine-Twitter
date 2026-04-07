"""
config.py — single source of all paths and shared settings.

Import this at the top of every notebook:
    import sys; sys.path.insert(0, '..'); from config import *
"""

from pathlib import Path

# ── Root of the pipeline folder ─────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent

# ── Data directories ─────────────────────────────────────────────────────────
DATA_DIR       = ROOT / "data"
INPUT_DIR      = DATA_DIR / "input"       # word_forms.xlsx lives here
RAW_DIR        = DATA_DIR / "raw"         # timestamped run folders (run_YYYYMMDD_HHMMSS)
PROCESSED_DIR  = DATA_DIR / "processed"   # cleaned, combined CSVs
FINAL_DIR      = DATA_DIR / "final"       # versioned snapshots used in paper

# ── Output directories ────────────────────────────────────────────────────────
OUTPUT_DIR     = ROOT / "outputs"
FIGURES_DIR    = OUTPUT_DIR / "figures"

# ── Key file paths ────────────────────────────────────────────────────────────
# Choose which CSV in data/input/ to use as the master list of queried words.
# Change CURRENT_INPUT_NAME to another filename in data/input/ to point the notebooks
# at a different input without editing notebooks themselves.
CURRENT_INPUT_NAME = "all_forms_manuscript_version.csv"
WORD_FORMS_ALL      = INPUT_DIR  / CURRENT_INPUT_NAME     # all inflected forms with metadata; Canonical==1 rows define the canonical dataset

# Processed output files (from 02_combine_data)
# Keep metadata separate from API data - merge on [query, language_ISO] as needed
QUERY_METADATA_FILE       = PROCESSED_DIR / "query_metadata.csv"              # lookup: [query, language_ISO, Canonical, Type, ...]
ALL_WORDS_DAILY_FILE      = PROCESSED_DIR / "all_words_daily.csv"            # all queries (236), daily, API data only
CHOSEN_WORDS_DAILY_FILE   = PROCESSED_DIR / "chosen_words_daily.csv"         # canonical words only (Canonical==1), daily, API data only
ALL_WORDS_WEEKLY_FILE     = PROCESSED_DIR / "all_words_weekly.csv"           # all queries (236), weekly aggregated, API data only
CHOSEN_WEEKLY_FILE        = PROCESSED_DIR / "chosen_words_weekly.csv"        # canonical words only (Canonical==1), weekly aggregated, API data only
CHOSEN_WEEKLY_PIVOT_FILE  = PROCESSED_DIR / "chosen_words_weekly_pivoted.csv" # wide pivot: language rows x week columns

# ── API settings ──────────────────────────────────────────────────────────────
API_BASE_URL   = "https://storywrangling.org/api/ngrams"
API_DELAY_MIN  = 3   # seconds — minimum random delay between requests
API_DELAY_MAX  = 5   # seconds — maximum random delay between requests

# ── Analysis settings ─────────────────────────────────────────────────────────
SMOOTHING_WINDOW = 3    # weeks rolling average (set to None to disable)
REMOVE_UA_RU     = False  # exclude Ukrainian and Russian from between-language plots

# ── Language display order (matches paper) ────────────────────────────────────
LANGUAGE_ORDER = [
    'Ukrainian', 'Russian', 'Romanian', 'German', 'Dutch', 'Swedish',
    'Danish', 'Greek', 'English', 'Norwegian', 'Czech', 'Estonian',
    'Persian', 'Polish', 'Italian', 'Spanish', 'French', 'Finnish',
    'Turkish', 'Catalan', 'Portuguese', 'Hungarian', 'Urdu',
    'Indonesian', 'Arabic', 'Serbian', 'Korean', 'Vietnamese'
]

# ── Ensure all directories exist (safe to call at import time) ────────────────
for _d in [INPUT_DIR, RAW_DIR, PROCESSED_DIR, FINAL_DIR, FIGURES_DIR]:
    _d.mkdir(parents=True, exist_ok=True)
