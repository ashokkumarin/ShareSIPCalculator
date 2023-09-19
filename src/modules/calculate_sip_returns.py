from modules.share_price_fetcher import SharePriceFetcher
from modules.get_next_n_month_dates import get_dates_next_N_months

def calculate_sip_returns(symbol, start_date, sip_amount, months):
    share_price_fetcher = SharePriceFetcher(symbol)
    dates = get_dates_next_N_months(start_date, months)

    # Initialize variables for calculating returns
    total_investment = 0
    total_units_purchased = 0

    for date in dates:
        closing_price = share_price_fetcher.get_historical_prices(date.strftime("%Y-%m-%d"))    # Fetch historical data for the current month
        if closing_price > 0:
            units_purchased = sip_amount // closing_price                                           # Calculate units purchased for the current month (using integer division)
            
            # Update total investment and units purchased
            total_investment += units_purchased * closing_price                 # Calculate investment for the current month
            total_units_purchased += units_purchased                            # Update total units purchased
        
    current_price = share_price_fetcher.get_current_price()                 # Fetch the current price of the stock
    current_value = total_units_purchased * current_price                   # Calculate the current value of the investment
    returns = (current_value - total_investment) / total_investment         # Calculate SIP returns
    
    #print(f"Total investment: {total_investment}, Total units purchased: {total_units_purchased}, Current price: {current_price}, Current value: {current_value}, Returns: {returns}")

    return total_investment, total_units_purchased, current_price, current_value, returns