from random import randint
tilfeldig_tall = randint(1, 100)
ferdig = False

while ferdig != True:
    gjett = int(input("Gjett et tall mellom 1 og 100: "))
    if gjett > tilfeldig_tall:
        print("Du gjettet for høyt :-)")
    elif gjett < tilfeldig_tall:
        print("Du gjettet for lavt ;-)")
    elif gjett == tilfeldig_tall:
        print("Hurra, du gjettet korrekt!!! :-D")
        ferdig = True
    else:
        print("Har du tastet et tall mellom 1 og 100?")
