filnavn = input("Skriv inn filnavnet: ")

linjenummer = 0     # Teller
try:
    with open(filnavn, "r", encoding="UTF-8") as tekstfilen:
        for linje in tekstfilen:
            linjenummer += 1
            try:
                tallet = float(linje)
            except ValueError:
                print(f"Feilformatert linje: {linjenummer}")
                continue
except FileNotFoundError:
    print("Klarer ikke skrive til filen")
except IOError:
    print("Feil under skriving til fil")
print()
print("Ferdig")