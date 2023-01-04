#Python Gently Temerature Conversion

def convertToCelsius(f):
    f = int(f)
    c = (f - 32) * (5/9)
    return(c)

def convertToFahrenheit(c):
    c = int(c)
    f = c * (9 / 5) + 32
    return(f)

assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15
assert convertToCelsius(45) == 113
