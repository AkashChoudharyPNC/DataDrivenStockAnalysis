import pandas as pd
import glob

files = glob.glob("data/processed_csv/*.csv")

for file in files:
    df = pd.read_csv(file)
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    df["daily_return"] = df["close"].pct_change()
    df.dropna(inplace=True)

    df.to_csv(file, index=False)
