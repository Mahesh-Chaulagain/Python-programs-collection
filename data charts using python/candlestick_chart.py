import yfinance as yf
import mplfinance as mpf

# Define the stock symbol and date range
symbol = input("Enter Stock Name: ")
start_date = "2022-01-01"
end_date = "2023-10-13"

# Fetch stock data
stock_data = yf.download(symbol,start=start_date, end=end_date)
print(stock_data)

# Create the candlestick chart
# mpf.plot(stock_data, type='candle', style='yahoo', title=f'{symbol} CandleStick Chart')