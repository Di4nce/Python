# Du har følgende oppgavetekst og følgende forslag til programkode. Forslaget til programkoden er
# oppgitt under der du skriver inn svaret og i vedlagt .pdf fil. Beskriv hva som er problemene med
# den foreslåtte koden og hva som er løsningene, enten som programkode eller som tekst. 10%
 
# Oppgavetekst:
# "Du har et system med tre brytere som kan være enten av (0) eller på (1). Bryterne er nummerert
# 1, 2 og 3. Programmet ditt skal registrere historikken til dette systemet i ei liste. For hver gang en
# bryter blir slått av eller på skal det legges inn et nytt innslag i denne lista. Hvert innslag skal være
# ei liste som inneholder tidspunktet i indeks 0 og tilstanden til hver bryter i de neste tre plassene i
# lista. Programmet skal gå i løkke. For hver iterasjon skal programmet be brukeren skrive hvilken
# bryter som bytter tilstand og når det skjedde. For de andre bryterne skal tilstanden i det nye
# innslaget være den samme for i forrige innslag i historikken. Programmet skal avslutte og skrive
# ut historikken når brukeren skriver ei tom linje for hvilken bryter som skifter tilstand. Brukeren skal
# få en feilmelding hvis brukeren skriver inn ei tid som er tidligere enn sist innslag eller skriver inn en
# ugyldig bryter."

# Foreslått løsning:
 
# historikk = list()
# historikk.append([0, 0, 0, 0])
# fortsetter = True
# while fortsetter:
#     hvilken_bryter = input("Skriv inn hvilken bryter (1, 2 eller 3) som skifter verdi: ")
#     if hvilken_bryter == "":
#         fortsetter = False
#         break
#     tid = int(input("Skriv inn tidspunktet innslaget skjedde: "))
#     forrige_innslag = historikk[-1]
#     dette_innslaget = forrige_innslag
#     dette_innslaget[0] = tid
#     bryter_indeks = int(hvilken_bryter)
#     if dette_innslaget[bryter_indeks] == 0:
#         dette_innslaget[bryter_indeks] = 1
#     else:
#         dette_innslaget[bryter_indeks] = 0
#     historikk.append(dette_innslaget)
# print("\n Resultat:")
# print(historikk)
 
# Utskrift fra foreslått løsning:
# "
# Skriv inn hvilken bryter (1, 2 eller 3) som skifter verdi: 1 
# Skriv inn tidspunktet innslaget skjedde: 5 
# Skriv inn hvilken bryter (1, 2 eller 3) som skifter verdi: 2 
# Skriv inn tidspunktet innslaget skjedde: 8 
# Skriv inn hvilken bryter (1, 2 eller 3) som skifter verdi: 3 
# Skriv inn tidspunktet innslaget skjedde: 12 
# Skriv inn hvilken bryter (1, 2 eller 3) som skifter verdi: 2 
# Skriv inn tidspunktet innslaget skjedde: 15 
# Skriv inn hvilken bryter (1, 2 eller 3) som skifter verdi:
 
# Resultat: 
# [[15, 1, 0, 1], [15, 1, 0, 1], [15, 1, 0, 1], [15, 1, 0, 1], [15, 1, 0, 1]]
# "
 
# Dette resultatet burde ha vært:
# [[0, 0, 0, 0], [5, 1, 0, 0], [8, 1, 1, 0], [12, 1, 1, 1], [15, 1, 0, 1]]
 
# Skriv ditt svar her

# Problem med stabel og refereanser
historikk = list()
historikk.append([0, 0, 0, 0])
fortsetter = True
while fortsetter:
    hvilken_bryter = int(input("Skriv inn hvilken bryter (1, 2 eller 3) som skifter verdi: "))
    if hvilken_bryter == "":
        fortsetter = False
        break
    if hvilken_bryter > 3 or hvilken_bryter < 1:
        print("Du må velge en bryter 1, 2 eller 3!")
        continue
    tid = int(input("Skriv inn tidspunktet innslaget skjedde: "))
    forrige_innslag = historikk[-1]
    if tid < forrige_innslag[0]:
        print("Du må skrive en større tid en tidligere")
        continue
    dette_innslaget = forrige_innslag
    dette_innslaget[0] = tid
    bryter_indeks = hvilken_bryter
    if dette_innslaget[bryter_indeks] == 0:
        dette_innslaget[bryter_indeks] = 1
    else:
        dette_innslaget[bryter_indeks] = 0
    historikk.append([dette_innslaget[0], dette_innslaget[1], dette_innslaget[2], dette_innslaget[3]])

print("\n Resultat:")
print(historikk)
