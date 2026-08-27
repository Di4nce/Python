import turtle as t
t.shape("turtle")
t.pencolor("green")
t.pensize(3)

kanter = int(input("Tast inn antall sider: "))

if kanter < 3:
    print("Umulig å ha mindre enn tre kanter!")
else:
    grader = 360 / kanter   # Måtte flytte denne til etter else, for det er umulig å dele på f.eks. 0
    for i in range(kanter):
        t.forward(100)
        t.right(grader)
    t.done()