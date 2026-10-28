# Pascal's trekant
# Pascal's trekant er en trekant av tall på følgende format:
 
# 1
# 1, 1
# 1, 2, 1
# 1, 3, 3, 1
# 1, 4, 6, 4, 1
# osv.
 
# Hver linje starter og slutter på 1. Tallene som er i mellom er summen av tallet på samme posisjon i
# linja over og tallet i posisjonen rett til venstre i linja over. Så for eksempel i linje 5 så er første tall 1.
# Andre tall i linje 5 er summen av første og andre tall i linje 4, som er 1 + 3 = 4. Tredje tall i linje 5 er
# summen av andre og tredje tall i linje 4, som er 3 + 3 = 6.
 
# Skriv et Python script som lar brukeren skrive inn antall linjer av Pascal's trekant den skal skrive
# ut og så skriver ut det antall linjer.

linjer = int(input("Skriv inn antall linjer: "))

forrige = []
for i in range(linjer):
    ny = [1]    # Hver linje starter med 1
    for j in range(len(forrige) -1):    # Tallene i midten
        ny.append(forrige[j] + forrige[j +1])
    if i > 0:
        ny.append(1)    # Hver linje slutter med 1
    print(*ny, sep=", ")    # Stjernenpakker ut listen sli at tallene skrives ut etter hverandre, 
    # og sep=", " setter komma og mellomrom mellom
    forrige = ny