# Lagre enhetene og konverteringen i filer og last inn ei slik fil før 
# hver batch med konverteringer. Slik kan man bruke samme script for 
# enhetene for ulike ting for eksempel tid, vekt eller hastighet.
import csv
import dictionaries as d    # måtte rename fra 01_dictionaries for å få den til å virke.

with open("Ovinger/Oving_9/maalenhet.csv", "r", encoding="Utf-8") as filen:
    filen.readline()    # hopper over første linje
    csv_filen = csv.reader(filen, delimiter=";")    # csv funksjon som er importert, lager en csv objekt
    maaleenhet = list() # lager en liste med alle måleenhetene
    antall_enheter = []
    forkortelse = []
    for verdier in csv_filen:
        maaleenhet.append(verdier[0])
        antall_enheter.append(float(verdier[1].replace(",", "."))) # Gjør en del ting på en linje i stedet for å dele opp
        forkortelse.append(verdier[2].strip(" "))   # må huske å fjerne mellomrom med strip


# print(maaleenhet)
# print(antall_enheter)
# print(forkortelse)

# slå sammen til dictonary, så kan jeg bare bruke samme script som tidligere
maaleenheter = {}
indeks = 0  # En counter for indeksen
for verdi in maaleenhet:
    maaleenheter[verdi] = [antall_enheter[indeks], forkortelse[indeks]]
    indeks += 1

# print(maaleenheter)

d.konvertering()    # henter inn script fra første del av oppgaven, så en slipper å skrive to ganger