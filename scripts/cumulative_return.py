import pandas as pd
import glob
import os

# Load market summary
summary = pd.read_csv("data/market_summary.csv")

# Get top 5 stocks by yearly return
top5_symbols = summary.sort_values(
    "yearly_return", ascending=False
).head(5)["symbol"].tolist()

# Process only top 5
for file in glob.glob("data/processed_csv/*.csv"):
    symbol = os.path.basename(file).replace(".csv", "")

    if symbol in top5_symbols:
        df = pd.read_csv(file)

        df["cumulative_return"] = (1 + df["daily_return"]).cumprod()

        df.to_csv(file, index=False)
