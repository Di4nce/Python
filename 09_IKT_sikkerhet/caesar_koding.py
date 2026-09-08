FORSKYVNING = 3

teksten = input("Skriv inn teksten som skal krypteres: ")
resultat = ""  # Akkumulator
for tegn in teksten:
    if tegn == " ":
        resultat += tegn
        continue
    tegn = tegn.lower()
    tegnkode = ord(tegn)
    tegnkode += FORSKYVNING
    # resultat += chr(tegnkode)
    if tegnkode > 122:
        tegnkode -= 26
    if tegnkode < 96:
        tegnkode += 26
    resultat += chr(tegnkode)
print(resultat)