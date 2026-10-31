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

        if len(årdata)==0:  # Her var det satt variablen årstall ved en feil, rettet den til årdata :-) (StianL)
            print("Dette året har ikke data")
            #Til dette tidspunkt har alt bare være tolking av datafilen
        else:
            print(årdata[0])
            datoer = [] #Variabler for å jobbe med grafen
            snødybde = []
            nedbør = []
            middeltemperatur = []
            middelvind = []
            
#-------------------------Legger til i liste-------------------------------------------------
            for line in årdata:
                datoer.append(line["Tid"])

                if line["Snødybde"]=="-" or line["Snødybde"]=="":
                    snødybde.append(0)
                else:
                    snødybde
                    snødybde.append(float(line["Snødybde"]))
                
                if line["Nedbør"]=="-" or line["Nedbør"]=="":
                    nedbør.append(0)
                else:
                    nedbør.append(float(line["Nedbør"].replace(",",".")))

                if line["Middeltemperatur (døgn)"]=="-" or line["Middeltemperatur (døgn)"]=="":
                    middeltemperatur.append(0)
                else:
                    middeltemperatur.append(float(line["Middeltemperatur (døgn)"].replace(",",".")))
                
                if line["Middelvind"]=="-" or line["Middelvind"]=="":
                    middelvind.append(0)
                else:
                    middelvind.append(float(line["Middelvind"].replace(",",".")))

#---------------------Lager grafene--------------------------------------------------

            plt.plot(datoer, snødybde) #Snødybden
            plt.title("Snødybde")
            plt.xlabel("Dato")
            plt.ylabel("Snødybde")
            plt.show()

            plt.plot(datoer, nedbør) #Nedbøren
            plt.title("Nedbør")
            plt.xlabel("Dato")
            plt.ylabel("Nedbør")
            plt.show()

            plt.plot(datoer, middeltemperatur) #Middeltempraturen
            plt.title("Middeltemperatur")
            plt.xlabel("Dato")
            plt.ylabel("Middeltempratur")
            plt.show()

            plt.plot(datoer, middelvind) #Middelvinden
            plt.title("Høyeste middelvind")
            plt.xlabel("Dato")
            plt.ylabel("Middeltempratur")
            plt.show()
        
except FileNotFoundError:
    print("Fil existerer ikke")