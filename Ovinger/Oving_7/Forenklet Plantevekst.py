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
            middeltemperatur = []
            middeltemperatur_vekst = []
            plantevekst = []

            
#-------------------------Legger til i liste-------------------------------------------------
            for line in årdata:
                datoer.append(line["Tid"])

                if line["Middeltemperatur (døgn)"]=="-" or line["Middeltemperatur (døgn)"]=="":
                    middeltemperatur.append(0)
                else:
                    middeltemperatur.append(float(line["Middeltemperatur (døgn)"].replace(",",".")))
                

            print("Datoer:", len(datoer))
            
            #---------------------Beregner plantevekst--------------------------------------------------
            for V in middeltemperatur:          #bruker middeltemperatur listen til å beregne plantevekst
                V_float = float(V)

                if V_float >= 5:
                    vekst = V_float - 5
                    plantevekst.append(vekst)
                else:
                    plantevekst.append(0)

            plantevekst_år = sum(plantevekst)
            print(f"Total plantevekst for {årstall}: {plantevekst_år}")


      
except FileNotFoundError:
    print("Fil existerer ikke")
