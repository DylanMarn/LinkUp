# Dylan Marn

'''
LinkedUp: An app designed to help far away friends...
    allow users to link up whenever possible and make the most of their time,
    by making the plans easy so they can make the memories


'''

import re

# class User stores data about each user
class User:
    def __init__(self, name, location, startdate, enddate):
        self.name = name
        self.location = location
        self.startdate = startdate
        self.enddate = enddate

def main():


    user1 = user()
    ...


## create functions to get user input(name, location and dates) for 2+ users

def user():

    name = None
    while not name:
        name = get_name(input("What is your name? "))
        while True:
            print(f"Hello {name},") 
            response = input("is this how your would like to be addressed? (Y/N)").upper()
            if response == "Y": # if confirmed, continue
                break
            elif response == "N": # if denied, reset end date
                name = None
                break

    s_date = None # initalize start date to nothing
    while not s_date: # loop until valid start date
        s_date = get_date(input("Start date: "))
        if s_date: # if valid start date, confirm with user
            while True: # loop until user confirms or denies
                print(f"The start of your trip is {s_date} %YYYY-MM-DD%")
                response = input("Is this correct? (Y/N) ").upper()
                if response == "Y": # if confirmed, continue
                    break
                elif response == "N": # if denied, reset start date
                    s_date = None
                    break


    e_date = None # initalize end date to nothing
    while not e_date: # loop until valid end date
        e_date = get_date(input("End date: "))
        if e_date: # if valid start date, confirm with user
            while True: # loop until user confirms or denies
                print(f"The end of your trip is {e_date} %YYYY-MM-DD%")
                response = input("Is this correct? (Y/N) ").upper()
                if response == "Y": # if confirmed, continue
                    break
                elif response == "N": # if denied, reset end date
                    e_date = None
                    break

## create a function to get user name

def get_name(name):
    name = name.strip().title()
    return name 

## create a function to get user location

def get_location():

    ...

## create a function to get user date, returned in standard form

def get_date(date):
    # create a dict of months and corresponding number
    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12
        }
    # test for date in MonthName DD, YYYY format
    matches1 = re.search(r"^(.+) (\d{1,2}),? (\d{1,4})$", date, re.IGNORECASE)
    if matches1:
        try: # match input month to corresponding number
            month = int(months[matches1.group(1)])
        except: # if invalid month surpress error
            print("Invalid month name")
            return None
        day = int(matches1.group(2))
        year = int(matches1.group(3))

    # test for date in MM/DD/YYYY format
    matches2 = re.search(r"^(\d{1,2})[/-](\d{1,2})[/-](\d{1,4})$", date, re.IGNORECASE)
    if matches2:
        month = int(matches2.group(1))
        day = int(matches2.group(2))
        year = int(matches2.group(3))

    try: # test input for calendar date bounds
        if 1 <= month <= 12 and 1 <= day <= 31: # narrow bounds, only 12 months with max 31 days
            if month in [4,6,9,11] and day == 31: # months with only 30 days
                print("Invalid days for given month")
                return None
            elif month == 2 and day > 29 and year%4 == 0: # February on leap years
                print("Invalid days for given month")
                return None
            elif month == 2 and day > 28 and year%4 != 0: # February on non-leap years
                print("Invalid days for given month")
                return None
            else: # if input satisfies all bounds
                print(year, f"{month:02}", f"{day:02}", sep="-")
                return f"{year}-{month}-{day}"
    except:
        pass

    # if none of the above can be completed, provide user a hint
    print("Invalid date - Valid forms of date include")
    print("1 MM/DD/YYYY")
    print("2 MM-DD-YYYY")
    print("3 Month DD, YYYY")

## create a funtion to determine if two users have overlapping dates in the same location
def overlap():

    ...


## create a function that tells the user with who and when they can LinkUP
def LinkUp():

    ...


if __name__ == "__main__":
    main()