#Python Gently Ex 20 Leap Year

def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    return False
    
assert isLeapYear(1999) == False

assert isLeapYear(2000) == True

assert isLeapYear(2001) == False

assert isLeapYear(2004) == True

assert isLeapYear(2100) == False

assert isLeapYear(2400) == True
