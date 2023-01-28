##Python Gently Ex26 Handshakes



def shakes(names):
    a = len(names)
    x = []    
    for y in range(1,a):
        x.append(y)
    return sum(x)

def printHandshakes(names):
    y = shakes(names)
    a = len(names)
    while len(names) > 0:
        shaker = names[0]
        for x in range(0,a):
            if names[x] != shaker:
                print( shaker + ' shakes with ' +names[x])
        names.remove(names[0])    
        a = len(names)
    return y


assert printHandshakes(['Alice', 'Bob']) == 1

assert printHandshakes(['Alice', 'Barry', 'Carol']) == 3

assert printHandshakes(['Alice', 'Billy', 'Carol', 'David']) == 6
