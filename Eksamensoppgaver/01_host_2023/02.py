# Variabler og datatyper
# I øving 1 oppgave f skulle du lage et program som svarte på følgende oppgave:
 
# "Man oppgir vanligvis størrelsen til en TV eller dataskjerm som antall tommer langs diagonalen.
# For å finne ut om det er plass til TV-en der du tenker å ha den trenger du ofte å vite bredden og
# høyden til TV-en. Skriv et Python-script som regner ut bredde og høyde til en skjerm basert på
# lengden til diagonalen. Brukeren skal oppgi denne diagonale lengden. Anta at skjermen er på 16:9
# format (forholdet mellom bredde og høyde er 16:9, en skjerm som er 16 brei er 9 høy). Scriptet
# skal skrive ut lengden og bredden til skjermen. Du kan skrive ut lengde og bredde i samme enhet
# som brukeren oppgir diagonalen i (typisk tommer)."
 
# Under svaralternativene og i den vedlagte .pdf fila er det seks forslag til svar på denne oppgaven,
# som alle er varianter av løsningsforslaget. Du skal krysse av for alle forslagene som er riktige
# svar på oppgaven.
 
# Poeng: 3 poeng for hvert riktige kryss, -3 poeng for hvert feil kryss. Maksimalt 9 poeng, minimum
# 0 poeng.
# Velg ett eller flere alternativer
# Forslag 1 [x]
# Forslag 2 [ ]
# Forslag 3 [x]
# Forslag 4 [x]
# Forslag 5 [ ]
# Forslag 6 [ ]

 
# Forslag 1
skjermstorrelse_str = input("Skriv inn størrelsen til skjermen: ")
skjermstorrelse = float(skjermstorrelse_str)
nevner = (16**2 + 9**2)**0.5
faktor = skjermstorrelse/nevner
bredde = 16*faktor
hoyde = 9*faktor
print(f"En standard 16:9 skjerm med diagonal {skjermstorrelse} er "+
    f"{hoyde} høy og {bredde} brei.")
 
# Forslag 2
skjermstorrelse_str = input("Skriv inn størrelsen til skjermen: ")
skjermstorrelse = float(skjermstorrelse_str)
bredde = 16*faktor
hoyde = 9*faktor
nevner = (16**2 + 9**2)**0.5
faktor = skjermstorrelse/nevner
print(f"En standard 16:9 skjerm med diagonal {skjermstorrelse} er "+
    f"{hoyde} høy og {bredde} brei.")
 
# Forslag 3
skjermstorrelse_str = input("Skriv inn størrelsen til skjermen: ")
skjermstorrelse = float(skjermstorrelse_str)
nevner = (16**2 + 9**2)**0.5
faktor = skjermstorrelse/nevner
hoyde = 9*faktor
bredde = 16*faktor
print(f"En standard 16:9 skjerm med diagonal {skjermstorrelse} er "+
    f"{hoyde} høy og {bredde} brei.")
 
# Forslag 4
skjermstorrelse = input("Skriv inn størrelsen til skjermen: ")
skjermstorrelse_float = float(skjermstorrelse)
nevner = (16**2 + 9**2)**0.5
faktor = skjermstorrelse_float/nevner
hoyde = 9*faktor
bredde = 16*faktor
print(f"En standard 16:9 skjerm med diagonal {skjermstorrelse} er "+
    f"{hoyde} høy og {bredde} brei.")
 
# Forslag 5
skjermstorrelse = input("Skriv inn størrelsen til skjermen: ")
skjermstorrelse_float = float(skjermstorrelse)
print(f"En standard 16:9 skjerm med diagonal {skjermstorrelse} er "+
    f"{hoyde} høy og {bredde} brei.")
nevner = (16**2 + 9**2)**0.5
faktor = skjermstorrelse_float/nevner
hoyde = 9*faktor
bredde = 16*faktor
 
# Forslag 6
skjermstorrelse = input("Skriv inn størrelsen til skjermen: ")
skjermstorrelse_float = float(skjermstorrelse)
nevner = (16**2 + 9**2)**0.5
faktor = skjermstorrelse/nevner
hoyde = 9*faktor
bredde = 16*faktor
print(f"En standard 16:9 skjerm med diagonal {skjermstorrelse} er "+
    f"{hoyde} høy og {bredde} brei.")