import yfinance as yf
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Stock Price App", page_icon="📈", layout='wide')
st.write("""
         # Simple Stock Price App
         
         Shown are the stock **open price**, **high Price**, **low price** and **close price** of Google!
         
         """)

# Define the ticker symbol
tickerSymbol = 'GOOGL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
tickerDf = tickerData.history(period='1y', start='2023-12-31', end='2024-12-31')

col1, col2 = st.columns(2)
# Open High Low Close Volume Dividends Stock Splits
with col1:
    st.write("""
             ### Open Price
             """)
    st.line_chart(tickerDf.Open)
    st.write("""
             ### High Price
             """)
    st.line_chart(tickerDf.High)

with col2:
    st.write("""
             ### Low Price
             """)
    st.line_chart(tickerDf.Low)
    st.write("""
         ### Closing Price
         """)
    st.line_chart(tickerDf.Close)
