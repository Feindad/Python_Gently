#Python Gently Ex32 Convert Str to Int
def convertStrToInt(strnum):
    
    numdic = {'0': 0,'1': 1,'2':2 ,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}
    if strnum[0] == '-':
        strnum = strnum[1:]
        neg = -1
    else:
        neg = 1
    lenstr=len(strnum)
    pwr=  1
    numlist=[]
    for x in range(lenstr):
        pwr= lenstr - x -1
        dig=(numdic[strnum[x]])
        numlist.append(dig * 10 ** pwr)

    return neg* sum(numlist)



for i in range(-10000, 10000):
        assert convertStrToInt(str(i)) == i
