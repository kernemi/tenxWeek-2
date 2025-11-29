from transformers import pipeline
import pandas as pd

classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english", device=-1)
df = pd.read_csv("data/clean_reviews.csv")
def hf_batch_predict(texts):
    out = classifier(texts, truncation=True)
    # out is list of dicts {label, score}
    return out

# process in batches
results=[]
batch_size=16
for i in range(0, len(df), batch_size):
    batch = df['review'].iloc[i:i+batch_size].tolist()
    results.extend(hf_batch_predict(batch))

df['hf_label'] = [r['label'].lower() for r in results]
df['hf_score'] = [r['score'] for r in results]
df.to_csv("data/reviews_with_sentiment_hf.csv", index=False)
