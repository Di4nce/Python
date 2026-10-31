
import csv
import matplotlib.pyplot as plt

#------------Fra koden til Stian modifisert mer effektivt---------------
def les_vaerdata(filsti):
    tider = []
    maks_temperatur = []
    middel_temperatur = []
    nedborer = []
    middelvinder = []
    snodybder = []

    with open(filsti, "r", encoding="UTF-8") as filen:
        filen.readline()
        csv_filen = csv.reader(filen, delimiter=";")

        for verdier in csv_filen:
            tider.append(verdier[2])
            maks_temperatur.append(verdier[3])
            middel_temperatur.append(verdier[4])
            nedborer.append(verdier[5])
            middelvinder.append(verdier[6])
            snodybder.append(verdier[7])

    return tider, maks_temperatur, middel_temperatur, nedborer, middelvinder, snodybder


def les_tall(verdi):
    if verdi == "-" or verdi.strip() == "":
        return None
    return float(verdi.replace(",", "."))

#------------------funskjon for agregeringen per år----------------
def vis_statestikk(aarstall):
    try:
        tider, maks_temperatur, middel_temperatur, nedborer, middelvinder, snodybder = les_vaerdata("sinnes_2014_2025_med_makstemperatur.csv")

        måneder = []
        snø_per_måned = []
        nedbør_per_måned = []
        temperatur_per_måned = []
        vind_per_måned = []

        for i in range(len(tider)): # Går gjennom alle dagene, men tar bare med valgt år
            dato = tider[i].strip()
            år = dato[6:10]

            if år == aarstall:
                måned = dato[3:10]

                if måned not in måneder:
                    måneder.append(måned)
                    snø_per_måned.append([])
                    nedbør_per_måned.append([])
                    temperatur_per_måned.append([])
                    vind_per_måned.append([])

                j = måneder.index(måned)

                snø = les_tall(snodybder[i]) #Gjør om strngen til tall
                nedbør = les_tall(nedborer[i])
                temperatur = les_tall(middel_temperatur[i])
                vind = les_tall(middelvinder[i])

                if snø is not None:
                    snø_per_måned[j].append(snø) #Fjerner none og legger inn ny liste for januar

                if nedbør is not None:
                    nedbør_per_måned[j].append(nedbør)

                if temperatur is not None:
                    temperatur_per_måned[j].append(temperatur)

                if vind is not None:
                    vind_per_måned[j].append(vind)

        if len(måneder) == 0:
            print("Dette året har ikke data.")

        else:
            maks_snø = []
            total_nedbør = []
            maks_middeltemperatur = []
            min_middeltemperatur = []
            maks_middelvind = []

            for i in range(len(måneder)):

                # Maksimal snødybde og legger til i maks snø
                if len(snø_per_måned[i]) > 0:
                    maks_snø.append(max(snø_per_måned[i]))
                else:
                    maks_snø.append(None)

                # Total nedbør: flere enn 20 gyldige målinger
                if len(nedbør_per_måned[i]) > 20:
                    total_nedbør.append(sum(nedbør_per_måned[i]))
                else:
                    total_nedbør.append(None)
                    print(måneder[i],"- Det er ikke registrert total nedbør denne måneden.")

                # Maksimal og minimal middeltemperatur
                if len(temperatur_per_måned[i]) > 0:
                    maks_middeltemperatur.append(max(temperatur_per_måned[i]))
                    min_middeltemperatur.append(min(temperatur_per_måned[i]))
                else:
                    maks_middeltemperatur.append(None)
                    min_middeltemperatur.append(None)

                # Maksimal middelvind
                if len(vind_per_måned[i]) > 0:
                    maks_middelvind.append(max(vind_per_måned[i]))
                else:
                    maks_middelvind.append(None)

            #----------Lager grafer-----#
            fig, graf = plt.subplots(2, 2, figsize=(10, 8))
            # Graf 1: Maksimal snødybde
            graf[0,0].plot(måneder, maks_snø, marker="o")
            graf[0,0].set_title("Maksimal snødybde per måned")
            graf[0,0].set_xlabel("Måned")
            graf[0,0].tick_params(axis='x', labelrotation=45)
            graf[0,0].set_ylabel("Snødybde")

            # Graf 2: Total nedbør
            graf[0,1].plot(måneder, total_nedbør, marker="o")
            graf[0,1].set_title("Total nedbør per måned i " + aarstall)
            graf[0,1].set_xlabel("Måned")
            graf[0,1].tick_params(axis='x', labelrotation=45)
            graf[0,1].set_ylabel("Nedbør")

            # Graf 3: Maksimal og minimal middeltemperatur
            graf[1,0].plot(måneder, maks_middeltemperatur, marker="o", label="Maksimum")
            graf[1,0].plot(måneder, min_middeltemperatur, marker="o", label="Minimum")
            graf[1,0].set_title("Maksimal og minimal middeltemperatur i " + aarstall)
            graf[1,0].set_xlabel("Måned")
            graf[1,0].tick_params(axis='x', labelrotation=45)
            graf[1,0].set_ylabel("Temperatur")
            graf[1,0].legend()

            # Graf 4: Maksimal middelvind
            graf[1,1].plot(måneder, maks_middelvind, marker="o")
            graf[1,1].set_title("Maksimal middelvind per måned i " + aarstall)
            graf[1,1].set_xlabel("Måned")
            graf[1,1].tick_params(axis='x', labelrotation=45)
            graf[1,1].set_ylabel("Middelvind")
            plt.tight_layout()
            plt.show()

    except FileNotFoundError:
        print("Filen eksisterer ikke.")