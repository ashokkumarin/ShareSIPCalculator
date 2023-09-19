import yfinance as yf
from datetime import date, timedelta, datetime

# Define the NSE stock symbol you want to fetch data for
nse_symbol = "VOLTAS"  # Replace with the symbol of the stock you want to fetch
start_date = "2022-09-19"  # Replace with the date you're interested in (YYYY-MM-DD format)
end_date = (datetime.strptime(start_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d")

# Create a Ticker object for the NSE stock
nse_stock = yf.Ticker(f"{nse_symbol}.NS")

# Fetch historical data for the specified date
historical_data = nse_stock.history(start=start_date, end=end_date)

if historical_data is not None:
    # Extract the closing price for the specified date
    closing_price = historical_data['Close'].values[0]
else:
    print(f"* * * Historical Data is Null * * *")
    closing_price = 0

# Fetch current data
current_data = nse_stock.info
current_price = current_data["currentPrice"]

# Print the current price
print("# # # # # # # # # # # # # # # # # # # #")
print(f"Current price: {current_price}")

# Print the closing price for the specified date
print(f"Closing price for {start_date}: {closing_price}")
print("# # # # # # # # # # # # # # # # # # # #")