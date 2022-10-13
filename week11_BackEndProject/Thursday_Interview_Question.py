
# * PROMPT *
# Write a function in python to detect if it's Friday the 13th. The function can accept two parameters. The first parameter will be the number indicating the month, and the second will be the year in four digits. Return True when the month contains a Friday the 13th, else return False.


import datetime
from datetime import datetime
import calendar

def friday13th(month, year):
    date = f'{month} 13 {year}'.format()
    thirteen = datetime.strptime(date, '%m %d %Y').weekday()
    return (calendar.day_name[thirteen]) == "Friday"            # this will return a boolean of either true or false, depending on if the information given contains a friday 13th.

print(friday13th(5,2022))