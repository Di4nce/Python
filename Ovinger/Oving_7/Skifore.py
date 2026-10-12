import csv
import matplotlib.pyplot as plt

try:
    # Leser CSV-filen
    with open("sinnes_2014_2025_med_makstemperatur.csv", "r", encoding="UTF-8") as filen:
        data = csv.DictReader(filen, delimiter=";")
    # Brukeren skriver inn årstall
        årstall = input("Skriv inn årstall (YYYY): ")
        årstall_fjor = str(int(årstall) - 1)    # Må hente inn også fjorårets data (StianL)

        # årdata_fjor = []    # Tenkte feil, trenger ikke legge dette i en egen variabel (StianL)
        årdata=[]
        

        for line in data:
            dato=line["Tid(norsk normaltid)"].strip()
            år=dato[6:10] #legger slik at årstallet bare skal ha det og ikke datoen
            if dato[3:5] == '':
                mnd = 99
            else:
                mnd=int(dato[3:5]) # må også sjekke mnd for sesong start (november) og slutt (mai) (StianL)
            # print(dato[3:5]) # Brukt til feilsøking
            uten_sted_og_maxtemp = {"Tid": dato,"Snødybde": line["Snødybde"], "Nedbør": line["Nedbør (døgn)"], "Middeltemperatur (døgn)": line["Middeltemperatur (døgn)"], "Middelvind": line["Høyeste middelvind (døgn)"]} #uten maks temp
            if (år == årstall_fjor and mnd >= 11) or (år == årstall and mnd <= 5): # Lagt til årstall_fjor også, samt også mnd (StianL) 
                årdata.append(uten_sted_og_maxtemp)

        if len(årdata)==0:  # Tror det skal være årdata og ikke årstall (Stian L)
            print("Dette året har ikke data")
            #Til dette tidspunkt har alt bare være tolking av datafilen
        else:
            # print(årdata[0])
            datoer = [] #Variabler for å jobbe med grafen
            snødybde = []
            
#-------------------------Legger til i liste-------------------------------------------------
            for line in årdata:
                datoer.append(line["Tid"])

                if line["Snødybde"]=="-" or line["Snødybde"]=="":
                    continue
                elif int(line["Snødybde"]) >= 20:
                    # snødybde
                    snødybde.append(int(line["Snødybde"]))
                
                
            # print("Datoer:", len(datoer)) # Ble brukt til feilsøking, trengs ikke lenger (Stian L)
            print("Snødybder:", snødybde)
            print(f"Antall dager med skiføre i {årstall_fjor}/{årstall}:", len(snødybde))
        
except FileNotFoundError:
    print("Fil existerer ikke")