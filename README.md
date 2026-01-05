# 📊 Data-Driven Stock Analysis Dashboard (Nifty 50)

## 📌 Project Overview
This project performs an end-to-end data analysis of Nifty 50 stocks using daily OHLCV market data.
Raw stock data provided in YAML format is transformed, cleaned, analyzed, and visualized using an
interactive Streamlit dashboard to generate actionable market insights.

The project demonstrates a complete data pipeline — from raw data ingestion to analytical dashboards —
following real-world data engineering and analytics practices.

---

DataDrivenStockAnalysis/
│
├── app.py                     # Streamlit dashboard application
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
├── .gitignore                 # Ignored files and folders
│
├── data/
│   ├── raw_yml/               # Raw stock data files (YAML format)
│   ├── processed_csv/         # Cleaned stock-wise CSV files
│   ├── market_summary.csv     # Stock-level performance metrics
│   ├── sector_performance.csv # Sector-wise average yearly returns
│   ├── stock_correlation.csv  # Stock price correlation matrix
│   └── sector_mapping.csv     # Stock-to-sector mapping file
│
├── scripts/
│   ├── yaml_to_csv.py         # Convert raw YAML data to CSV format
│   ├── data_cleaning.py       # Data cleaning & daily return calculation
│   ├── analysis.py            # Market & sector-wise analysis
│   ├── correlation.py         # Stock correlation analysis
│   └── cumulative_return.py   # Cumulative return calculation (Top 5 stocks)


---

## 🛠️ Tech Stack
- Python
- Pandas
- NumPy
- Streamlit
- Matplotlib
- YAML
- Power BI (optional extension)

---

## 🔄 Data Pipeline
1. Ingest raw YAML stock data
2. Convert YAML files to CSV format
3. Clean data and calculate daily returns
4. Generate market-level performance metrics
5. Perform sector-wise analysis
6. Compute stock correlation matrix
7. Calculate cumulative returns for top stocks
8. Visualize insights using Streamlit dashboard

---

## 📈 Key Features
- Market overview (Green vs Red stocks)
- Top 10 gainers and losers
- Volatility-based risk analysis
- Sector-wise average yearly returns
- Stock price correlation matrix
- Cumulative returns for top-performing stocks
- Clean, professional Streamlit dashboard

---

## ▶️ How to Run

### Install dependencies
pip install -r requirements.txt

### Execute data pipeline (run in order)
python scripts/yaml_to_csv.py
python scripts/data_cleaning.py
python scripts/analysis.py
python scripts/correlation.py
python scripts/cumulative_return.py

### Launch dashboard
python -m streamlit run app.py

---

## 📊 Output
An interactive Nifty 50 Stock Performance Dashboard displaying:
- Market trends
- Sector performance
- Risk indicators
- Correlation insights

---

## 🎯 Use Cases
- Financial market analysis
- Investment insight generation
- Data analyst / data engineering portfolio project
- Interview and live evaluation demonstration

---

## 👤 Author
Akash Choudhary  
Data Analyst | Python | SQL | Data Visualization
