import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from data.fetch_stock import get_stock_data
from cache.redis_cache import get_cache, set_cache
from analysis.groq_analysis import stock_analysis

st.title("Live Stock Analysis")

st.sidebar.title("Controls")
ticker = st.sidebar.text_input("Enter Ticker")
period = st.sidebar.selectbox("Select Period", ["1mo", "3mo", "6mo", "1y", "2y"])
fetch_btn = st.sidebar.button("Fetch Data")

if 'data' not in st.session_state:
    st.session_state.data = None

if fetch_btn:
    key = f"{ticker}_{period}"
    data = get_cache(key)
    if data is None:
        data = get_stock_data(ticker, period)
        data.columns = [col[0] for col in data.columns]
        set_cache(key, data)
    elif isinstance(data.columns, pd.MultiIndex):
        data.columns = [col[0] for col in data.columns]
    st.session_state.data = data

if st.session_state.data is not None:

    data = st.session_state.data

    latest_close = float(data['Close'].iloc[-1])
    first_close = float(data['Close'].iloc[0])
    period_high = float(data['High'].max())
    period_low = float(data['Low'].min())
    price_change = ((latest_close - first_close) / first_close) * 100

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Latest Close", f"${latest_close:.2f}")
    col2.metric("Price Change", f"{price_change:.2f}%")
    col3.metric("Period High", f"${period_high:.2f}")
    col4.metric("Period Low", f"${period_low:.2f}")

    candle = go.Candlestick(
        x=data.index,
        open=data['Open'],
        high=data['High'],
        low=data['Low'],
        close=data['Close']
    )
    fig = go.Figure(data=[candle])
    fig.update_layout(title=f"{ticker} Price Chart")
    st.plotly_chart(fig)

    volume = px.bar(x=data.index, y=data['Volume'], title="Volume")
    st.plotly_chart(volume)

    st.subheader("AI Analysis")
    user_question = st.text_input("Ask AI about this stock")
    ask_btn = st.button("Ask AI")
    if ask_btn:
        with st.spinner("Analyzing..."):
            response = stock_analysis(data, user_question, ticker)
            st.write(response)