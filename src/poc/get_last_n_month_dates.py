from datetime import datetime, timedelta

def get_dates_last_N_months(start_date, months):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")  # Convert the start date to a datetime object
    day_fixed = start_date.day                              # Get the day from the start date
    dates_last_N_months = []                                # Initialize a list to store the result dates

    dates_last_N_months.append(start_date)  
    # Calculate and store the dates for the last N months with the same day as the start date
    for i in range(months-1):
        # Calculate the new date by subtracting one month, keeping the same day as the start_date
        new_date = start_date - timedelta(days=start_date.day) # Calculate the new date by subtracting one month from the start date
        
        if (day_fixed < new_date.day):                          # Check if the day of the start date is greater than the day of the new date
            new_date = new_date.replace(day=day_fixed)          # If yes, replace the day of the new date with the day of the start date (to avoid issues with months with less than 31 days
        
        dates_last_N_months.append(new_date)                # Append the new date to the result list
        start_date = new_date - timedelta(days=1)           # Update the start_date for the next iteration

    return dates_last_N_months

# Example usage: Get dates for the last 10 months with the same day as the start date
start_date = "2023-08-31"  # Replace with your desired start date (YYYY-MM-DD format)
months = 15                # Number of months to calculate
dates = get_dates_last_N_months(start_date, months)

for date in dates:
    print(date.strftime("%Y-%m-%d"))
