import turtle

turtle.shape("turtle")  # Gjør om fra pil til skildpadde


turtle.forward(100)     # 100 Piksler
turtle.right(90)        # Snur seg 90grader mot høyre
turtle.pencolor("red")  # Endre penfarge til rød, kan bruke standard fargeord på engleks
turtle.pensize(3)       # Bredden i antall piksler
turtle.forward(100)
turtle.penup()
turtle.right(90)        # Snur seg 90grader mot høyre
turtle.forward(100)
turtle.pendown()
turtle.right(90)        # Snur seg 90grader mot høyre
turtle.forward(100)

turtle.circle(50)       # Radius i piksler
turtle.done()           # Ferdig og tegn, men vent med å lukke vinduet