#Python Gently Ex13 Sum & Product

def calculateSum(nums):
    summ = 0
    for num in nums:
        summ = summ + num
    return summ
    
def calculateProduct(nums):
    prod = 1
    for num in nums:
        prod = prod * num
    return prod



assert calculateSum([]) == 0

assert calculateSum([2, 4, 6, 8, 10]) == 30

assert calculateProduct([]) == 1

assert calculateProduct([2, 4, 6, 8, 10]) == 3840



