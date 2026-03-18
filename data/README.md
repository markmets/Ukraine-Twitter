# Data

This directory contains all datasets used in the analysis.  
All frequency data is sourced from the [Storywrangler](https://storywrangler.org/) API.

## Files

| File | Description |
|---|---|
| `28languagesUA.csv` | Daily count, rank, and frequency statistics for Ukraine-related keywords across 28 languages (2008–2023) |
| `original_language_query_dict.json` | JSON mapping of language name to the search keyword used for that language (28 languages) |
| `pivotUkraine_SUM_excelInput_weekly.csv` | Pivoted weekly sums of the `freq` column per language (languages as rows, week-start dates as columns) |
| `All_cases_allmetadata.csv` | Per-query-form dataset with full linguistic metadata (case, gender, plurality, etc.) for the comparative plot |

## Column reference

### `28languagesUA.csv`

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

A JSON object mapping language name to the search keyword, e.g.:

```json
{
  "English": "Ukraine",
  "Ukrainian": "Україна",
  "Arabic": "أوكرانيا"
}
```

28 languages are included in total.

### `pivotUkraine_SUM_excelInput_weekly.csv`

Languages as rows, ISO week-start dates (`YYYY-MM-DD`) as columns. Values are the sum of daily `freq` values within each week.

### `All_cases_allmetadata.csv`

One row per query form per week. Columns:

| Column | Type | Description |
|---|---|---|
| `query` | str | Search keyword in the target language |
| `language_ISO` | str | ISO 639-1 language code |
| `date` | datetime | Week-start date |
| `count` | float | Weekly tweet count |
| `freq` | float | Weekly relative frequency |
| `language` | str | Full language name |
| `type` | str | Grammatical type (e.g. `Adjective`, `Noun`) |
| `plurality` | str | Grammatical number (e.g. `Singular`, `Plural`) |
| `gender` | str | Grammatical gender |
| `case` | str | Grammatical case |
| `demonym` | str | Whether the form is a demonym (`Yes`/`No`) |
| `attributes` | str | Shorthand attribute combination (e.g. `A-S-N`) |
| `marked_noun` | str | Associated marked noun form, if any |
