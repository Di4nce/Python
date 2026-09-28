import turtle as t
import math as m

t.bgcolor("black")
t.speed(0)
storrelse = 10
grader = 10
endring_storrelse = 10


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

sider = 6
farge = ['#FF5733', '#FB5739', '#F75740', '#F35746', '#EF574D', '#EB5753', '#E7575A', '#E35760', '#DF5767', '#DB576D', '#D75774', '#D3577A', '#CF5781', '#CB5787', '#C7578E', '#C35794', '#BF579B', '#BB57A1', '#B757A8', '#B357AE', '#AF57B5', '#AB57BB', '#A757C2', '#A357C8', '#9F57CF', '#9B57D5', '#9757DC', '#9357E2', '#8F57E9', '#8B57EF', '#8757F6', '#8357FC', '#7F57FF', '#7B57FF', '#7757FF', '#7357FF', '#6F57FF', '#6B57FF', '#6757FF', '#6357FF', '#5F57FF', '#5B57FF', '#5757FF', '#5357FF', '#4F57FF', '#4B57FF', '#4757FF', '#4357FF', '#3F57FF', '#3357FF']
antall = len(farge)
farge_teller = 0
for i in range(antall):
    hjorne()
    for i in range(sider):
        firkant_side(farge[farge_teller])
    farge_teller += 1
    storrelse += endring_storrelse
    t.right(grader)
t.done()