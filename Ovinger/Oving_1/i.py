import math

diagonal = float(input("Skriv inn diagonalen i tommer: "))

s = math.sqrt(16**2 + 9**2)

bredde = 16 * diagonal / s
hoyde = 9 * diagonal / s

print("Høyde i cm er: ", round((hoyde*2.54), 1))
print("Bredde i cm er: ", round((bredde*2.54), 1))