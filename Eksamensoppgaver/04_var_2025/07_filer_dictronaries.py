# Gitt ei liste over antall sykkelpasseringer på noen målepunkter. Fila heter "passeringer.txt" og har
# følgende format:
 
# stasjonsnavn; antall_passeringer; dato; fra_klokkeslett; til_klokkeslett
 
# Du kan anta at denne fila ligger i samme mappe som Python-scriptet ditt. Første linje i fila er
# beskrivelsen av formatet. Datoene er på formatet ÅÅÅÅ-MM-DD, for eksempel 2025-01-15 er 15.
# januar 2025.
 
# Skriv et Python-script som gjør følgende:
# a) Les inn fila, regn ut totalt antall passeringer og skriv ut totalen (8%)
# b) Les inn fila og regn ut totalt antall passeringer på en bestemt dato, som brukeren skal skrive
# inn. Skriv ut antall passeringer den datoen. (4%)
# c) Les inn fila og regn ut totalt antall passeringer for hver stasjon. Du vet ikke på forhånd hvilke
# stasjoner som ligger i fila. Skriv ut en tabell med linjer på formatet "stasjonsnavn: totalt antall
# passeringer" (6%)
 
 
 
# Skriv ditt svar her
import csv

with open("passeringer.txt", mode="r", encoding="Utf-8") as filen:
    filen.readline()
    stasjonsnavn = list()
    antall_passeringer = list()
    passeringer_totalt = 0
    datoer = list()
    stasjoner = list()
    csv_filen = csv.reader(filen, delimiter=";")
    for verdier in csv_filen:
        passeringer = int(verdier[1].strip()) # Husk rekkefølgen på dette
        passeringer_totalt += passeringer
        antall_passeringer.append(passeringer)
        datoer.append(verdier[2].strip())
        stasjoner.append(verdier[0].strip())
print(f"Totalt antall passeringer er {passeringer_totalt}") # Svar å oppgave a)

passering_pa_dato = 0
sjekk_dato = input("Skriv inn dato som skal sjekkes (ÅÅÅÅ-MM-DD): ")
indeks = 0
for dato in datoer:
    if sjekk_dato == dato:
        passering_pa_dato += antall_passeringer[indeks]
    indeks += 1
print(f"På datoen {sjekk_dato} var det totalt {passering_pa_dato} passeringer")

stasjon = {}
for enkelt_stasjon in stasjoner:
    stasjon[enkelt_stasjon] = 0
indeks = 0
for enkelt_stasjon in stasjoner:
    stasjon[enkelt_stasjon] += antall_passeringer[indeks]
    indeks += 1
for enkelt_stasjon in stasjon:
    print(f"{enkelt_stasjon}: {stasjon[enkelt_stasjon]}")







# Eksempel-datafil. Dette er bare et lite utdrag fra den ekte fila, en løsning som bare virker for dette
# konkrete eksemplet men ikke for andre tilsvarende filer vil få sterkt redusert score. Oppgaven er
# inspirert av en ekte datafil over sykkelpasseringer fra Stavanger Kommune, men dette eksemplet
# er testedata lagd for denne eksamensoppgaven.

# stasjonsnavn;antall passeringer;dato;fra_klokkeslett;til_klokkeslett
# Hillevåg;12;2025-01-15;06:00;07:00
# Hillevåg;23;2025-01-15;07:00;08:00
# Hillevåg;28;2025-01-18;07:00;08:00
# Tjensvollkrysset;9;2025-01-15;06:00;07:00
# Tjensvollkrysset;19;2025-01-15;07:00;08:00
# Tjensvollkrysset;23;2025-01-18;07:00;08:00
# Kvernevik;3;2025-01-15;06:00;07:00
# Kvernevik;9;2025-01-18;06:00;07:00
# Kvernevik;12;2025-01-18;07:00;08:00