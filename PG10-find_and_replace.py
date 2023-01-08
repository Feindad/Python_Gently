### Python Gently Ex-10 Find and Replace 
#test edit 

def find_replace(text,oldText,newText):
    text = text.replace(oldText,newText)
    return text

def findAndReplace(text,oldText,newText):
    pass
        
assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'

assert findAndReplace('fox', 'fox', 'dog') == 'dog'

assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'

assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'

assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'

