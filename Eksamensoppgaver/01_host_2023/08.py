# Filer og exceptions
# Du har to filer med elementer som er sammenliknbare. Den første fila heter "grupper.txt" og
# inneholder elementer på følgende format: 
# 4, 7, 2, 3
# 12, 17, 45
# 3, 11
# 15, 16, 23
 
# Hver linje representerer ei gruppe med elementer. I dette tilfellet er hvert element et heltall.
# Den andre fila heter "elementer.txt" og inneholder ett element på hver linje:
# 3
# 4
# 17
# 34
 
# Skriv et Python-script som finner hvilke av linjene i den første fila hvor minst ett av elementene i
# gruppa fins i den andre fila. Python-scriptet skal skrive ut minimum linjenummeret til hver linje i
# den første fila hvor den finner minst ett av elementene i den andre fila.
# I eksempel-filene som er oppgitt vil linje 1, 2 og 3 være riktig svar. I den første linja er tallene 3 og 4
# med i den andre fila. I den andre linja er tallet 17 med i den andre fila. I den tredje linja er tallet 3
# med i den andre fila. Ingen av tallene i den fjerde linja er med i den andre fila.
# Merk at ditt Python-script skal fungere også for andre filer enn eksempel-fila oppgitt her så lenge
# filene er i samme format.
 
# Poeng:
# - Korrekt lesing av filene 6%
# - Korrekt håndtering av feil, inkludert tomme linjer. Tomme linjer skal den hoppe over. Du trenger
# bare å håndtere feil i lesing av en av de to filene. 4%
# - Finner korrekt hver linjei den første fila som har minst ett element i den andre fila og skriver dette
# ut 6%
 
# Skriv ditt svar her
with open("grupper.txt", mode="r", encoding="utf-8") as filen:
    grupper = filen.readlines()

liste_elementer = []

with open("elementer.txt", mode="r", encoding="utf-8") as filen2:
    for line in filen2:
        try:
            liste_elementer.append(line.strip())    # Må strippe for å fjerne mellomrom og \n
        except ValueError:
            print("Hoppet over en linje grunnet feil format eller tom linje")

linjenummer = 0
for linje in grupper:
    linjenummer += 1
    funnet = False
    for tall in linje:
        if tall in liste_elementer:
            funnet = True
    if funnet == True:
        print(f"Funnet korrekt tall i linje: {linjenummer}")