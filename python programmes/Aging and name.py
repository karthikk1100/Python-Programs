import datetime

def year_when_100(age):
    current_year = datetime.datetime.now().year
    year_when_100 = current_year + (100 - age)
    return year_when_100


name = input("Enter your name: ")
age = int(input("Enter your age: "))

year_100 = year_when_100(age)


print(f"Hello {name}, you will turn 100 years old in the year {year_100}.")
