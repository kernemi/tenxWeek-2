# tenxWeek-2: Customer Experience Analytics
## Task 1

### Overview
This information contains the code and data for Task 1: Data Collection and Preprocessing of Google Play Store reviews for three Ethiopian bank apps (CBE, BOA, Dashen Bank).

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
