import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Filbanen til CSV-fila. Denne er relativ til mappa "Ovinger/Oving_5"
filsti = "Ovinger/Oving_5/timestrafikk_sykkelmotorveien_juni_2026_innlagte_feil.csv"

# Be brukeren skrive inn en dato. Fila inneholder data fra 2026-06-01 til 2026-06-08
dato_valgt = input("Skriv inn en dato (format ÅÅÅÅ-MM-DD, f.eks. 2026-06-03): ")

# Sjekk at datoen faktisk er skrevet på riktig format før vi går videre.
# Hvis formatet er feil, avslutter vi med en tydelig melding i stedet for
# å bare vise et tomt plott.
try:
    datetime.strptime(dato_valgt, "%Y-%m-%d")
except ValueError:
    print("Datoen er ikke skrevet på riktig format (ÅÅÅÅ-MM-DD). Prøv igjen.")
    exit()

# Lister for de 24 timene i døgnet (0, 1, 2 ... 23)
timer = list(range(24))

# Lister som skal fylles med antall sykkelpasseringer for hver time
sandnes_tall = [0] * 24
stavanger_tall = [0] * 24

# Holder styr på om vi faktisk fant noen rader som matcher datoen
fant_data = False

# Åpner CSV-fila. try/except fanger opp tilfellet der fila ikke finnes
# der vi forventer, i stedet for at scriptet krasjer med en kryptisk feil.
try:
    with open(filsti, "r", encoding="utf-8") as fil:
        leser = csv.reader(fil, delimiter=";")
        next(leser)  # hopp over overskriftsraden

        for rad in leser:
            dato = rad[5]
            fra_tidspunkt = rad[6]
            retning = rad[8]
            trafikkmengde = rad[9]

            if dato == dato_valgt:
                time = int(fra_tidspunkt[0:2])

                if retning == "Totalt i retning Sandnes":
                    fant_data = True
                    # Noen rader kan ha ugyldige tall (f.eks. "-" eller "Feil")
                    # i stedet for et tall. Da varsler vi og bruker 0,
                    # i stedet for at scriptet krasjer.
                    try:
                        sandnes_tall[time] = int(trafikkmengde)
                    except ValueError:
                        print(f"Advarsel: fant ugyldig trafikktall '{trafikkmengde}' "
                              f"kl. {fra_tidspunkt} mot Sandnes. Bruker 0 i stedet.")

                elif retning == "Totalt i retning Stavanger":
                    fant_data = True
                    try:
                        stavanger_tall[time] = int(trafikkmengde)
                    except ValueError:
                        print(f"Advarsel: fant ugyldig trafikktall '{trafikkmengde}' "
                              f"kl. {fra_tidspunkt} mot Stavanger. Bruker 0 i stedet.")

except FileNotFoundError:
    print(f"Fant ikke fila '{filsti}'. Sjekk at du kjører scriptet fra riktig mappe.")
    exit()

# Hvis ingen rader i det hele tatt matchet datoen, sier vi ifra
# i stedet for å bare vise et tomt plott
if not fant_data:
    print(f"Fant ingen data for datoen {dato_valgt}. Fila dekker 2026-06-01 til 2026-06-08.")
    exit()

# Plotter de to kurvene i samme plott
plt.plot(timer, sandnes_tall, label="Mot Sandnes")
plt.plot(timer, stavanger_tall, label="Mot Stavanger")

plt.xlabel("Time på døgnet")
plt.ylabel("Antall sykkelpasseringer")
plt.title("Sykkelpasseringer " + dato_valgt)
plt.legend()
plt.show()