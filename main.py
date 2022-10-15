# Dylan Marn

'''
LinkUp: An app designed to help far away friends...
    allow users to link up whenever possible and make the most of their time,
    by making the plans easy so they can make the memories

2 users input their trip details and the program alerts the users if there is any overlap time where they could possible LinkUp

Taget audience:
    college students who moved away from friends for school - easily lets friend group know who is back home to LinkUp
    friends that want help connecting whenever possible
    friends that want an easy way to plan events (with app full functionality)
    
Further development:
    add capacity for 2+ users
    add a "home" location where another user's trip to that location will yield a LinkUp
    add support for world-wide locations, possibly as specific as cities
        add feature that matched users traveling to neighboring cities not just exact locations
    add a "things to do" section that helps connected users find things to do in the area
'''

from operator import and_
import re
from datetime import date

# class Trip stores important trip data
class Trip:
    def __init__(self, name, home, location=None, startdate=None, enddate=None, days=0):
        self.name = name
        self.home = home
        self.location = location
        self.startdate = startdate
        self.enddate = enddate
        self.days = days
    
    def __str__(self):
        return f"{self.name} is from {self.home} and traveling to {self.location} from {self.startdate} to {self.enddate}"


def main():
    print("Please fill out the following for user #1")
    user1 = set_user() # get user #1 trip details
    print(f"\nPlease fill out the following for user #2")
    user2 = set_user() # get user #2 trip details
    print(user1)
    print(user2)
    linkUp(user1, user2)


## create functions to get user input(name, location and dates) for 2+ users

def set_user():
    # get name
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

    # get home location
    home = None
    while not home: # loop until valid state
        home = get_location(input("Where are you currently? "))    
        if home: # if valid state, confirm with user
            while True: # loop until user confirms or denies
                response = input(f"{name}, it appears you are currenly in {home}, is this correct? (Y/N)").upper()
                if response == "Y": # if confirmed, continue
                    break
                elif response == "N": # if denied, reset state
                    location = None
                    break
                else:
                    print("Invalid response")

    # determine if user has an upcoming trip
    
    while True:
        trip = input("Do you have an upcoming trip? (Y/N)").upper()
        if trip == "N":
            return Trip(name, home)
        elif trip == "Y":
            # get trip location
            location = None # initalize state to nothing
            while not location: # loop until valid state
                location = get_location(input("Where are you traveling to? "))
                if location == home:
                    print("You are already there")
                    location = None
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

            # get trip start date
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

            # get trip end date
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

            return Trip(name, home, location, date(*s_date), date(*e_date))

        else:
            print("Invalid response")


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

    # test for date in common MM/DD/YYYY or MM-DD-YYYY format
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
                if year%4 == 0: # leap year
                    if year%100 == 0: # not leap year
                        if year%400 == 0: # leap year
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
    if not user1.location and not user2.location: # if neither users have a trip
        if user1.home == user2.home: # only linkUp if homes are the same
            print(f"{user1.name} and {user2.name} will both be in {user1.home} indefinetly")
        else: # else there is no overlap
            print(f"There is no overlapping period within {user1.name}'s and {user2.name}'s locations")
    elif not user1.location and user2.location: # if only user2 has a trip
        if user1.home == user2.home: # if homes are the same, linkUp until user2 leaves
            print(f"{user1.name} and {user2.name} will both be in {user1.home} until {user2.startdate}")
        elif user1.home == user2.location: # if user2's trip is to user1's home, linkUp for duration of user2's trip
            print(f"{user1.name} and {user2.name} will both be in {user1.home} from {user2.startdate} to {user2.enddate}")
        else: # else there is no overlap
            print(f"There is no overlapping period within {user1.name}'s and {user2.name}'s locations")
    elif user1.location and not user2.location: # if only user1 has a trip
        if user1.home == user2.home: # if homes are the same, linkUp until user1 leaves
            print(f"{user1.name} and {user2.name} will both be in {user1.home} until {user1.startdate}")
        elif user2.home == user1.location: # if user1's trip is to user2's home, linkUp for duration of user1's trip
            print(f"{user1.name} and {user2.name} will both be in {user1.home} from {user1.startdate} to {user1.enddate}")
        else: # else there is no overlap
            print(f"There is no overlapping period within {user1.name}'s and {user2.name}'s locations")
    elif user1.location and user2.location: # if both users have a trip
        earliest_start = min(user1.startdate, user2.startdate)
        latest_start = max(user1.startdate, user2.startdate) 
        earliest_end = min(user1.enddate, user2.enddate) 
        latest_end = max(user1.enddate, user2.enddate)       
        if user1.home == user2.home and user1.location != user2.location: # if home location is the same but not trip location, linkUp until first user to leave 
            print(f"{user1.name} and {user2.name} will both be in {user1.home} until {earliest_start}")
        elif user1.home == user2.home and user1.location == user2.location: # if home location and trip location is the same
            print(f"{user1.name} and {user2.name} will both be in {user1.home} until {earliest_start}")
            if latest_start < earliest_end:
                print(f"They will both be in {user1.location} from {latest_start} to {earliest_end}")
            elif latest_start > earliest_end:
                print(f"They will both be back in {user1.home} from {earliest_end} to {latest_start}")
            else:
                print(f"They will both be back in {user1.home} only on {latest_start}")
            print(f"and finally will both be in {user1.home} from {earliest_start} indefinetly")
        elif user1.home == user2.location and user2.home == user1.location: # if user1's trip is to user2's home and if user2's trip is to user1's home
            if user1.enddate < user2.startdate:
                print(f"{user1.name} and {user2.name} will both be in {user1.location} from {earliest_start} to {earliest_end}")
                print(f"They will both be in {user2.location} from {latest_start} to {latest_end}")
            elif user2.enddate < user1.startdate:
                print(f"{user1.name} and {user2.name} will both be in {user2.location} from {earliest_start} to {earliest_end}")
                print(f"They will both be in {user1.location} from {latest_start} to {latest_end}")

            if user1.startdate > user2.startdate and user1.startdate < user2.enddate:
                print(f"{user1.name} and {user2.name} will both be in {user1.home} from {earliest_start} to {latest_start}")
            elif user2.startdate > user1.startdate and user2.startdate < user1.enddate:
                print(f"{user1.name} and {user2.name} will both be in {user2.home} from {earliest_start} to {latest_start}")
            elif user1.startdate == user2.startdate:
                print(f"They just misses each other on {earliest_start}")
            
            if user1.enddate < user2.enddate and user1.enddate > user2.startdate:
                print(f"They will both be in {user1.home} from {earliest_end} to {latest_end}")
            elif user2.enddate < user1.enddate and user2.enddate > user1.startdate:
                print(f"They will both be in {user1.location} from {earliest_end} to {latest_end}") 
            elif user1.enddate == user2.enddate:
                print(f"They just misses each other on {latest_end}") 
        
        elif user1.home != user2.home and user1.location == user2.location: # if trip location is the same but not home
            delta = (earliest_end - latest_start).days + 1
            overlap_days = max(0, delta) # find the number of overlapping days if any
            print(f"{user1.name} and {user2.name} will both be in {user1.location} from {latest_start} to {earliest_end}")
    else: # if home location and trip location is not the same
        print(f"There is no overlapping time within {user1.name}'s and {user2.name}'s locations")
    

if __name__ == "__main__":
    main()