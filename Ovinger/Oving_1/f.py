import math

diagonal = float(input("Skriv inn diagonalen: "))

s = math.sqrt(16**2 + 9**2)

bredde = 16 * diagonal / s
hoyde = 9 * diagonal / s

print("Høyde er: ", round(hoyde, 1))
print("Bredde er: ", round(bredde, 1))