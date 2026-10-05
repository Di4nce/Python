tallrekke = []

with open ("07_Filer/101.txt", mode="r", encoding="utf-8") as filen:
    for line in filen:
        tall = line.strip()
        tallrekke.append(int(tall))
print(tallrekke)

# Summen av tallene
summen = sum(tallrekke)
print(f"Summen av alle tallene er: {summen}")
# Snittet av tallene
snitt = summen / len(tallrekke)
print(f"Snittet er: {snitt}")
# Det høyeste tallet
maximum = max(tallrekke)
print(f"Det høyeste tallet er: {maximum}")
# Det laveste tallet
laveste = min(tallrekke)
print(f"Og det laveste tallet.. er....: {laveste}")