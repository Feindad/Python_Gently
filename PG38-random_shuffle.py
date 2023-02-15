###Python Gently Exercise 38 Random Shuffle
import random

def shuffle(deck):
    l = len(deck)-1
    if l == 0:
        return
    shufDeck = []
    a = random.randint(0,l)
    b = deck[a]
    
    while len(shufDeck) < len(deck):    
            
        if b in shufDeck:
            a = random.randint(0,l)
            b = deck[a]
        else:
            shufDeck.append(b)

    
    print(deck,shufDeck)
    return shufDeck




random.seed(42)

# Perform this test ten times:

for i in range(10):

    testData1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        
   
    
    shuffle(testData1)

    # Make sure the number of values hasn't changed:
    
    assert len(testData1) == 10

    # Make sure the order has changed:

    assert testData1 != [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Make sure that when re-sorted, all the original values are there:

    print (testData1)
    assert sorted(testData1) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

 

# Make sure an empty list shuffled remains empty:

testData2 = []

shuffle(testData2)

assert testData2 == []
