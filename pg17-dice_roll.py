#Python Gently Ex17 Dice Roll
import random

def rollDice(num):
    score = 0
    total = 0
    if num ==0:
        return 0
    
    for roll in range(num):
        score = random.randint(1,6)
        total = total + score
    return total

assert rollDice(0) == 0

assert rollDice(1000) != rollDice(1000)

for i in range(1000):

    assert 1 <= rollDice(1) <= 6

    assert 2 <= rollDice(2) <= 12

    assert 3 <= rollDice(3) <= 18

    assert 100 <= rollDice(100) <= 600
