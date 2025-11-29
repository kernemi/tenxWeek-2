# keywords_per_bank.py
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("data/reviews_with_sentiment_hf.csv")

banks = df['app_name'].unique()
all_results = []

for bank in banks:
    print(f"Processing: {bank}")
    df_bank = df[df['app_name'] == bank]

    vectorizer = TfidfVectorizer(
        ngram_range=(1,3),
        stop_words='english',
        max_features=2000
    )

    X = vectorizer.fit_transform(df_bank['review'].fillna(''))
    feature_names = np.array(vectorizer.get_feature_names_out())
    
    tfidf_sum = np.asarray(X.sum(axis=0)).ravel()
    top_idx = tfidf_sum.argsort()[-40:][::-1]
    top_terms = feature_names[top_idx]

    # Save per bank
    pd.DataFrame(top_terms, columns=["keyword"]).to_csv(
        f"data/keywords_{bank}.csv", index=False
    )

    all_results.append(pd.DataFrame({
        "bank": bank,
        "keyword": top_terms
    }))

# Save combined
combined = pd.concat(all_results)
combined.to_csv("data/top_keywords_per_bank.csv", index=False)

print("Saved per bank and combined keywords.")
