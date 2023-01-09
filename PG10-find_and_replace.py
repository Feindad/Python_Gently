### Python Gently Ex-10 Find and Replace 
#test edit 


def find_replace(text,oldText,newText):
    text = text.replace(oldText,newText)
    return text

def findAndReplace(text,oldText,newText):
    olen = len(oldText)
    tlen = len(text)
    nlen = len(newText)
    for x in range(tlen):
        
        if oldText in (text[x:x+olen]):
            text = text[0:x] + newText + text[x+olen:]
            print(text)
            return text




assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'

assert findAndReplace('fox', 'fox', 'dog') == 'dog'

assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'

assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'

assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'

