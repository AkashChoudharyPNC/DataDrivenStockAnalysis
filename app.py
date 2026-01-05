import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Nifty 50 Stock Dashboard",
    layout="wide"
)

# ---------------- TITLE ----------------
st.markdown(
    """
    <h1 style='text-align: center;'>📊 Nifty 50 Stock Performance Dashboard</h1>
    <p style='text-align: center; color: grey;'>
    Data-driven insights into market trends, sector performance & risk
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ---------------- LOAD DATA ----------------
summary = pd.read_csv("data/market_summary.csv")
sector = pd.read_csv("data/sector_performance.csv")
corr = pd.read_csv("data/stock_correlation.csv", index_col=0)

# ---------------- KPIs ----------------
st.markdown("## 📌 Market Overview")


k1, k2, k3 = st.columns(3)

k1.metric(
    label="🟢 Green Stocks",
    value=(summary.yearly_return > 0).sum()
)

k2.metric(
    label="🔴 Red Stocks",
    value=(summary.yearly_return < 0).sum()
)

k3.metric(
    label="📈 Average Return (%)",
    value=round(summary.yearly_return.mean() * 100, 2)
)

st.markdown("---")

# ---------------- GAINERS & LOSERS ----------------
g1, g2 = st.columns(2)

with g1:
    st.subheader("🚀 Top 10 Gainers")
    st.dataframe(
        summary.sort_values("yearly_return", ascending=False)
               .head(10),
        use_container_width=True
    )

with g2:
    st.subheader("📉 Top 10 Losers")
    st.dataframe(
        summary.sort_values("yearly_return")
               .head(10),
        use_container_width=True
    )

st.markdown("---")

# ---------------- VOLATILITY ----------------
st.subheader("⚠️ High Volatility Stocks (Risk Indicator)")


st.bar_chart(
    summary.sort_values("volatility", ascending=False)
           .head(10)
           .set_index("symbol")["volatility"],
    use_container_width=True
)

st.markdown("---")

# ---------------- SECTOR PERFORMANCE ----------------
st.subheader("🏭 Sector-wise Average Yearly Return")

st.bar_chart(
    sector.set_index("sector")["yearly_return"],
    use_container_width=True
)

st.markdown("---")

# ---------------- CORRELATION ----------------
st.subheader("🔗 Stock Price Correlation (Top Stocks)")

st.caption(
    "Correlation matrix based on daily percentage returns"
)

st.caption("Values close to 1 indicate strong positive correlation")


st.dataframe(
    corr.iloc[:10, :10],
    use_container_width=True
)

st.markdown("---")

# ---------------- FOOTER ----------------
st.markdown(
    "<p style='text-align:center; color: grey;'>"
    "Built with Python & Streamlit | Data-Driven Stock Analysis Project"
    "</p>",
    unsafe_allow_html=True
)
