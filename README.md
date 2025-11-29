# tenxWeek-2: Customer Experience Analytics

## Overview
This information contains the code and data for Task 1: Data Collection and Preprocessing of Google Play Store reviews for three Ethiopian bank apps (CBE, BOA, Dashen Bank).

## Task 1: Data Collection and Preprocessing

### Folder Structure
- `scrape/` : scripts to scrape Google Play Store reviews.
- `processing/` : scripts to clean and preprocess review data.
- `data/` : contains raw and cleaned review CSVs.
- `tests/` : unit tests for preprocessing functions.
- `notebooks/` : optional exploratory analysis notebooks.

### Requirements
Python 3.10+, install dependencies:
```bash
pip install -r requirements.txt

```
### file/folder structure for Task 1
```bash
tenxweek-2/
│
├── README.md                  
├── requirements.txt           # Python dependencies
├── .gitignore
├── data/
│   ├── raw_reviews.csv        # scraped, uncleaned reviews
│   └── clean_reviews.csv      # cleaned & preprocessed reviews
├── scrape/
│   └── scrape_playstore.py    # scraping functions
├── processing/
│   └── preprocess.py          # cleaning functions
├── tests/
│   └── test_preprocess.py     # unit tests for preprocessing
```
### How to run
```
# Scrape reviews:
python scrape/scrape_playstore.py
# Output: data/raw_reviews.csv

# Preprocess reviews:
python processing/preprocess.py
# Output: data/clean_reviews.csv

# Run tests:
pytest tests/
```

## Task 2 : Sentiment and Thematic Analysis

-Quantify review sentiment and extract themes to identify satisfaction drivers and pain points for each bank's mobile app.

### Folder Structure
- additional ```visualiations``` folder is created to visualize theme summary.

### Sentiment Analysis

- Each review is assigned:
    ```sentiment_label (positive, negative, neutral)
    sentiment_score (numeric, e.g., 0–1 or -1–1 depending on method)```
Sentiment is aggregated by bank and rating to identify trends and overall satisfaction levels.

- Outputs:
    ```data/reviews_with_sentiment_hf.csv # cleaned reviews with HuggingFace sentiment labels and scores```

### Thematic / Keyword Extraction

Preprocessing steps: tokenization, stopword removal, lemmatization

TF-IDF: extract significant keywords and n-grams (1–3 words) from reviews

Manual Theme Grouping: Keywords mapped into 3–5 overarching themes per bank:
```
| Theme                           | Example Keywords               |
| ------------------------------- | ------------------------------ |
| **Account Access Issues**       | login, OTP, pin, biometric     |
| **Transaction Performance**     | slow, transfer failed, timeout |
| **User Interface & Experience** | UI, navigation, intuitive      |
| **Crashes & Stability**         | crash, freeze, force close     |
| **Customer Support**            | support, response, call        |
```
Outputs:
    ``` data/top_keywords_per_bank.csv # keywords grouped per bank ```

    ``` data/keywords_with_themes.csv # keywords assigned to themes ```

### Modularity & Reproducibility

Sentiment and thematic analyses are modular scripts, so they can be rerun independently without reprocessing the entire dataset.

Supports updates with new reviews or model improvements.

### Next Steps

Aggregate results to identify top drivers and pain points for each bank.

Visualize sentiment trends and theme distributions for reporting in Task 4.

Use visualizations (bar charts, stacked bars, word clouds) to communicate insights to stakeholders.