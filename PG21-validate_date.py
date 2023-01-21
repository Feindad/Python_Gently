#Python Gently Ex:21 Validate Date
import isLeapYear

def isValidDate(year, month, day):
    thirtyOnes =[1,3,5,7,8,10,12]

    if day == 31 and month not in thirtyOnes:
        return False
    
    if month > 12 or month < 1:
        return False

    if day > 31 or day < 1:
        return False
    if isLeapYear.isLeapYear(year) == False and day == 29 and month == 2:
        return False

    return True

assert isValidDate(1999, 12, 31) == True

assert isValidDate(2000, 2, 29) == True

assert isValidDate(2001, 2, 29) == False

assert isValidDate(2029, 13, 1) == False

assert isValidDate(1000000, 1, 1) == True

assert isValidDate(2015, 4, 31) == False

assert isValidDate(1970, 5, 99) == False

assert isValidDate(1981, 0, 3) == False

assert isValidDate(1666, 4, 0) == False

 

import datetime

d = datetime.date(1970, 1, 1)

oneDay = datetime.timedelta(days=1)

for i in range(1000000):

    assert isValidDate(d.year, d.month, d.day) == True

    d += oneDay
