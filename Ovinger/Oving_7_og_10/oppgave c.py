import csv
import matplotlib.pyplot as plt


#--------------------------------------- Script for lesing av CSV filer --------------------------------------------------- #
def les_vaerdata(filsti):   # Denne kan hentes inn i andre python script, se i main script nedendfor hvordan å bruke
    tider = list()          # Lager en liste for hver kolonne vi skal bruke
    maks_temper = list()
    middel_temper = list()
    nedborer = list()   # Ja jeg vet, ikke helt gramatisk korrekt :-P
    middelvinder = list()
    snodybder = list()
    with open(filsti, "r", encoding="Utf-8") as filen:
        filen.readline()
        csv_filen = csv.reader(filen, delimiter=";")    # Lager en variabel med hele csv filen
        for verdier in csv_filen:   # Går gjennom hver rad i variabelen og fyller ut listene
            tid = verdier[2]        # Leser kolonnen for tid
            tider.append(tid)       # Legger til i listen vi lagde over
            maks_temp = verdier[3]
            maks_temper.append(maks_temp)
            middel_temp = verdier[4]
            middel_temper.append(middel_temp)
            nedbor = verdier[5]
            nedborer.append(nedbor)
            middelvind = verdier[6]
            middelvinder.append(middelvind)
            snodybde = verdier[7]
            snodybder.append(snodybde)
    return tider, maks_temper, middel_temper, nedborer, middelvinder, snodybder # retunerer slik at disse kan legges inn i variabler

# --------------------------------------- Hovedscript Antall pr År (10 b) ------------------------------------------------- #
def antall_pr_aar(tider, maks, maalestasjon):    # Lager en funksjon slik at den kan brukes for alle målestasjonene
    tider.pop()     # Fjerner siste tomme raden
    max_aar = {}        # Lager en tom dictionary
    teller = 0
    for tid in tider:   # Fyller opp dictionary med årene
        max_aar[int(tid[6:])] = [] # Legger inn alle årene som int
    for tid in tider:
        if maks[teller] != "-":  # Noen av værstasjonene manglet måling, da tar vi dem ikke med,
            # Kan også løses som en try, except funksjon, i tilfelle det var andre feil enn "-" i målingene
            max_aar[int(tid[6:])].append(float(maks[teller].replace(",", "."))) # Gjør om til float, bytter , med . og legger til dictionary
        teller += 1
    sommerdager = []    # Liste med antall dager over 20
    hoysommerdager = [] # Liste med antall dager over 25
    tropedager = []     # Liste med antall dager over 30
    max_aar_sortert = dict(sorted(max_aar.items()))     # 
    aar = list(max_aar_sortert.keys()) # Liste med årene

    for ar in max_aar_sortert:              # Går gjennom hver key (år) i dictonary
        sommerdag = 0
        hoysommerdag = 0
        tropedag = 0
        for temp in (max_aar_sortert[ar]):  # Går gjennom hver value i aktuell key (år)
            if temp > 30:
                tropedag += 1
            elif temp > 25:
                hoysommerdag += 1
            elif temp > 20:
                sommerdag += 1
        sommerdager.append(sommerdag)
        hoysommerdager.append(hoysommerdag)
        tropedager.append(tropedag)

    plt.subplot(2, 2, 1)
    plt.plot(aar, sommerdager, color="goldenrod")
    plt.title("Sommerdager pr år")
    plt.subplot(2, 2, 2)
    plt.plot(aar, hoysommerdager, color="darkorange")
    plt.title("Høysommerdager pr år")
    plt.subplot(2, 2, 3)
    plt.plot(aar, tropedager, color="crimson")
    plt.title("Tropedager pr år")
    plt.suptitle(maalestasjon)
    plt.tight_layout()  # Skal hindre overlapp
    plt.show()
