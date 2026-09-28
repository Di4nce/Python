import turtle as t
import math as m

t.bgcolor("black")
t.speed(0)
storrelse = 10
grader = 10
endring_storrelse = 10
farger = ["yellow", "red", "blue", "green", "magenta", "orange"]
sider = len(farger)

def firkant_side(color):
    t.left(360/sider)
    t.color(color)
    t.forward(storrelse)

def hjorne():
    radius = storrelse / (2 * m.sin(m.pi / sider))  # Endret til radius (litt hjelp fra AI for formelen) sentrum -> hjørne
    vinkel = 90 - 180 / sider # Endret til dynamisk vinkel (litt hjelp fra AI her)
    t.penup()
    t.goto(0,0)
    t.right(vinkel) 
    t.forward(radius) 
    t.pendown()
    t.left(vinkel)

for i in range(50):
    hjorne()
    farge_teller = 0
    for i in range(sider):
        firkant_side(farger[farge_teller])
        farge_teller += 1
    
    storrelse += endring_storrelse
    t.right(grader)
t.done()