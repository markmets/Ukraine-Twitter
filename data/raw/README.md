# Raw Data

This directory holds the original, unmodified Twitter data exports.

## Expected Files

| File | Description |
|---|---|
| `ukraine_tweets_YYYY.csv` | Yearly tweet export (one file per year, 2008–2023) |
| `ukraine_tweets_all.xlsx` | Combined dataset across all years |

## Data Format

Each CSV / Excel file should contain at minimum the following columns:

| Column | Type | Description |
|---|---|---|
| `id` | int64 | Unique tweet ID |
| `created_at` | datetime | Tweet creation timestamp (UTC) |
| `text` | str | Full tweet text |
| `lang` | str | Detected language code (e.g. `en`, `uk`, `ru`) |
| `retweet_count` | int | Number of retweets |
| `favorite_count` | int | Number of likes |
| `user_location` | str | User-provided location string |
| `user_followers_count` | int | Follower count at time of tweet |

## Obtaining the Data

The full dataset is not stored in this repository due to file-size limits and Twitter's
Terms of Service. To reproduce the collection step:

1. Obtain Twitter API (v2) access credentials.
2. Store your bearer token in `bearer_token.txt` (this file is git-ignored).
3. Run `notebooks/01_data_collection.ipynb`.