#----------------------------------------oppgave c.py-----------------------------------------------------------
def gjennomsnitt_pr_aar(tider, middel):
    temp_pr_aar = {}

    for i in range(len(tider)):

        # Hopper over tomme datoer og manglende temperaturer
        if tider[i] == "" or middel[i] == "-":
            continue

        aar = int(tider[i][6:])

        if aar not in temp_pr_aar:
            temp_pr_aar[aar] = []

        temp_pr_aar[aar].append(
            float(middel[i].replace(",", "."))
        )

    aar_liste = []
    gjennomsnitt_liste = []

    for aar in sorted(temp_pr_aar):

        # Krever minst 300 målinger
        if len(temp_pr_aar[aar]) >= 300:

            gjennomsnitt = (
                sum(temp_pr_aar[aar])
                / len(temp_pr_aar[aar])
            )

            aar_liste.append(aar)
            gjennomsnitt_liste.append(gjennomsnitt)

    return aar_liste, gjennomsnitt_liste


def temperatursammenlikning():

    plt.figure(figsize=(10, 6))

    stasjoner = {
        "Oslo": "Nye CSV/oslo_blindern_1954_2025_med_makstemperatur.csv",
        "Røros": "Nye CSV/roeros_1954_2025_med_makstemperatur.csv",
        "Tromsø": "Nye CSV/tromsoe_1954_2025_med_makstemperatur.csv",
        "Værnes": "Nye CSV/vaernes_1954_2025_med_makstemperatur.csv",
        "Venabu": "Nye CSV/venabu_1954_2025_med_makstemperatur.csv"
    }

    for navn, fil in stasjoner.items():

        tider, maks, middel, nedbor, vind, sno = les_vaerdata(fil)

        aar, gjennomsnitt = gjennomsnitt_pr_aar(tider, middel)

        plt.plot(
            aar,
            gjennomsnitt,
            label=navn
        )

    plt.title("Gjennomsnittstemperatur per år")
    plt.xlabel("År")
    plt.ylabel("Temperatur (°C)")
    plt.grid()
    plt.legend()
    plt.show()


# ------------------------------------------ Script for oppgaven og meny ------------------------------------------- #    
if __name__ == "__main__":  # Må ha denne slik at hovedscript ikke hentes inn om en skal importere funksjonen

    fortsett = True
    while fortsett:
        print("Sommerdager pr år, velg målestasjon: ")
        print("Tast 1 for Oslo")
        print("Tast 2 for Røros")
        print("Tast 3 for Tromsø")
        print("Tast 4 for Værnes")
        print("Tast 5 for Venabu")
        print("Tast 6 for temperatursammenlikning")
        print("Tast annet for å avslutte")
        valg = input("Tast 1-5: ")
        if valg == "1":
            tider, maks, middel, nedbor, vind, snodybde = les_vaerdata("Nye CSV/oslo_blindern_1954_2025_med_makstemperatur.csv")
            # "Jukset" litt og måtte søke nettet for oppskriften for hvordan å opprette flere variabler på en gang
            antall_pr_aar(tider, maks, "Oslo")
        elif valg == "2":
            tider, maks, middel, nedbor, vind, snodybde = les_vaerdata("Nye CSV/roeros_1954_2025_med_makstemperatur.csv")
            antall_pr_aar(tider, maks, "Røros")
        elif valg == "3":
            tider, maks, middel, nedbor, vind, snodybde = les_vaerdata("Nye CSV/tromsoe_1954_2025_med_makstemperatur.csv")
            antall_pr_aar(tider, maks, "Tromsø")
        elif valg == "4":
            tider, maks, middel, nedbor, vind, snodybde = les_vaerdata("Nye CSV/vaernes_1954_2025_med_makstemperatur.csv")
            antall_pr_aar(tider, maks, "Værnes")
        elif valg == "5":
            tider, maks, middel, nedbor, vind, snodybde = les_vaerdata("Nye CSV/venabu_1954_2025_med_makstemperatur.csv")
            antall_pr_aar(tider, maks, "Venabu")
        elif valg == "6":
            temperatursammenlikning()
        else:
            fortsett = False