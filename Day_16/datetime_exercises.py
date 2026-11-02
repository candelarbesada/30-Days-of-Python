# Day 16

from datetime import datetime, timedelta
today = datetime.now()
print(f'Day: {today.day}. Month: {today.month}. Year: {today.year}. Hour: {today.hour}. Minute: {today.minute}. Timestamp: {today.timestamp()}')
print(f"Formatted date: {today.strftime("%m/%d/%Y, %H:%M:%S")}")
string_date = "Today is 5 December, 2019"
print(f"Formatted string: {datetime.strptime(string_date, 'Today is %d %B, %Y')}")

ny = datetime(2027, 1, 1, 0, 0, 0)
print(f"Time difference between now and New Year: {ny - today}")

print(f"Time difference between 1 January 1970 and now is {timedelta(seconds=today.timestamp())}")