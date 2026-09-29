import csv
import matplotlib.pyplot as plt

# Ved strenger quotechar='"'
with open("fil sti og filnavn", "r", encoding="Utf-8") as filen:
    tidspunkter = list()
    aksellerasjon = list()
    
    csv_filen = csv.DictReader(filen, delimiter=";")
    for verdier in csv_filen:
        tidspunkt = float(verdier["time (s)"])
        aksellerasjon = float(verdier["Absolut acceleration (m/s^2)"])
        tidspunkter.append(tidspunkt)
        aksellerasjon.append(aksellerasjon)

print(tidspunkter)
print(aksellerasjon)

plt.plot(tidspunkt, aksellerasjon)
plt.show