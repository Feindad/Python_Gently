#Python Gently EX-15 Median

def median(numbers):
    l =len(numbers)
    if l == 0:
        return None
    
    numbers.sort()
    
    if l % 2 != 0:
        med = l // 2
        return numbers[med]
    else:
        m =  l // 2
        med = (numbers[m] + numbers[m-1]) / 2
        return med

assert median([]) == None

assert median([1, 2, 3]) == 2

assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5

assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6

import random

random.seed(42)

testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]

for i in range(1000):

    random.shuffle(testData)

    assert median(testData) == 6
