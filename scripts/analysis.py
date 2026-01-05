import pandas as pd
import glob
import os

# ================================
# MARKET SUMMARY
# ================================

summary = []
files = glob.glob("data/processed_csv/*.csv")

for file in files:
    symbol = os.path.basename(file).replace(".csv", "").upper()
    df = pd.read_csv(file)

    yearly_return = (df["close"].iloc[-1] - df["close"].iloc[0]) / df["close"].iloc[0]
    volatility = df["daily_return"].std()

    summary.append({
        "symbol": symbol,
        "yearly_return": yearly_return,
        "volatility": volatility,
        "avg_price": df["close"].mean(),
        "avg_volume": df["volume"].mean()
    })

summary_df = pd.DataFrame(summary)
summary_df.to_csv("data/market_summary.csv", index=False)

# ================================
# SECTOR WISE PERFORMANCE
# ================================

sector_raw = pd.read_csv("data/sector_mapping.csv")

sector_raw["symbol"] = (
    sector_raw["Symbol"]
    .astype(str)
    .apply(lambda x: x.split(":")[-1].strip().upper())
)

sector_df = sector_raw[["symbol", "sector"]]

# -------- FINAL ALIAS FIX --------
alias_map = {
    "ADANIENT": "ADANIGREEN",
    "BHARTIARTL": "AIRTEL",
    "TATACONSUM": "TATACONSUMER",
    "BRITANNIA": "BRITANNIA"
}

summary_df["symbol"] = summary_df["symbol"].replace(alias_map)

# Merge
sector_merged = summary_df.merge(
    sector_df, on="symbol", how="left"
)
sector_merged["sector"] = sector_merged["sector"].fillna("UNKNOWN")


print("Matched rows:", sector_merged.shape[0])

# Aggregate
sector_performance = (
    sector_merged
    .groupby("sector")["yearly_return"]
    .mean()
    .reset_index()
)

sector_performance.to_csv(
    "data/sector_performance.csv", index=False
)
