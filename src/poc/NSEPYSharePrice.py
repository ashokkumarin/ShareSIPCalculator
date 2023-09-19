from nsepy import get_history
from datetime import date

# Define the NSE stock symbol you want to fetch data for
nse_symbol = "TVSMOTOR"  # Replace with the symbol of the stock you want to fetch
date_to_check = "2023-09-15"  # Replace with the date you're interested in (YYYY-MM-DD format)

# Fetch current data
current_data = get_history(symbol=f"{nse_symbol}", start=date.today(), end=date.today())

# Fetch historical data for the specified date
historical_data = get_history(symbol=f"{nse_symbol}", start=date_to_check, end=date_to_check)

# Extract the current price and the closing price for the specified date
current_price = current_data["Close"].values[0]
closing_price = historical_data['Close'].values[0]

# Print the current price and the closing price for the specified date
print("# # # # # # # # # # # # # # # # # # # #")
print(f"Current price: {current_price}")
print(f"Closing price for {date_to_check}: {closing_price}")
print("# # # # # # # # # # # # # # # # # # # #")
