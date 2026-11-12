# Fillesing, klasser og objekter
# Gitt koden under, som inneholder en klasse "Kommune". Gitt ei fil som inneholder observerte
# posisjoner av en plante- eller dyreart på følgende format:
 
# observasjonsID;antall;x-koordinat;y-koordinet
 
# Fila har kolonnetitler på første linje i fila. Fila heter "observasjoner.csv"
 
# a) Lag en funksjon som tar inn navnet på fila og ei liste med kommuner som parametere.
# Funksjonen skal lese inn fila og teller for hver kommune hvor mange observasjoner det er i den
# kommunen. Funksjonen skal returnere dette som et dictionary med navn på kommunen som
# nøkkel og antall observasjoner som verdi. 12%
 
# b) Håndter alle feil som kan oppstå under lesing av denne fila. 4%
 
# Merk: Du trenger ikke lage hele scriptet her, bare det som står i oppgaveteksten.
# Merk 2: Du må bruke metoden er_inni for å finne ut hvilken kommune en observasjon er i.
 
# Skriv ditt svar her
import csv

def kommune_obsv(filnavn, kommuneliste):
    antall_pr_kommune = {}
    try:
        with open(filnavn, "r", encoding="UTF-8") as filen:
            filen.readline()
            antall = list()
            x_koordinat = list()
            y_koordinat = list()
            csv_filen = csv.reader(filen, delimiter=";")
            linje = 2   # Hopper egentlig over øverste linje ovenfor, defnisjonssak
            for verdier in csv_filen:
                try:
                    antall.append(int(verdier[1].strip()))
                    x_koordinat.append(int(verdier[2].strip()))
                    y_koordinat.append(int(verdier[3].strip()))
                except (ValueError, IndexError):
                    print(f"Feil på linje {linje}")
                finally:
                    linje += 1
    except FileNotFoundError:
        print("Feil filnavn")
        return antall_pr_kommune    # Exit avslutter hele programmet
    for kommune in kommuneliste:
        antall_pr_kommune[kommune] = 0
        index = 0
        for verdi in antall:
            i_kommunen = kommune.er_inni(x_koordinat[index], y_koordinat[index])
            if i_kommunen:
                antall_pr_kommune[kommune] += verdi # evt +1 om en bare skal telle antall linjer med observasjon
            index += 1
    return antall_pr_kommune

# Klassen Kommune:
# class Kommune:
#     def __init__(self, navn, befolkning, omraade):
#         self.navn = navn
#         self.befolkning = befolkning1
#         self.omraade = omraade
 
#     def er_inni(self, x_koordinat, y_koordinat):
#         """Sjekker om en posisjon oppgitt med x- og y- koordinater er innenfor kommunen.
#            Returnerer True hvis posisjonen er innenfor og False ellers.
#            Du skal bruke denne metoden i denne oppgaven, men trenger ikke å vite hvordan den
#            er implementert for å løse oppgaven. Derfor er ikke implementasjonen av metoden
#            oppgitt her."""
 
# Fila:
# ObservasjonsID;antall;x-koordinat;y-koordinat
# 1;3;132;143
# 2;1;23;1324
# 3;2;145;342
# 4;1;15;956