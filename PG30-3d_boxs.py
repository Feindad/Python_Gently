#Python Gently Ex30 3d box drawing Sort of.  I didn't like the look of ascii
#I may revisit this after completing the book.

import turtle

t = turtle.Turtle()

def square(size):
    for x in range(4):
        t.forward(size)
        t.right(90)
    
def drawBox(size):
    side = size *.707
    s = turtle.getscreen()
    square(size)
    t.right(45)
    t.forward(side)
    t.left(45)
    square(size)
    t.penup()
    t.goto(size,0)
    t.pendown()
    t.right(45)
    t.forward(side)
    t.left(45)
    t.penup()
    t.goto(0,-size)
    t.pendown()
    t.right(45)
    t.forward(side)
    t.left(45)
    t.penup()
    t.goto(size,-size)
    t.pendown()
    t.right(45)
    t.forward(side)
    t.left(45)
