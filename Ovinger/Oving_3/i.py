import turtle as t
t.pencolor("gold")
t.bgcolor("black")

def stjerne(stjerne_storrelse):
    for i in range(12):
        t.forward(stjerne_storrelse)
        t.backward(stjerne_storrelse)
        t.right(30)

def arm():
    global heading
    t.setheading(heading)
    t.penup()
    t.forward(15) # Lage litt startavstand
    t.pendown
    for i in range(9):
        t.penup()
        t.right(20)
        t.forward(30)
        t.pendown()
        stjerne(stjerne_storrelse)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    heading += 360 / arms

heading = 0
stjerne_storrelse = 10
start_storrelse = 20

stjerne(start_storrelse) # En fin stor stjerne i midten :-)

fortsette = True
while fortsette:
    try:
        arms = int(input("Skriv inn antall spiralarmer: "))
    except ValueError:
        print("Du må taste inn et heltall ;-)")
        continue
    fortsette = False

for i in range (arms):
    arm()

t.done()
