# theme_summary.py
import pandas as pd

df = pd.read_csv("data/keywords_with_themes.csv")

summary = df.groupby(["bank", "theme"]).size().reset_index(name="count")
summary.to_csv("data/theme_summary.csv", index=False)

print("Saved → data/theme_summary.csv")
