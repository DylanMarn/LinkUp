# Dylan Marn

'''
LinkedUp: An app designed to help far away friends...
    allow users to link up whenever possible and make the most of their time,
    by making the plans easy so they can make the memories


'''

import re
from datetime import date

# class Trip stores important trip data
class Trip:
    def __init__(self, name, location, startdate, enddate, days=0):
        self.name = name
        self.location = location
        self.startdate = startdate
        self.enddate = enddate
        self.days = days
    
    def __str__(self):
        return f"{self.name} is traveling to {self.location} from {self.startdate} to {self.enddate}"

def main():
    print("Please fill out the following for user #1")
    user1 = set_user()
    print(f"\nPlease fill out the following for user #2")
    user2 = set_user()

    overlap = linkUp(user1, user2)
    try: # in case overlap = None
        if overlap.days > 0: # if overlapping time
            print(user1)
            print(user2)
            print(f"{overlap.name} will both be in {overlap.location} from {overlap.startdate} to {overlap.enddate}")
            print(f"{overlap.days} days to make memories")
        else: # if no overlapping time
            print(f"There is no overlapping time between {user1.name}'s and {user2.name}'s trips")
    except:
        pass


## create functions to get user input(name, location and dates) for 2+ users

def set_user():
    name = None # initalize name to nothing
    while not name: # loop until valid name
        name = get_name(input("What is your name? "))
        if name: # if valid name, confirm with user
            while True: # loop until user confirms or denies
                response = input(f"Hello {name}, is this how you would like to be addressed? (Y/N)").upper()
                if response == "Y": # if confirmed, continue
                    break
                elif response == "N": # if denied, reset name
                    name = None
                    break
                else:
                    print("Invalid response")

    location = None # initalize state to nothing
    while not location: # loop until valid state
        location = get_location(input("Where are you traveling to? "))
        if location: # if valid state, confirm with user
            while True: # loop until user confirms or denies
                response = input(f"{name}, it appears you are traveling to {location}, is this correct? (Y/N)").upper()
                if response == "Y": # if confirmed, continue
                    break
                elif response == "N": # if denied, reset state
                    location = None
                    break
                else:
                    print("Invalid response")

    s_date = None # initalize start date to nothing
    while not s_date: # loop until valid start date
        s_date = get_date(input("Start date: "))
        if s_date: # if valid start date, confirm with user
            while True: # loop until user confirms or denies
                print(f"The start of your trip is {date(*s_date)} %YYYY-MM-DD%")
                response = input("Is this correct? (Y/N) ").upper()
                if response == "Y": # if confirmed, continue
                    break
                elif response == "N": # if denied, reset start date
                    s_date = None
                    break
                else:
                    print("Invalid response")


    e_date = None # initalize end date to nothing
    while not e_date: # loop until valid end date
        e_date = get_date(input("End date: "))
        try:
            if (date(*e_date) - date(*s_date)).days >= 0:
                if e_date: # if valid start date, confirm with user
                    while True: # loop until user confirms or denies
                        print(f"The end of your trip is {date(*e_date)} %YYYY-MM-DD%")
                        response = input("Is this correct? (Y/N) ").upper()
                        if response == "Y": # if confirmed, continue
                            break
                        elif response == "N": # if denied, reset end date
                            e_date = None
                            break
                        else:
                            print("Invalid response")
            else:
                e_date = None
                print("Error: End date can not be before start date")
        except:
            pass


    return Trip(name, location, date(*s_date), date(*e_date))

## create a function to get user name

def get_name(name):
    name = name.strip().title()
    return name 

## create a function to get user location

def get_location(location):
    location = location.strip().title() # clean up user input
    # dictionary of US states and abbreviation as potential location names
    # for further development, additional locations should be added
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }

    # list of keys and values to compare user input with
    keysList = list(states.keys())
    for i in range(len(keysList)): # title case keys to match title cased input
        keysList[i] = keysList[i].title()
    valuesList = list(states.values())

    if location in keysList:
        return states[location.upper()] # return full state name if given abbreviated version (must use upper to index into dict)
    elif location in valuesList:
        return location # return user input if valid
    else:
        print("Invalid location")
        print("Currently only U.S. states supported")
        return None

## create a function to get user date, returned in standard form

def get_date(givendate):
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
    matches1 = re.search(r"^(.+) (\d{1,2}),? (\d{1,4})$", givendate, re.IGNORECASE)
    if matches1:
        try: # match input month to corresponding number
            month = int(months[matches1.group(1)])
        except: # if invalid month surpress error
            print("Invalid month name")
            return None
        day = int(matches1.group(2))
        year = int(matches1.group(3))

    # test for date in MM/DD/YYYY format
    matches2 = re.search(r"^(\d{1,2})[/-](\d{1,2})[/-](\d{1,4})$", givendate, re.IGNORECASE)
    if matches2:
        month = int(matches2.group(1))
        day = int(matches2.group(2))
        year = int(matches2.group(3))

    try: # test input for calendar date bounds
        if 1 <= month <= 12 and 1 <= day <= 31: # narrow bounds, only 12 months with max 31 days
            if month in [4,6,9,11] and day == 31: # months with only 30 days
                print("Invalid days for given month")
                return None
            elif month == 2: # February
                if year%4 == 0:
                    if year%100 == 0:
                        if year%400 == 0:
                            if day > 29:
                                print("Invalid days for given month")
                                return None
                            else:
                                return [year, month, day]
                        if day > 28:
                            print("Invalid days for given month")
                            return None
                        else:
                            return [year, month, day]
                    if day > 29:
                        print("Invalid days for given month")
                        return None
                    else:
                        return [year, month, day]
                if day > 28:
                    print("Invalid days for given month")
                    return None
                else:
                    return [year, month, day]
            else: # if input satisfies all bounds
                return [year, month, day]
    except:
        pass

    # if none of the above can be completed, provide user a hint
    print("Invalid date - Valid forms of date include")
    print("1 MM/DD/YYYY")
    print("2 MM-DD-YYYY")
    print("3 Month DD, YYYY")

## create a funtion to determine if two users have overlapping dates in the same location
def linkUp(user1, user2):
    if user1.location == user2.location: # check for same trip location
        latest_start = max(user1.startdate, user2.startdate) # find the overlapping dates
        earliest_end = min(user1.enddate, user2.enddate)
        delta = (earliest_end - latest_start).days + 1
        overlap_days = max(0, delta) # find the number of overlapping days if any
        return Trip(f"{user1.name} and {user2.name}", user1.location, latest_start, earliest_end, overlap_days)
    else: # if no overlapping location
        print(f"There is no overlapping locations within {user1.name}'s and {user2.name}'s trips")
    


if __name__ == "__main__":
    main()