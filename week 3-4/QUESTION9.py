#making a function that checks the dictionary if there is already an entry for said day and if there is not, adds entry for said day
def add_daily_temp(temps_dict,temperature,day):
    if day not in temps_dict:
        temps_dict[day]=temperature
    return temps_dict

#making an empty dictionary
daily_temperature={}

#adding values for different days in the dictionary
daily_temperature=add_daily_temp(daily_temperature, 20, "Sunday")
daily_temperature=add_daily_temp(daily_temperature, 21, "Monday")
daily_temperature=add_daily_temp(daily_temperature, 22, "Tuesday")
daily_temperature=add_daily_temp(daily_temperature, 19, "Wednesday")
daily_temperature=add_daily_temp(daily_temperature, 24, "Thursday")
print("Daily Temperatures:",daily_temperature)

#adding duplicate days, this should not update the dictionary
daily_temperature=add_daily_temp(daily_temperature, 25, "Sunday")
print("After trying to update temperature for sunday")
print("Daily Temperatures:",daily_temperature)