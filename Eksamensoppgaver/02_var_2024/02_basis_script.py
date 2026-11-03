# Skriv et Python script som regner ut volumet til en pyramide. Programmet skal lese inn lengde,
# bredde og høyde til pyramiden som flyttall, regne ut volumet, og skrive ut volumet.
# Formelen for volumet av en pyramide er 1/3*bredde*lengde*høyde
# Merk: Det er ikke noe behov for å sjekke for lovlig input fra brukeren i denne oppgaven.

lengde = float(input("Skriv inn lengde: "))
bredde = float(input("Skriv inn bredde: "))
hoyde = float(input("Skriv inn hoyde: "))

volum = 1/3*bredde*lengde*hoyde

print(volum)