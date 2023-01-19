#Python Gently Ex19 Password Generator
import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special = "~!@#$%^&*()_+]"
numbers = "1234567890"



def generatePassword(length):
    if length <= 11:
        length = 12
    mylist =[]
    password = ''
    digit = ''
    for x in range(length):
        l = lower[random.randint(1,25)]
        u = upper[random.randint(1,25)]
        s = special[random.randint(1,9)]
        n = str(random.randint(0,9))

        mylist = [l,u,s,n]
        d = random.choice(mylist)
        password = password + d
        mylist =[]
        
    return password


assert len(generatePassword(8)) == 12

 
pw = generatePassword(14)

assert len(pw) == 14

hasLowercase = False

hasUppercase = False

hasNumber = False

hasSpecial = False

for character in pw:

    if character in lower:

        hasLowercase = True

    if character in upper:

        hasUppercase = True

    if character in numbers:

        hasNumber = True

    if character in special:

        hasSpecial = True

assert hasLowercase and hasUppercase and hasNumber and hasSpecial
