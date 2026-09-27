import turtle as t
import math as m

t.bgcolor("black")
t.speed(0)
storrelse = 10
grader = 10
endring_storrelse = 10
farger = ["yellow", "red", "blue", "green"]

def firkant_side(color):
    t.left(90)
    t.color(color)
    t.forward(storrelse)

def hjorne(): # hadde ikke trengt å være en def, men lagde for oversikt sin skyld
    t.penup()
    t.goto(0,0)
    t.right(45)
    t.forward((m.sqrt((storrelse**2)+(storrelse**2)))/2)
    t.pendown()
    t.left(45)

for i in range(50):
    hjorne()
    firkant_side(farger[0])
    firkant_side(farger[1])
    firkant_side(farger[2])
    firkant_side(farger[3])
    storrelse += endring_storrelse
    t.right(grader)
t.done()