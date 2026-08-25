# Fakultet: 7! = 1*2*3*4*5*6*7

# range(5): Heltall fra og med 0 til me ikke med 5
# range(2, 7): Heltall fra og med 2 til men ikke med 7
# range(2, 7, 2): Annenhvert heltall fra og med 2 til men ikke med 7
# range(12, 2, -3): Negativ steglengde teller nedover

# off-by-one-error / Feil med 1

har_gyldig_verdi = False
while not(har_gyldig_verdi):
    try:
        fakultet_av = int(input("Fakultet av: "))
    except ValueError:
        fakultet_av = -1    # Ikke et positivt heltall
    if fakultet_av > 0:
        har_gyldig_verdi = True
    else:
        print("Fakultet eksisterer bare for positive heltall!")

resultat = 1    # Akkumulator
for tall in range(1, fakultet_av+1):
    resultat = resultat * tall
    print(tall)
print(f"Resultatet ble: {resultat}")