import csv
import json
from modules.calculate_sip_returns import calculate_sip_returns

def read_config_from_file(config_file):
    try:
        with open(config_file, "r") as file:
            config_data = json.load(file)
            return config_data
    except FileNotFoundError:
        print(f"Config file '{config_file}' not found.")
        return {}

def main():
    # Specify the path to your JSON config file
    config_file = "config.json"
    
    # Read config data from the config file
    config_data = read_config_from_file(config_file)
    
    if not config_data:
        print("No config data found in the config file.")
        return
    
    symbols = config_data.get("symbols", [])
    start_date = config_data.get("start_date", "")
    sip_amount = config_data.get("sip_amount", 0)
    months = config_data.get("months", 0)
    
    # Initialize a list to store results for all symbols
    all_results = []    
    i=0
    
    for symbol in symbols:
        print(f"{i}: Calculating SIP returns for {symbol}...")
        i = i + 1
        # Calculate SIP returns for the current symbol
        (total_investment, total_units_purchased, current_price, current_value, sip_returns) = calculate_sip_returns(symbol, start_date, sip_amount, months)
        
        # Create a dictionary to store the results
        result_dict = {
            "Symbol": symbol,
            "Start Date": start_date,
            "SIP Amount": sip_amount,
            "Months": months,
            "Total Investment": total_investment,
            "Total Units Purchased": total_units_purchased,
            "Current Price": current_price,
            "Current Value": current_value,
            "Anualized Returns": sip_returns
        }
        
        all_results.append(result_dict)
    
    # Write the results to a CSV file
    with open("sip_returns.csv", mode="w", newline="") as csv_file:
        fieldnames = ["Symbol", "Start Date", "SIP Amount", "Months", "Total Investment", "Total Units Purchased", "Current Price", "Current Value", "Anualized Returns"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()  # Write the header row
        
        for result in all_results:
            writer.writerow(result)  # Write each result as a row in the CSV file

# Example usage
if __name__ == "__main__":
    main()
