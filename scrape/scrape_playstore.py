# scrape/scrape_playstore.py
from google_play_scraper import Sort, reviews_all
import pandas as pd

def scrape_app(app_package, bank_name, min_reviews=400):
    # reviews_all returns list of dicts with keys: content, score, at, userName, reviewId...
    raw = reviews_all(
        app_package,
        lang='en',   
        country='et',
        sort=Sort.MOST_RELEVANT
    )
    df = pd.DataFrame(raw)
    df = df.rename(columns={
        "content": "review",
        "score": "rating",
        "at": "date",
        "reviewId": "review_id"
    })
    df['bank'] = bank_name
    df['app_name'] = app_package
    df['source'] = 'google_play'
    # keep only necessary columns
    df = df[['review_id','review','rating','date','bank','app_name','source']]
    return df

if __name__ == "__main__":
    apps = {
      "Commercial Bank of Ethiopia": "com.combanketh.mobilebanking",  
      "Bank of Abyssinia": "com.boa.boaMobileBanking",
      "Dashen Bank": "com.dashen.dashensuperapp"
    }
    outdfs=[]
    for bank, pkg in apps.items():
        df = scrape_app(pkg, bank)
        if df.shape[0] < 400:
            print(bank, "only", df.shape[0], "reviews — consider running again or expanding country/lang filters")
        outdfs.append(df)
    all_df = pd.concat(outdfs).drop_duplicates(subset=['review_id']).reset_index(drop=True)
    all_df['date'] = pd.to_datetime(all_df['date']).dt.date
    all_df.to_csv("data/raw_reviews.csv", index=False)
