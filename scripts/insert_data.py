import pandas as pd
import psycopg2

df = pd.read_csv("data/reviews_with_sentiment_hf.csv")

conn = psycopg2.connect(
    dbname="bank_reviews",
    user="postgres",
    password="yourpassword",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Insert banks 
banks = {
    "CBE": 1,
    "BOA": 2,
    "Dashen": 3,
}

for bank, bank_id in banks.items():
    cursor.execute(
        "INSERT INTO banks (bank_id, bank_name, app_name) VALUES (%s, %s, %s) ON CONFLICT DO NOTHING;",
        (bank_id, bank, f"{bank} Mobile App")
    )

# Insert reviews
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO reviews (bank_id, review_text, rating, review_date, sentiment_label, sentiment_score, source)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """, (
        banks[row['bank']],
        row['review'],
        int(row['rating']),
        row['date'],
        row['sentiment_label'],
        float(row['sentiment_score']),
        row['source']
    ))

conn.commit()
cursor.close()
conn.close()
