from modules.share_price_fetcher import SharePriceFetcher

# Example usage
if __name__ == "__main__":
    symbol_to_fetch = "VOTLAS.NS"  # Replace with the symbol of the NSE stock you want to fetch

    share_price_fetcher = SharePriceFetcher(symbol_to_fetch)

    current_price = share_price_fetcher.get_current_price()
    print(f"Current Price for {symbol_to_fetch}: {current_price}")

    start_date = "2023-09-15"  # Replace with the start date (YYYY-MM-DD format)
    end_date = "2023-09-16"    # Replace with the end date (YYYY-MM-DD format)

    historical_prices = share_price_fetcher.get_historical_prices(start_date, end_date)
    print(f"Historical Prices for {symbol_to_fetch} from {start_date} to {end_date}:\n{historical_prices}")
