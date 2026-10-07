# Skriv et program som leser inn innholdet i filen og lagrer avstandene i en selvvalgt datastruktur
# Skriv inn navnet på to byer, og print ut avstanden mellom dem.

byer = []
reise_by = {}

with open ("07_Filer/103_avstand.txt", mode="r", encoding="utf-8") as filen:
    linje_nr = 0
    for linje in filen:
        # linje.strip() #Virker ikke, skulle vært ny_linje = linje.strip()
        if linje_nr == 0:
            # linje.strip("-") #Virker ikke, skulle vært ny_linje = ny_linje.strip("-")
            byer = linje.split()
            # print(byer, end="")
        else:
            by = linje.split()
            reise_by[by[0]] = by[1:]

        linje_nr += 1
    # print(reise_by)

fra_by = input("Skriv inn by du reiser fra: ")
til_by = input("Skriv inn by du reiser til: ")

if til_by in byer:
    posisjon = byer.index(til_by) - 1 # Må trekke fra en siden første er en "-" først
else:
    print("Denne byen finnes ikke i databasen")
# print(posisjon)

avstander = reise_by.get(fra_by)
avstand = avstander[posisjon]
print(f"Avstanden mellom {fra_by} og {til_by} er {avstand} km..")