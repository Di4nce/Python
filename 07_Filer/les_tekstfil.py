filnavn = input("Skriv inn filnavnet: ") # Husk mappe 07_Filer/filnavn

tekstfilen = open(filnavn, "r", encoding="UTF-8") # r for read, encoding og UTF-8 for å få Æ Ø Å
for linje in tekstfilen:
    print(linje, end="") # End er en tom streng, ungår at den avslutter på linjeskift, for da kommer den i tilleg til den scripten lager automatisk
tekstfilen.close() # Viktig å avslutte slik at alt blir skrevet og "andre" kan skrive til filen
print()         # Skriver ut en tom linje
print("Ferdig")

