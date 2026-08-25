# Lag et script som lar brukeren skrive inn flere linjer tekst og hvor
# brukeren avslutter med å skrive inn en tom linje

# Alltid tenk over hvordan en løkke skal avsluttes

TYNGDEAKSELERASJON = 9.8    # Kun caps er en konstant verdi som ikke skal endres

hele_teksten = ""       # Akkumulator
antall_linjer = -1       # Teller
nv_linje = "Startverdi" # Verdilager - lager siste verdi fra brukeren
while nv_linje != "":   # Så lenge nv_linje er ulik en tom streng
    nv_linje = input("Skriv inn en linje: ")
    hele_teksten += nv_linje + "\n"   # hele_teksten = hele_teksten + nv_linje
    antall_linjer += 1
print(f"Antall linjer: {antall_linjer}")
print(hele_teksten)