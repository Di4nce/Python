filnavn = input("Skriv inn filnavnet: ") # Husk mappe 07_Filer/filnavn

try:
    with open(filnavn, "r", encoding="UTF-8") as tekstfilen:
        for linje in tekstfilen:
            print(linje, end="") # End er en tom streng, ungår at den avslutter på linjeskift, for da kommer den i tilleg til den scripten lager automatisk
except FileNotFoundError:
    print("Klarer ikke skrive til filen")
except IOError:
    print("Feil under skriving til fil")


# tekstfilen.close() # Trengs ikke når vi bruker en with blokk, avsluttes automatisk
print()         # Skriver ut en tom linje
print("Ferdig")

