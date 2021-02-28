import datetime

x = datetime.datetime.now()
# Print date in readable format. Displayed format is day, date-month-year hour:minute:second local_timezone
print(x.strftime("%A, %d-%m-%Y %H:%M:%S %Z"))
