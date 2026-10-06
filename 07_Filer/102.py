# Alle prisene i 102_forpris.txt skal senkes med fem kroner, 
# og legges i ny fil med samme format i 102_tilbudspris.txt

with open("07_Filer/102_tilbudspris.txt", "w", encoding="UTF-8") as new:
    new.write("")

with open("07_Filer/102_forpris.txt", "r", encoding="UTF-8") as filen:
    for linje in filen:
        ny_linje = linje.strip()
        splittet = ny_linje.split()
        tilbudspris = splittet[0] + " " + str(int(splittet[1])-5) + "\n"
        # print(tilbudspris) #Trengs ikke, bare brukt til feilsøking
        with open("07_Filer/102_tilbudspris.txt", "a", encoding="UTF-8") as tilbud:
            tilbud.write(tilbudspris)
       