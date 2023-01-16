#Python Gently Ex 16 Mode
def average(numbers):
    av= 0
    av = (sum(numbers) // len(numbers))
    return(av)

def get_keys_from_value(d, val):
    return [k for k, v in d.items() if v == val]
def mode(numbers):
    if len(numbers)== 0:
        return None
    modeDict ={}
    modeList =[]
    numbers.sort()
    for number in numbers:
        if number not in modeDict:
            modeDict.update({number : 1 })
        else:
            count = modeDict[number]
            modeDict.update({number : count + 1})
    modeList = list(modeDict.values())
    modeList.sort(reverse=True)
    v = (modeList[0])
    mode = get_keys_from_value(modeDict, v)
    
    return mode[0]

assert mode([]) == None

assert mode([1, 2, 3, 4, 4]) == 4

assert mode([1, 1, 2, 3, 4]) == 1

import random

random.seed(42)

testData = [1, 2, 3, 4, 4]

for i in range(1000):

    random.shuffle(testData)

    assert average(testData) == 2

