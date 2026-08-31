# Script for å reagne ut volum av et rom

mangler_verdi = True
while mangler_verdi:
    try:
        lengde = float(input("Lengde til rommet: "))
    except ValueError:
        print("Lengde må være et tall")
        continue
    if lengde < 0.0:
        print("Lengdem må være positiv")
    else:
        mangler_verdi = False

