from datetime import datetime, timedelta

def get_first_day_of_next_month(start_date):
    delta =  (31 - start_date.day) + 1 # Calculate the number of days to be added to the start date to get the last day of the month
    new_date = start_date + timedelta(days=delta) # Calculate the new date by adding the delta to the start date
    new_date = new_date - timedelta(days=new_date.day) # Calculate the new date by subtracting one month from the start date
    new_date = new_date + timedelta(days=1) # Add one day to get the first day of the next month
    
    return new_date
    
def get_last_day_of_next_month(start_date):
    delta =  (31 - start_date.day) + 1 # Calculate the number of days to be added to the start date to get the last day of the month
    new_date = start_date + timedelta(days=delta) # Calculate the new date by adding the delta to the start date
    new_date = new_date - timedelta(days=new_date.day) # Calculate the new date by subtracting one month from the start date    
    
    return new_date

def get_dates_next_N_months(start_date, months):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")  # Convert the start date to a datetime object
    day_fixed = start_date.day                              # Get the day from the start date
    dates_next_N_months = []                                 # Initialize a list to store the result dates

    dates_next_N_months.append(start_date)  
    # Calculate and store the dates for the next N months with the same day as the start date
    for i in range(months-1):
        # Calculate the new date by adding one month, keeping the same day as the start_date
        next_month_first_day = get_first_day_of_next_month(start_date)  # Get the first day of the next month
        next_month_last_day = get_last_day_of_next_month(next_month_first_day) # Get the last day of the next month
        
        new_date = next_month_first_day # Calculate the new date by adding one month to the start date
        
        # Adjust the day to day_fixed if needed
        if day_fixed > next_month_last_day.day:
            new_date = new_date.replace(day=next_month_last_day.day)
        else:
            new_date = new_date.replace(day=day_fixed)
        
        dates_next_N_months.append(new_date)                # Append the new date to the result list
        start_date = new_date                               # Update the start_date for the next iteration

    return dates_next_N_months
