import csv

# Ved strenger quotechar='"'
with open("fil sti og filnavn", "r", encoding="Utf-8") as filen:
    filen.readline()
    tidspunkter = list()
    aksellerasjoner = list()
    csv_filen = csv.reader(filen, delimiter=";")
    for verdier in csv_filen:
        tidspunkt = float(verdier[0])
        aksellerasjon = float(verdier[4])
        tidspunkter.append(tidspunkt)
        aksellerasjoner.append(aksellerasjon)

print(tidspunkter)
print(aksellerasjoner)