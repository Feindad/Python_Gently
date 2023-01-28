#Python Gently ex28 border drawing

def drawBorder(x,y):
    for s in range(y):
        for t in range(x):
            if s == 0 or s == y-1:
                print('-', end='')
            else:
                if t == 0 or t == x-1:
                    print('|', end='')
                else:
                    print(' ', end='')
        print()
