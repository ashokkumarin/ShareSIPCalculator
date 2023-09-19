import yfinance as yf

class SharePriceFetcher:
    def __init__(self, symbol):
        self.symbol = symbol
        self.stock = yf.Ticker(symbol)

    def get_current_price(self):
        try:
            current_data = self.stock.info
            return current_data.get("last_price")
        except Exception as e:
            return f"Error fetching current price: {str(e)}"

    def get_historical_prices(self, start_date, end_date):
        try:
            historical_data = self.stock.history(start=start_date, end=end_date)
            return historical_data
        except Exception as e:
            return f"Error fetching historical prices: {str(e)}"
