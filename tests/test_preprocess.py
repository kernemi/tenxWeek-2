import pandas as pd
import pytest

@pytest.fixture
def load_clean_data():
    """Load preprocessed reviews CSV for testing"""
    df = pd.read_csv("data/clean_reviews.csv")
    return df

def test_total_reviews(load_clean_data):
    """Check that we have at least 1200 reviews"""
    df = load_clean_data
    assert len(df) >= 1200, f"Only {len(df)} reviews, expected at least 1200."

def test_missing_values(load_clean_data):
    """Check that missing values are <5% of total rows for key columns"""
    df = load_clean_data
    total_rows = len(df)
    key_cols = ['review', 'rating', 'date', 'bank', 'app_name']
    missing_count = df[key_cols].isnull().sum().sum()
    missing_percentage = (missing_count / (total_rows * len(key_cols))) * 100
    assert missing_percentage < 5, f"Missing values too high: {missing_percentage:.2f}%"
