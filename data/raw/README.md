# Raw Data

This directory holds the original, unmodified source data as collected from the Storywrangler API.

## Files

| File | Description |
|---|---|
| `28languagesUA.csv` | Daily frequency and rank data per language for Ukraine-related terms (28 languages, 2008–2023) |
| `original_language_query_dict.json` | Mapping of language names to the keyword used in the final query for each language |

## Data Format

### `28languagesUA.csv`

Each row corresponds to one language on one day. Columns:

| Column | Type | Description |
|---|---|---|
| `date` | date | Day of observation (YYYY-MM-DD) |
| `count` | int | Total tweet count (including retweets) |
| `count_no_rt` | int | Tweet count excluding retweets |
| `rank` | int | Daily rank of the term (including retweets) |
| `rank_no_rt` | int | Daily rank excluding retweets |
| `freq` | float | Relative frequency of the term (including retweets) |
| `freq_no_rt` | float | Relative frequency excluding retweets |
| `odds` | float | Odds of the term appearing (including retweets) |
| `odds_no_rt` | float | Odds excluding retweets |
| `language` | str | Language name (e.g. `Arabic`, `Ukrainian`) |
| `country` | str | Country filter applied (`ukraine`) |

### `original_language_query_dict.json`

A JSON object mapping language name to the search keyword used, e.g.:

```json
{
  "English": "Ukraine",
  "Ukrainian": "Україна",
  "Arabic": "أوكرانيا"
}
```

28 languages are included in total.
