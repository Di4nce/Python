# from collections import defaultdict   # Anbefales ikke brukt

# Lager et tomt dictionary, disse tre linjene gjør det samme
# telefonkatalog = dict()
telefonkatalog = {}
# telefonkatalog = defaultdict(int)

# Setter inn nøkkel "Jan Johansen" med verdi 12345678
telefonkatalog["Jan Johansen"] = 12345678
telefonkatalog["Berit Ås"] = 876654331
telefonkatalog["Hans Hansen"] = 45454545

# Skriver ut verdien til nøkkel "Jan Johansen"
print(telefonkatalog["Jan Johansen"])
print(telefonkatalog["Hans Hansen"])

# Viser hvordan bruke "in" operatoren for å teste om en nøkkel er med i
# et dictionary
teststreng = "Berit Ås"
if teststreng in telefonkatalog:
    print(telefonkatalog[teststreng])
else:
    print(teststreng, "er ikke i dictionariet")

tuppel = (2, 3, 4)
telefonkatalog[tuppel] = 345345345   # Liste gir en TypeError, unhashable, men tuple går bra

for nokkel in telefonkatalog:
    print(f"{nokkel}: {telefonkatalog[nokkel]}")

del telefonkatalog[(2, 3, 4)] # Sletter et par basert på nøkkel
telefonkatalog["Jan Johansen"] = 234765334  # Setter inn ny verdi


