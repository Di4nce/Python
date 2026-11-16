# Skriv et Python script som regner ut volumet til en pyramide med kvadratisk base. Formelen for
# volumet er: V = b*b*h hvor b er lengden til sidene til kvadratet og h er høyden målt fra toppen og
# langs ei loddrett linje. Scriptet skal lese inn lengden til siden til kvadratet og høyden fra brukeren og
# skrive ut resultatet. (6%)
 
# Skriv ditt svar her

lengde = float(input("Skriv inn side-lengden til pyramiden: "))
hoyde = float(input("Skriv inn høyden til pyramiden: "))

volum = lengde*lengde*hoyde     # Skal formelen egentlig være l*l*h / 3 ??

print(f"Volumet til pyramiden er: {volum:.2f}")