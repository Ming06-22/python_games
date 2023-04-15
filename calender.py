import datetime

DAYS = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
MONTHS = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

# get user input
while (True):
    response = input("Enter the year for the calender: ")
    if (response.isdecimal() and int(response) > 0):
        year = int(response)
        break
    
while (True):
    response = input("Enter the month for the calender: ")
    if (response.isdecimal() and 0 < int(response) <= 12):
        month = int(response)
        break
    
# get calender information
def getCalender(year, month):
    calText = "\n"
    calText += (" " * 34) + MONTHS[month - 1] + " " + str(year) + "\n"
    calText += "   Sunday     Monday     Tuesday   Wednesday  Thursday    Friday    Saturday\n"
    
    weekSeperator = "+----------" * 7 + "+\n"
    blankRow = "|          " * 7 + "|\n"
    currentDate = datetime.date(year, month, 1)
    
    while (currentDate.weekday() != 6):
        currentDate -= datetime.timedelta(days = 1)
        
    while (True):
        calText += weekSeperator
        
        dayNumberRow = ""
        for i in range(7):
            dayNumberLabel = str(currentDate.day).rjust(2)
            dayNumberRow += "|" + dayNumberLabel + " " * 8
            currentDate += datetime.timedelta(days = 1)
        dayNumberRow += "|\n"
        
        calText += dayNumberRow
        for i in range(3):
            calText += blankRow
        
        if (currentDate.month != month):
            break
    
    calText += weekSeperator
    
    return calText

calText = getCalender(year, month)
print(calText)

# output txt file
calenderFilename = f"calender_{year}_{month}.txt"
with open(calenderFilename, "w") as f:
    f.write(calText)
    
print(f"Save to {calenderFilename}")