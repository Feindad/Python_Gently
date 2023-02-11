### Python Gently Ex #34 Uppercase letters

def getUppercase(word):
    udic = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D', 'e': 'E', 'f': 'F', 'g': 'G',
            'h': 'H', 'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L', 'm': 'M','n': 'N',
            'o': 'O', 'p': 'P', 'q': 'Q', 'r': 'R', 's': 'S', 't': 'T', 'u': 'U',
            'v': 'V', 'w': 'W', 'x': 'X', 'y': 'Y', 'z': 'Z'}
    uword=''
    for letter in word:
        if letter not in udic:
            uword = uword + letter
        else:
            uword = uword + udic[letter]
  
    return uword


assert getUppercase('Hello') == 'HELLO'

assert getUppercase('hello') == 'HELLO'

assert getUppercase('HELLO') == 'HELLO'

assert getUppercase('Hello, world!') == 'HELLO, WORLD!'

assert getUppercase('goodbye 123!') == 'GOODBYE 123!'

assert getUppercase('12345') == '12345'

assert getUppercase('') == ''
