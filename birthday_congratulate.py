# Task 1. Implement a function to display a list of colleagues you need to congratulate on their birthdays this week

from collections import defaultdict 
from datetime import datetime


def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)
    current_date = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=current_date.year)

        if birthday_this_year < current_date:
            birthday_this_year = birthday.replace(year=current_date.year + 1) #replace the old year with the current year

        delta_days = (birthday_this_year - current_date).days

        if 0 <= delta_days < 7:
            bday = birthday_this_year.strftime("%A")
            if bday == "Saturday" or bday == "Sunday":
                bday = "Monday"
            birthdays_per_week[bday].append(name)
            
    for bday, names in birthdays_per_week.items():
        new_string = ', '.join(names)
        print (bday + ': ' + new_string)
    return birthdays_per_week



get_birthdays_per_week(users= [
    {"name": "Bill Gates", "birthday": datetime(1955, 3, 20)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)},
    {"name": "John Doe", "birthday": datetime(1990, 3, 12)}])




