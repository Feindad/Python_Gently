#EX8 Pyton Gently Read Write File

def writeToFile(file,text):
    f = open(file, "w")
    f.write(text)
    f.close()

def appendToFile(file,text):
    f = open(file, "a")
    f.write(text)
    f.close()

def readFromFile(file):
    f = open(file, "r")
    return(f.read())

writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')
assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'


