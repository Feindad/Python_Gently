##Python Gently Ex26 Handshakes



def shakes(names):
    a = len(names)
    x = []    
    for y in range(1,a):
        x.append(y)
    return sum(x)

def printHandshakes(names):

    return shakes(names)


assert printHandshakes(['Alice', 'Bob']) == 1

assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3

assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6
