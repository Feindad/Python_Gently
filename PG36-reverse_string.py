###Python Gently EXercise #36breverse string

def reverseString(word):
    rword=[]
    retword=''
    l = len(word)-1
    for letter in word:
        rword.append(letter)
    for x in range(l,-1,-1):
        retword=retword + retword.join(rword[x])
    return retword 


assert reverseString('Hello') == 'olleH'

assert reverseString('') == ''

assert reverseString('aaazzz') == 'zzzaaa'

assert reverseString('xxxx') == 'xxxx'
