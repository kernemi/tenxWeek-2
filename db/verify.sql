-- Count reviews per bank
SELECT bank_id, COUNT(*) FROM reviews GROUP BY bank_id;

-- Average rating per bank
SELECT bank_id, AVG(rating) FROM reviews GROUP BY bank_id;

-- Sentiment breakdown
SELECT bank_id, sentiment_label, COUNT(*)
FROM reviews
GROUP BY bank_id, sentiment_label;
