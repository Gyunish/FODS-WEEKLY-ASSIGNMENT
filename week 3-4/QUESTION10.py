#making a function that takes input of the daily temperature from the user for each day of the week and returns a dictionary that contains the info
def get_daily_temps():
    days_of_week=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]   #list of days
    daily_temperature={}
    for day in days_of_week:    #running for loop through list of days
        while True:
            try:
                temperature=float(input("Enter the average temperature of "+day))   #asking for user input
                break
            except ValueError:
                print("Please enter valid temperature.")
        daily_temperature[day] = temperature    #putting user input in dictionary with corresponding day
    return daily_temperature    #returning dictionary

daily_temperature=get_daily_temps()
print("Daily Temperatures:",daily_temperature)