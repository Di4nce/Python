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
            if dato[3:5] == '':
                mnd = 99
            else:
                mnd=int(dato[3:5]) # Må sjekke startmnd også
            uten_sted_og_maxtemp = {"Tid": dato,"Snødybde": line["Snødybde"], "Nedbør": line["Nedbør (døgn)"], "Middeltemperatur (døgn)": line["Middeltemperatur (døgn)"], "Middelvind": line["Høyeste middelvind (døgn)"]} #uten maks temp
            if årstall==år and mnd >= 4:
                årdata.append(uten_sted_og_maxtemp)

        if len(årdata)==0:
            print("Dette året har ikke data")
            #Til dette tidspunkt har alt bare være tolking av datafilen
        else:
            # print(årdata[0])
            datoer = []
            plantevekst = []

            middeltemperatur = []
            maks_vekst = 0
            nåværende = 0
            maks_start_dato = 0

#-------------------------Legger til i liste-------------------------------------------------
            for line in årdata:
                datoer.append(line["Tid"])

                if line["Middeltemperatur (døgn)"]=="-" or line["Middeltemperatur (døgn)"]=="":
                    middeltemperatur.append(0)
                else:
                    middeltemperatur.append(float(line["Middeltemperatur (døgn)"].replace(",",".")))


            # print("Datoer:", len(datoer))
            # print(datoer)
            print(middeltemperatur)
            #---------------------Beregner plantevekst--------------------------------------------------
            for V in middeltemperatur:          #bruker middeltemperatur listen til å beregne plantevekst
                V_float = float(V)

                if V_float >= 5:
                    vekst = V_float - 5
                    plantevekst.append(vekst)
                elif V_float < 0:
                    plantevekst.append(V_float)
                else:
                    plantevekst.append(0)

            #--------------------Beregner optimal startdato----------------------------------------------
            for i in range(len(plantevekst)):
                nåværende = sum(plantevekst[i:]) # Tenkte litt for kompliser og lagde en ny løkke,
                # men det trengs ikke, kan bare bruke indekset på listen som allerede er laget. Rettet og ferdig :-D
                if nåværende > maks_vekst:
                    maks_vekst = nåværende
                    lengste_start = datoer[i]
                
            plantevekst_år = sum(plantevekst)
            print(f"Normal total plantevekst for {årstall}: {plantevekst_år}")
            print(f"Optimal startdato er {lengste_start} som gir totalt {maks_vekst}")



except FileNotFoundError:
    print("Fil existerer ikke")