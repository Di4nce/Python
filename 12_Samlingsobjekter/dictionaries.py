telefonkatalog = dict()
telefonkatalog = {}

# Setter inn nøkkel "Jan Johansen" med verdi 12345678
telefonkatalog["Jan Johansen"] = 12345678
telefonkatalog["Berit Ås"] = 876654331
telefonkatalog["Hans Hansen"] = 45454545

# Skriver ut verdien til nøkkel "Jan Johansen"
print(telefonkatalog["Jan Johansen"])
print(telefonkatalog["Hans Hansen"])

teststreng = "Berit Ås"
if teststreng in telefonkatalog:
    print(telefonkatalog[teststreng])
else:
    print(teststreng, "er ikke i dictionariet")

for nokkel in telefonkatalog:
    print(f"{nokkel}: {telefonkatalog[nokkel]}")