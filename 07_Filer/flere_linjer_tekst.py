hele_teksten = ""       # Akkumulator
antall_linjer = -1       # Teller
nv_linje = "Startverdi" # Verdilager - lager siste verdi fra brukeren
while nv_linje != "":   # Så lenge nv_linje er ulik en tom streng
    nv_linje = input("Skriv inn en linje: ")
    hele_teksten += nv_linje + "\n"   # hele_teksten = hele_teksten + nv_linje
    antall_linjer += 1

print(f"Antall linjer: {antall_linjer}")

print()
filnavn  = input("Lagre til hvilken fil? ")
tekstfil = open(filnavn, "w", encoding="UTF-8")
tekstfil.write(hele_teksten)
tekstfil.close()