import csv
import matplotlib.pyplot as plt

# Filbanen til CSV-fila. Denne er relativ til mappa "Ovinger/Oving_5"
#filsti = "Ovinger/Oving_5/timestrafikk_sykkelmotorveien_juni_2026.csv"
filsti = "Ovinger/Oving_5/timestrafikk_sykkelmotorveien_juni_2026_innlagte_feil.csv" # Til å teste robusthet

# Be brukeren skrive inn en dato. Fila inneholder data fra 2026-06-01 til 2026-06-08
dato_valgt = input("Skriv inn en dato (format ÅÅÅÅ-MM-DD, f.eks. 2026-06-03): ")

# Lister for de 24 timene i døgnet (0, 1, 2 ... 23)
timer = list(range(24))

# Lister som skal fylles med antall sykkelpasseringer for hver time.
# Vi starter med 0 for alle timene, og fyller inn riktig tall etter hvert
# som vi leser gjennom fila.
sandnes_tall = [0] * 24
stavanger_tall = [0] * 24

# Åpner CSV-fila og leser den rad for rad
with open(filsti, "r", encoding="utf-8") as fil:
    leser = csv.reader(fil, delimiter=";")

    # Den første raden er bare overskrifter, så vi hopper over den
    next(leser)

    for rad in leser:
        # Henter ut de kolonnene vi trenger fra raden
        dato = rad[5]
        fra_tidspunkt = rad[6]
        retning = rad[8]
        trafikkmengde = rad[9]

        # Vi vil bare bruke radene som gjelder datoen brukeren skrev inn
        if dato == dato_valgt:
            # "Fra tidspunkt" ser ut som f.eks. "06:00"
            # De to første tegnene gir oss timen som heltall (0-23)
            time = int(fra_tidspunkt[0:2])

            # Vi er kun interessert i totalsummen for hver retning,
            # ikke tallene for hvert enkelt felt (kjørefelt)
            try:        # La inn en try her, dersom en har feil i traffikkmengden, så leser den det som 0
                if retning == "Totalt i retning Sandnes":
                    sandnes_tall[time] = int(trafikkmengde)
                elif retning == "Totalt i retning Stavanger":
                    stavanger_tall[time] = int(trafikkmengde)
            except ValueError:
                sandnes_tall[time] = 0

# Plotter de to kurvene i samme plott
plt.plot(timer, sandnes_tall, label="Mot Sandnes")
plt.plot(timer, stavanger_tall, label="Mot Stavanger")

plt.xlabel("Time på døgnet")
plt.ylabel("Antall sykkelpasseringer")
plt.title("Sykkelpasseringer " + dato_valgt)
plt.legend()
plt.show()