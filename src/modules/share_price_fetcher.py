import yfinance as yf
from datetime import timedelta, datetime

class SharePriceFetcher:
    def __init__(self, symbol):
        self.symbol = symbol
        self.stock = yf.Ticker(f"{symbol}.NS")

    def get_current_price(self):
        try:
            current_data = self.stock.info
            return current_data["currentPrice"]
        except Exception as e:
            print (f"Error fetching current price: {str(e)}")
            raise e # Raise the exception to the caller

    def get_historical_prices(self, start_date):
        historical_date = datetime.strptime(start_date, "%Y-%m-%d")
        today = datetime.today()
        end_date = (historical_date + timedelta(days=5)).strftime("%Y-%m-%d")
        
        if historical_date >= today: # Check if the start date is in the future
            self.get_current_price()
        else:
            try:
                historical_data = self.stock.history(start=start_date, end=end_date)
                if (len(historical_data['Close'].values) == 0):
                    return 0
                else:
                    return historical_data['Close'].values[0]
            except Exception as e:
                print (f"Error fetching historical prices: {str(e)}")
                raise e # Raise the exception to the caller
