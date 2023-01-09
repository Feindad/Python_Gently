# Rolling text sign. Having a bit of troble with Ex1o.
# Perhaps the concept of a rolling text sign will incrementally help me.

message ="I won't fail. I've just have found 10,000 ways that won't work" #Edison
window = 8
newMessage =[]
match = "won't"
word = "didn't"
l = len(match)
def rollingText(text):
    tlen = len(text)
    for x in range(tlen):
        print(text[x:x+8]) #, end ="")
        if match in (text[x:x+l]):
            text = text[0:x] + word + text[x+l:]
            print(text)
            
rollingText(message)
