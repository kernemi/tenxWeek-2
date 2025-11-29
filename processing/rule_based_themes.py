# rule_based_themes.py
import pandas as pd

df = pd.read_csv("data/top_keywords_per_bank.csv")

themes = {
    "Account Access Issues": [
        "login", "login error", "password", "signin", "account locked"
    ],
    "Transaction Performance": [
        "slow", "delayed", "transfer", "transaction failed", "network error"
    ],
    "UI/UX": [
        "easy use", "good ui", "interface", "design"
    ],
    "Customer Support": [
        "support", "help", "response", "service"
    ],
    "Features / Requests": [
        "update", "add feature", "notification", "statement"
    ]
}

def map_theme(keyword):
    for theme, words in themes.items():
        for w in words:
            if w in keyword:
                return theme
    return "Other"

df['theme'] = df['keyword'].apply(map_theme)

df.to_csv("data/keywords_with_themes.csv", index=False)
print("Saved rule-based themes → data/keywords_with_themes.csv")
