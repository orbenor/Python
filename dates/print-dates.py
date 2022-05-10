from datetime import date, timedelta

# https://www.codegrepper.com/code-examples/python/get+first+and+last+day+of+month+python

last_day_of_prev_month = date.today().replace(day=1) - timedelta(days=1)

start_day_of_prev_month = date.today().replace(day=1) - timedelta(days=last_day_of_prev_month.day)

# For printing results
print(date.today().replace(day=1))
print(timedelta(days=1))
print(timedelta(days=last_day_of_prev_month.day))
print("First day of prev month:", start_day_of_prev_month)
print("Last day of prev month:", last_day_of_prev_month)

print("First day of prev month:", start_day_of_prev_month.strftime('%#d-%#m-%Y'))
