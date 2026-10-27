# Basis programmering
# Skriv et Python-script som regner ut volumet til ei kjegle. Brukeren skal oppgi radius til bunnen av
# kjeglen (r i formelen) og høyden til kjeglen (h i formelen). Etter å ha regnet ut volumet skal scriptet
# skrive dette ut.
 
# Formelen til volumet for ei kjegle: volum = 1/3*(pi*(r**2)*h)

import math
radius = float(input("Skriv inn radius på kjeglen: "))
hoyde = float(input("Skriv inn høyden til kjeglen: "))

volum = 1/3*(math.pi*(radius**2)*hoyde)

print(f"Volumet til kjeglen er {volum:.2f}")