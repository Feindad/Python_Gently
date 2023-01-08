#Area and volume Ex 4 from Python Gently


def area(l,w):
    return(l*w)

def perimeter(l,w):
    return(2*l + 2*w)

def volume(l,w,h):
    return(l*w*h)

def surfaceArea(l,w,h):
    return((l * w * 2) + (l * h * 2) + (w * h * 2))


assert area(10, 10) == 100

assert area(0, 9999) == 0

assert area(5, 8) == 40

assert perimeter(10, 10) == 40

assert perimeter(0, 9999) == 19998

assert perimeter(5, 8) == 26

assert volume(10, 10, 10) == 1000

assert volume(9999, 0, 9999) == 0

assert volume(5, 8, 10) == 400

assert surfaceArea(10, 10, 10) == 600

assert surfaceArea(9999, 0, 9999) == 199960002

assert surfaceArea(5, 8, 10) == 340

