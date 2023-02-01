##Python Gently Ex31 Convert to string
def rDig(num):
    numlist = ['0','1','2','3','4','5','6','7','8','9']
    rem = round(10 * (abs(num/10)- int(abs(num/10))))
    
    return numlist[rem]
    
def convertIntToStr(num):
     if num == 0:
         return "0"
     numString=''
     if num <0:
         neg = '-'
     else:
         neg =''
     
     num = abs(num)
     while num != 0:      
    
         numString = (rDig(num))+ numString 
         num = num//10   

     return neg + numString

for i in range(-10000, 10000):
    assert convertIntToStr(i) == str(i)
