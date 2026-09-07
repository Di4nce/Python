import matplotlib.pyplot as plt

with open("kan kopiere relativ path fra filen og lime inn", "r", 
          encoding="UTF-8") as fila:
# Kan klikke enter og dele inne i en parantes for å få plass til alt evt. kan \ brukes utenfor ()
    fila.readline()
    tidspunkter = list()
    aksellerasjoner = list()
    for linje in fila:
        komponenter = linje.split(";")
        tidspunkt = float(komponenter[0])
        aksellerasjon = float(komponenter[4])
        tidspunkter.append(tidspunkt)
        aksellerasjoner.append(aksellerasjon)
print(tidspunkter)
print(aksellerasjoner)

# Tar inn to lister og lager en plot, x-retning og y-retning, må være like lange
plt.plot(tidspunkter, aksellerasjoner, marker="*")  # Marker er frivillig for å lage en stjerne i hver verdi
plt.show()
