import yfinance as yf

# Prompting user for the share name
STK = input("Enter share name: ")

# Fetching historical market data
data = yf.Ticker(STK).history(period="1d")

# Extracting the last market price
last_market_price = data['Close'].iloc[-1]

# Displaying the last market price
print("Last Market Price:", last_market_price)