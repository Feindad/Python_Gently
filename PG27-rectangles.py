#Python Gently ex27 rectangle drawing

def drawRectangle(x,y):
    for s in range(y):
        for t in range(x):
            print('#', end='')
        print()
