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