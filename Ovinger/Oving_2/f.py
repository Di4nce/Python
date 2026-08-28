import turtle as t, random
t.shape("turtle")
t.pencolor("green")
t.pensize(3)

# for i in range(4):
#    t.circle(10)    
#    t.right(90) 
# t.done() # Beholder denne fra forrige deloppgave

radius = random.randint(10,30)
grader = random.randrange(30, 90, 10) # start 30, maks 90, 10 trinn om gangen
antall = random.randint(10,20)
print(f"Lager {antall} sirkler med {radius} start-radius og {grader} grader mellom hver!")
for i in range (antall):
    t.circle(radius)
    t.right(grader)
    radius += 10
t.done()
