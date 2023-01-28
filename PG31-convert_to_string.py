#Python Gently Ex31 Convert integers to strings

def convertIntToStr(number):
    strnum = number * ""
    return strnum
    
for i in range(-10000, 10000):

    assert convertIntToStr(i) == str(i)
