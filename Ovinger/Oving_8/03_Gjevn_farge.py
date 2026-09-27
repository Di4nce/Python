import turtle as t
import math as m

t.bgcolor("black")
t.speed(0)
storrelse = 10
grader = 10
endring_storrelse = 10
farger = ["yellow", "red", "blue", "green", "magenta"]
sider = len(farger)

def firkant_side(color):
    t.left(360/sider)
    t.color(color)
    t.forward(storrelse)

def hjorne():
    t.penup()
    t.goto(0,0)
    t.right(45)
    t.forward((m.sqrt((storrelse**2)+(storrelse**2)))/2) # denne stemmer nok ikke helt matematisk lener, men good enough
    t.pendown()
    t.left(45)

for i in range(20):
    hjorne()
    farge_teller = 0
    for i in range(sider):
        firkant_side(farger[farge_teller])
        farge_teller += 1
    
    storrelse += endring_storrelse
    t.right(grader)
t.done()