import math

def d_funksjon(diagonal, bredde_forhold=16, hoyde_forhold=9):
    s = math.sqrt(bredde_forhold**2 + hoyde_forhold**2)
    bredde = 16 * diagonal / s
    hoyde = 9 * diagonal / s
    print("Høyde er: ", round(hoyde, 1))
    print("Bredde er: ", round(bredde, 1))

diagonal_inn = float(input("Skriv inn diagonalen: "))
endre = input("Ønsker du å endre på forholdstallene fra 16:9? J/N: ").upper()

if endre == "J":
    bredde_inn = int(input("Skriv inn bredden: "))
    hoyde_inn = int(input("Skriv inn høyden: "))
    d_funksjon(diagonal_inn, bredde_inn, hoyde_inn)
else:
    d_funksjon(diagonal_inn)