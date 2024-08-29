

from alpaca.trading.client import TradingClient

import yfinance as yf
import pandas as pd

# Define a list of stocks to check
tickers = ["AAPL", "MSFT", "GOOG", "AMZN", "TSLA", "NVDA","BTC"]

# Get data for the last week for each stock
data = yf.download(tickers, start="2024-08-10", end="2024-08-17")

# Calculate weekly percentage change for each stock
weekly_changes = {}
for ticker in tickers:
    first_price = data['Adj Close'][ticker].iloc[0]
    last_price = data['Adj Close'][ticker].iloc[-1]
    weekly_change = (last_price - first_price) / first_price * 100
    weekly_changes[ticker] = weekly_change

# Convert to DataFrame for better display
weekly_changes_df = pd.DataFrame(list(weekly_changes.items()), columns=['Ticker', 'Weekly Change (%)'])

# Sort by top gainers and losers
top_gainers = weekly_changes_df.sort_values('Weekly Change (%)', ascending=False).head()
top_losers = weekly_changes_df.sort_values('Weekly Change (%)', ascending=True).head()

print("Top Weekly Gainers:\n", top_gainers)
print("\nTop Weekly Losers:\n", top_losers)