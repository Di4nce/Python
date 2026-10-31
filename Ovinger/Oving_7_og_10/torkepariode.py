import csv
import matplotlib.pyplot as plt

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
            uten_sted_og_maxtemp = {"Tid": dato,"Snødybde": line["Snødybde"], "Nedbør": line["Nedbør (døgn)"], "Middeltemperatur (døgn)": line["Middeltemperatur (døgn)"], "Middelvind": line["Høyeste middelvind (døgn)"]} #uten maks temp
            if årstall==år:
                årdata.append(uten_sted_og_maxtemp)

        if len(årstall)==0:
            print("Dette året har ikke data")
            #Til dette tidspunkt har alt bare være tolking av datafilen
        else:
            print(årdata[0])
            datoer = [] #Variabler for å jobbe med grafen
            nedbør = []

            
#-------------------------Legger til i liste-------------------------------------------------
            for line in årdata:
                datoer.append(line["Tid"])


                
                if line["Nedbør"]=="-" or line["Nedbør"]=="":
                    nedbør.append(0)
                else:
                    nedbør.append(float(line["Nedbør"].replace(",",".")))


            print("Datoer:", len(datoer))

            print("Nedbør:", nedbør)


            # ------------------ FINN LENGSTE TØRKEPERIODE ------------------

            lengste = 0
            nåværende = 0
            start_index = None
            lengste_start = None
            lengste_slutt = None

            for i, v in enumerate(nedbør):
                if v == 0:
                    if nåværende == 0:
                        start_index = i  # ny periode starter
                    nåværende += 1
                else:
                    if nåværende > lengste:
                        lengste = nåværende
                        lengste_start = start_index
                        lengste_slutt = i - 1
                    nåværende = 0

            # Sjekker om siste periode er den lengste
            if nåværende > lengste:
                lengste = nåværende
                lengste_start = start_index
                lengste_slutt = len(nedbør) - 1

            # Skriver ut resultat
            if lengste == 0:
                print(f"Ingen tørkeperioder i {årstall}.")
            else:
                print(f"Lengste tørkeperiode i {årstall}: {lengste} dager")
                print(f"Startdato: {datoer[lengste_start]}")
                print(f"Sluttdato: {datoer[lengste_slutt]}")

        

except FileNotFoundError:
    print("Fil existerer ikke")
