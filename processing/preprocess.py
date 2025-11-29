# processing/preprocess.py
import pandas as pd
import re
import unicodedata

def clean_text(s):
    if pd.isna(s): return s
    s = str(s).strip()
    s = unicodedata.normalize('NFKC', s)
    s = re.sub(r'https?://\S+','', s)
    s = re.sub(r'\s+',' ', s)
    return s

df = pd.read_csv("data/raw_reviews.csv", parse_dates=['date'])
df = df.drop_duplicates(subset=['review_id'])
df['review'] = df['review'].apply(clean_text)
df = df.dropna(subset=['review','rating'])
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
df.to_csv("data/clean_reviews.csv", index=False)
