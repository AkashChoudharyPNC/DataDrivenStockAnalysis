import yaml
import pandas as pd
import os

RAW_DIR = "data/raw_yaml"
OUT_DIR = "data/processed_csv"

os.makedirs(OUT_DIR, exist_ok=True)
stock_data = {}

for month in os.listdir(RAW_DIR):
    month_path = os.path.join(RAW_DIR, month)

    if os.path.isdir(month_path):
        for file in os.listdir(month_path):
            if file.endswith(".yaml"):
                with open(os.path.join(month_path, file), "r") as f:
                    data = yaml.safe_load(f)

                # data is a LIST of records
                for record in data:
                    symbol = record["Ticker"]

                    row = {
                        "date": record["date"],
                        "open": record["open"],
                        "high": record["high"],
                        "low": record["low"],
                        "close": record["close"],
                        "volume": record["volume"]
                    }

                    stock_data.setdefault(symbol, []).append(row)

# Save one CSV per stock
for symbol, rows in stock_data.items():
    df = pd.DataFrame(rows)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")
    df.to_csv(f"{OUT_DIR}/{symbol}.csv", index=False)
