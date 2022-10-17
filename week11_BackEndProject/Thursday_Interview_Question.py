
# * PROMPT *
# Write a function in python to detect if it's Friday the 13th. The function can accept two parameters. The first parameter will be the number indicating the month, and the second will be the year in four digits. Return True when the month contains a Friday the 13th, else return False.


# import datetime
# from datetime import datetime
# import calendar

# def friday13th(month: int, year: int) -> bool:
#     date = f'{month} 13 {year}'.format()                        # this takes the given info and sets up the date to look like, for example, '5 13 2022' and sets it in a format that we can check below
#     thirteen = datetime.strptime(date, '%m %d %Y').weekday()    # this is using the strptime method to check which day of the week the 13th lands on
#     return (calendar.day_name[thirteen]) == "Friday"            # this will return a boolean of either true or false, depending on if the information given contains specifically a FRIDAY 13th.

# print(friday13th(5,2022))



# def has_friday_13(month, year):
#     spooky = datetime.date(year, month, day)
#     return spooky.strftime("%A") == "Friday"
# print(has_friday_13(5,2022))