# Lag et Python-script som konverterer beløp i ei fil til en annen valuta og skriver dette ut i ei anna fil.
# Begge filene skal ha navn på valutaen i første linje og deretter ett beløp i hver linje. Programmet
# ditt skal:
 
# Be brukeren om navn på den første fila
# Lese inn valuta-navnet i den første fila og skrive ut dette til brukeren
# Be brukeren om navn på den andre valutaen
# Be brukeren om kursen mellom de to valutaene
# Be brukeren om navn på den andre fila
# Skrive ut navnet på den andre valutaen til den andre fila
# For hver linje etter den første i den første fila, les inn beløpet, gang det med kursen mellom
# de to valutaene, og skriv ut resultatet til den andre fila.
# Evaluering:
# 1. Lesing og skriving av filene 6 poeng
# 2. Konvertering av valutaer 4 poeng
# 3. Håndtering av feil 4 poeng. Du skal håndtere både feil i selve filbehandlingen slik som at
# brukeren har oppgitt en første fil som ikke eksisterer eller en andre fil som ikke kan skrives
# til, og feil format i selve fila. Linjer med feil format i den første fila skal du hoppe over. 4
# poeng

# Et eksempel på filformatet:
# NOK 
# 152.5 
# 134.5 
# 97.9 
# 78 
# 4563.3 
# 234.34 
# 45.6 
# 343.4 
# 23.5 
# 45.7 
# 33.6

# Skriv ditt svar her
fra_verdi = []
filnavn = input("Skriv inn navnet på filen: ")
try:
    with open(filnavn, "r", encoding="UTF-8") as filen:
        print("Valuta:", filen.readline().strip())
        # filen.readline() trengs ikke siden den kjøres inne i print
        for linje in filen:
            try:
                fra_verdi.append(float(linje.strip()))
            except ValueError:
                continue
except FileNotFoundError:
    print("Du må skrive et gyldig filnavn")
    exit()

til_valuta = input("Skriv inn navn på valuta du skal kovertere til: ")
kurs = float(input("Skriv inn kurs mellom valutaene: "))
filnavn_ny = input("Skriv navnet til filen som skal opprettes: ")

try:
    with open(filnavn_ny, "w", encoding="UTF-8") as filen:
        filen.write(til_valuta + "\n")
    with open(filnavn_ny, "a", encoding="UTF-8") as filen:
        for verdi in fra_verdi:
            konvertert = verdi * kurs
            filen.write(str(konvertert) + "\n")
except (IOError, PermissionError):
    print("Unable to write to file")