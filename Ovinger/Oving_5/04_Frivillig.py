import csv
import matplotlib.pyplot as plt

# Filbanen til CSV-fila. Denne er relativ til mappa "Ovinger/Oving_5"
filsti = "Ovinger/Oving_5/timestrafikk_sykkelmotorveien_juni_2026.csv"

# Be brukeren om to datoer som skal sammenliknes
dato_1 = input("Skriv inn første dato (ÅÅÅÅ-MM-DD): ")
dato_2 = input("Skriv inn andre dato (ÅÅÅÅ-MM-DD): ")

timer = list(range(24))

# Én liste med 24 plasser per retning, for hver av de to datoene
sandnes_dato1 = [0] * 24
stavanger_dato1 = [0] * 24
sandnes_dato2 = [0] * 24
stavanger_dato2 = [0] * 24

with open(filsti, "r", encoding="utf-8") as fil:
    leser = csv.reader(fil, delimiter=";")
    next(leser)  # hopp over overskriftsraden

    for rad in leser:
        dato = rad[5]
        fra_tidspunkt = rad[6]
        retning = rad[8]
        trafikkmengde = rad[9]
        time = int(fra_tidspunkt[0:2])

        # Sjekker hvilken av de to datoene raden hører til, og fyller
        # inn i riktig sett av lister
        if dato == dato_1:
            if retning == "Totalt i retning Sandnes":
                sandnes_dato1[time] = int(trafikkmengde)
            elif retning == "Totalt i retning Stavanger":
                stavanger_dato1[time] = int(trafikkmengde)
        elif dato == dato_2:
            if retning == "Totalt i retning Sandnes":
                sandnes_dato2[time] = int(trafikkmengde)
            elif retning == "Totalt i retning Stavanger":
                stavanger_dato2[time] = int(trafikkmengde)

# Plotter alle fire kurvene i samme plott
plt.plot(timer, sandnes_dato1, label=f"Mot Sandnes ({dato_1})")
plt.plot(timer, stavanger_dato1, label=f"Mot Stavanger ({dato_1})")
plt.plot(timer, sandnes_dato2, label=f"Mot Sandnes ({dato_2})")
plt.plot(timer, stavanger_dato2, label=f"Mot Stavanger ({dato_2})")

plt.xlabel("Time på døgnet")
plt.ylabel("Antall sykkelpasseringer")
plt.title(f"Sammenlikning: {dato_1} vs {dato_2}")
plt.legend()
plt.show()