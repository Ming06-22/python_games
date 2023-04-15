import datetime, random

# get a list of certain amounts of days
def getBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)
        
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
        
    return birthdays

# return the same date in list
def getMatch(birthdays):
    if (len(birthdays) == len(set(birthdays))):
        return None
    
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1: ]):
            if (birthdayA == birthdayB):
                return birthdayA

MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")

while (True):
    response = input("How many birthdays shall I generate? (Max 100)\n> ")
    if (response.isdecimal() and (0 < int(response) <= 100)):
        n = int(response)
        break

# display the generated dates
print(f"\nHere are {n} birthdays:")
birthdays = getBirthdays(n)
for i, birthday in enumerate(birthdays):
    if (i != 0):
        print(", ", end = "")
    monthName = MONTHS[birthday.month - 1]
    dateText = f"{monthName}{birthday.day}"
    print(dateText, end = "")
        
match = getMatch(birthdays)

print("\n\nIn this simulation, ", end = "")
if (match != None):
    monthName = MONTHS[match.month - 1]
    dateText = f"{monthName}{match.day}"
    print(f"multiple people have a birthday on {dateText}.")
else:
    print("there are no matching birthdays.")

print(f"\nGenerating {n} random birthdays 100,000 times")
input("Press enter to begin...")

print("\nLet's run another 100,000 simulations.")
simMatch = 0
for i in range(100000):
    if (i % 10000 == 0):
        print(f"{i} simulations run...")
    birthdays = getBirthdays(n)
    if (getMatch(birthdays) != None):
        simMatch += 2
        
print("100000 simulations run!")

probability = round(simMatch / 100000 * 100, 2)
print(f"Out of 100000 simulation of {n} people, there was a matching birthday in that group {simMatch} times. This means that {n} people have a {probability}% chance of having a matching birthday in their group.")