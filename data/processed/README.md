# Processed Data

This directory holds cleaned and aggregated datasets derived from the raw data, used as direct inputs by the analysis notebooks.

## Files

| File | Derived from | Description |
|---|---|---|
| `pivotUkraine_SUM_excelInput_weekly.csv` | `raw/28languagesUA.csv` | Pivoted weekly sums of the `freq` column per language (languages as rows, week-start dates as columns) |
| `All_cases_allmetadata.csv` | `raw/28languagesUA.csv` | Per-query-form dataset with full linguistic metadata (case, gender, plurality, etc.) for the comparative plot |

## Data Format

### `pivotUkraine_SUM_excelInput_weekly.csv`

Languages as rows, ISO week-start dates (`YYYY-MM-DD`) as columns. Values are the sum of daily `freq` values within each week.

| Column | Description |
|---|---|
| `language` | Language name (index column) |
| `<YYYY-MM-DD>` | Weekly sum of relative frequency for that language |

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
