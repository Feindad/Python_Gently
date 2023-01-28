#Python Gently Ex31 Convert integers to strings

def convertIntToStr(number):
    strnum =''    
    if number < 0:
        strnum = ('-')
    num = abs(number)
    ex = 1
    numlist = ['0','1','2','3','4','5','6','7','8','9']
    while num >=1:
     
        while num >= 10:
                ex = ex * 10
                num = num/10
                if round((num - int(num))*10) == 0:
                    strnum = strnum + '0'
        dig = int(num//1)
        print(dig)
        ret = numlist[dig]
        strnum = strnum + (ret)
        rem = num - dig
        num =round(ex * rem)
        ex = 1
    return strnum


    
for i in range(-99, 99):
    print(i)
    assert convertIntToStr(i) == str(i)
