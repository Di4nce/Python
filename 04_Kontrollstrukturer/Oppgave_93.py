tall_liste = []
stopp = False

while stopp != True:
    ny_tall = str(input("Skriv inn et heltall (skriv STOPP for å avslutte): "))
    if ny_tall != "STOPP":
        tall_liste.append(ny_tall)
    else:
        stopp = True

print(tall_liste)