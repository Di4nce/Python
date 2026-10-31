import csv

try:
    # Leser CSV-filen
    with open("sinnes_2014_2025_med_makstemperatur.csv", "r", encoding="UTF-8") as filen:
        data = csv.DictReader(filen, delimiter=";")
    # Brukeren skriver inn årstall
        årstall = input("Skriv inn årstall (YYYY): ")
        årdata=[]
        

        for line in data:
            dato=line["Tid(norsk normaltid)"].strip()
            år=dato[6:10] #legger slik at årstallet bare skal ha det og ikke datoen
            uten_sted = {"Tid": dato,"Snødybde": line["Snødybde"], "Nedbør": line["Nedbør (døgn)"],"Maksimumstemperatur (døgn)": line["Maksimumstemperatur (døgn)"], "Middeltemperatur (døgn)": line["Middeltemperatur (døgn)"], "Middelvind": line["Høyeste middelvind (døgn)"]} 
            # uten maks temp
            if år == årstall:
                årdata.append(uten_sted)

        if len(årdata)==0:
            print("Dette året har ikke data")
        else:
            maks_temperatur = [] # Laget ny variabel for å samle makstemperaturene
            sommerdag = 0       # Counter for dager over 20 grader
            hoy_sommerdag = 0   # Counter for dager over 25 grader
            tropedag = 0        # Counter for dager over 30 grader
            
#-------------------------Legger til i liste-------------------------------------------------
            for line in årdata:
                if line["Maksimumstemperatur (døgn)"] == "-":
                        continue
                else:
                    maks_temperatur.append(float((line["Maksimumstemperatur (døgn)"]).replace(",", ".")))  # Forandrer fra ","" til "."  og gjør om til float før den legger til listen
                
            # print("Maks-temperaturer:", maks_temperatur)    # Til test/feilsøking

            for temp in maks_temperatur:
                if temp > 30:
                    tropedag += 1
                elif temp > 25:
                    hoy_sommerdag += 1
                elif temp > 20:
                    sommerdag += 1

            print(f"Antall sommerdager (temperatur over 20° C) i {årstall}: {sommerdag}")
            print(f"Antall høy-sommerdager (temperatur over 25° C) i {årstall}: {hoy_sommerdag}")
            print(f"Antall tropedager (temperatur over 30° C) i {årstall}: {tropedag}")

except FileNotFoundError:
    print("Fil existerer ikke")