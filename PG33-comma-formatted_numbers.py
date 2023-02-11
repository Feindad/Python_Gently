##Python Gently Ex33 Comma-Formatted Numbers

def commaFormat(num):
    strnum = str(num)
    l = len(strnum)
    for x in range(2,-1,-1):
        print(strnum[x], end='')  
    return


assert commaFormat(1) == '1'

assert commaFormat(10) == '10'

assert commaFormat(100) == '100'

assert commaFormat(1000) == '1,000'

assert commaFormat(10000) == '10,000'

assert commaFormat(100000) == '100,000'

assert commaFormat(1000000) == '1,000,000'

assert commaFormat(1234567890) == '1,234,567,890'

assert commaFormat(1000.123456) == '1,000.123456'
