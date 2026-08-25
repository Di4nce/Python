temperatur = int(input("Temperatur: "))

if temperatur >= 19 and temperatur <= 26:
    print("Komfortabel romtemperatur")
else:
    print("Utenfor området")

if temperatur < 19 or temperatur > 26:
    print("Utenfor området!!")
else:
    print("Komfortabel romtemperatur")