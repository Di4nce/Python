import math, sys

format = input("Hva format ønsker du å regne i? 16:9, 4:3 eller 2:1? ")
# kunne også ha laget en egen input for h og en for b
if format == "16:9":
    h = 16
    b = 9
elif format == "4:3":
    h = 4
    b = 3
elif format == "2:1":
    h = 2
    b = 1
else:
    print("Du har valgt et ugyldig format, bedre lykke neste gang!")
    sys.exit(0)

diagonal = float(input("Skriv inn diagonalen i tommer: "))

s = math.sqrt(h**2 + b**2)

bredde = h * diagonal / s
hoyde = b * diagonal / s

print("Høyde i cm er: ", round((hoyde*2.54), 1))
print("Bredde i cm er: ", round((bredde*2.54), 1))