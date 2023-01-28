#Python Gently Ex25 Multiplication table
spacer = " "

for x in range(-1,11):
    for y in range(1,11):
        if x== 0:
            if x == 0 and y == 1:
                print("   +", end='')
            else:    
                print('---', end="")
        else:
            if x == -1 and y == 1:
                print(spacer * 3, end='')
            if len(str(abs(x*y)))==1:
                print(spacer, end="")
            print(abs(x*y), end=" ")
        if y == 1 and x>0:
            print("|" + str(abs(x)), end=' ')
        if y==10:
            print()
