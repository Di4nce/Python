import csv
import matplotlib.pyplot as plt

# Filstier til de to årenes data. Begge ligger i mappa "Ovinger/Oving_5"
filsti_2025 = "Ovinger/Oving_5/August_2025.csv"
filsti_2026 = "Ovinger/Oving_5/August_2026.csv"


def gjennomsnitt_per_time(filsti):
    """Leser en CSV-fil og regner ut gjennomsnittlig antall
    sykkelpasseringer for hver time i døgnet, for begge retninger."""

    # Summer for hver time i døgnet (24 timer), for hver retning
    sum_sandnes = [0] * 24
    sum_stavanger = [0] * 24

    # Liste for å holde styr på hvor mange forskjellige dager vi har sett
    dager = []

    with open(filsti, "r", encoding="utf-8") as fil:
        leser = csv.reader(fil, delimiter=";")
        next(leser)  # hopp over overskriftsraden

        for rad in leser:
            dato = rad[5]
            fra_tidspunkt = rad[6]
            retning = rad[8]
            trafikkmengde = rad[9]
            time = int(fra_tidspunkt[0:2])

            # Legg til datoen i lista hvis vi ikke har sett den før
            if dato not in dager:
                dager.append(dato)

            if retning == "Totalt i retning Sandnes":
                sum_sandnes[time] += int(trafikkmengde)
            elif retning == "Totalt i retning Stavanger":
                sum_stavanger[time] += int(trafikkmengde)

    antall_dager = len(dager)

    # Regner ut gjennomsnittet for hver time ved å dele summen
    # på antall dager vi har data for
    snitt_sandnes = []
    snitt_stavanger = []
    for i in range(24):
        snitt_sandnes.append(sum_sandnes[i] / antall_dager)
        snitt_stavanger.append(sum_stavanger[i] / antall_dager)

    return snitt_sandnes, snitt_stavanger


timer = list(range(24))

# Regner ut gjennomsnittstall for begge årene
snitt_sandnes_2025, snitt_stavanger_2025 = gjennomsnitt_per_time(filsti_2025)
snitt_sandnes_2026, snitt_stavanger_2026 = gjennomsnitt_per_time(filsti_2026)

# Plotter alle fire kurvene i samme plott
plt.plot(timer, snitt_sandnes_2025, label="Mot Sandnes 2025")
plt.plot(timer, snitt_stavanger_2025, label="Mot Stavanger 2025")
plt.plot(timer, snitt_sandnes_2026, label="Mot Sandnes 2026")
plt.plot(timer, snitt_stavanger_2026, label="Mot Stavanger 2026")

plt.xlabel("Time på døgnet")
plt.ylabel("Gjennomsnittlig antall sykkelpasseringer")
plt.title("Gjennomsnittlig sykkeltrafikk per time: august 2025 vs august 2026")
plt.legend()
plt.show()