import pandas as pd
import glob
import os

dfs = []

files = glob.glob("data/processed_csv/*.csv")

for file in files:
    symbol = os.path.basename(file).replace(".csv", "")
    df = pd.read_csv(file)[["date", "close"]]
    df = df.rename(columns={"close": symbol})
    dfs.append(df.set_index("date"))

price_df = pd.concat(dfs, axis=1)

# Calculate correlation of daily returns
correlation = price_df.pct_change().corr()

correlation.to_csv("data/stock_correlation.csv")
