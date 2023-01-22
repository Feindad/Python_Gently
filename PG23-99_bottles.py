### Python Gently Ex23 99 bottles of beer

def bottles(x):
    if x > 2:
        plural ="s"
    else:
        plural = ""
    print(str(x) + ' bottle' + plural + ' of beer on the wall,')
    print(str(x) + ' bottle' + plural + ' of beer,')
    print('Take one down,')
    print('Pass it around,')
    if x > 1:
        print(str(x-1) + ' bottle' + plural +' of beer on the wall,')
        print("")
    else:
        print('No more bottles of beer on the wall!')
        return

    return

for x in range(99,0,-1):
    bottles(x)
