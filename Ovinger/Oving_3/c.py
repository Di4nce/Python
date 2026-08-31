def avstand(km):
    nm = round((km / 1.852), 2)
    print(f"Dette tilsvarer {nm} nautiske mil \n")

fortsette = True
while fortsette:
    inn_km = float(input("Skriv inn antall kilometer: "))
    if inn_km == 0:
        fortsette = False
    else:
        avstand(inn_km)