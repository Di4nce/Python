# Vurdering av kode
# Denne oppgaven inneholder en serie med deloppgaver. Hver deloppgave inneholder en
# oppgavetekst og et forslag til kode som kanskje løser oppgaven slik den er beskrevet. Din
# oppgave er for hver av disse deloppgavene:
 
# 1: Gjør denne koden det oppgaveteksten i deloppgaven ber om? Hvis ja, skriv "ja" i tekstfeltet
# under den deloppgaven.
# 2: Hvis koden ikke gjør det oppgaveteksten ber om, skriv hva som er feilen i tekstfeltet under
# deloppgaven og beskriv hvordan å lage en korrekt løsning.
 
# Score: Opp til 5% for hver deloppgave.
 
# Deloppgave 1
# Oppgavetekst: Du ønsker å finne ut hvor lang tid det tar å kjøre en gitt vegstrekning. Lag et
# Python-script som leser inn avstanden i meter og fartsgrensa i kilometer pr. time. Scriptet skal
# regne ut hvor lang tid i sekunder det tar å kjøre denne strekningen med antakelse om at man
# kjører med en hastighet lik fartsgrensa, og skrive ut resultatet.
 
# Forslag:
# tid_i_sekunder = 0
 
# def tid_aa_kjore(avstand_i_meter, fart_i_kilometer_per_time):
#     tid_i_sekunder = avstand_i_meter / (fart_i_kilometer_per_time * 1000 / 3600)
 
# avstand_i_meter = float(input("Avstand i meter: "))
# fartsgrense = float(input("Fartsgrense i km/t: "))
# tid_aa_kjore(avstand_i_meter, fartsgrense)
# print(tid_i_sekunder)
# Skriv ditt svar her:
# MAngler en return og/eller endrer ikke en global variabel
def tid_aa_kjore(avstand_i_meter, fart_i_kilometer_per_time):
    tid_i_sekunder = avstand_i_meter / (fart_i_kilometer_per_time * 1000 / 3600)
    return tid_i_sekunder

avstand_i_meter = float(input("Avstand i meter: "))
fartsgrense = float(input("Fartsgrense i km/t: "))
tid_i_sekunder = tid_aa_kjore(avstand_i_meter, fartsgrense)
print(tid_i_sekunder)

# Deloppgave 2
# Oppgavetekst: Skriv en funksjon som tar inn to lister. Funksjonen skal lage ei ny liste som bare
# inneholder de elementene i liste 1 som også finnes i liste 2.
 
# Forslag:
# def med_i_begge(liste1, liste2):
#     resultat = list()
#     for element in liste1:
#         if element in liste2:
#             resultat.append(element)
#     return resultat
 
# Skriv ditt svar her
# Ja, dette skal virke som tiltenkt

# Deloppgave 3
# Oppgave: Skriv en funksjon som tar inn to lister med tall. Funksjonen skal lage ei ny liste hvor
# elementet på posisjon i i resultatet skal være summen av elementene ved posisjon i i de to listene
# som kommer inn. Hvis listene som kommer inn er av ulik lengde skal resultatet ha lengde som
# den korteste av dem.
 
# Forslag:
# def sum_liste(liste1, liste2):
#     resultat = list()
#     for i in range(len(liste1)):
#         resultat.append(liste1[i] + liste2[i])
#     return resultat
 
# Skriv ditt svar her:
# Bruker lengden til liste1, selv om denne er lengst
def sum_liste(liste1, liste2):
    resultat = list()
    if len(liste1) > len(liste2):
        lengde = len(liste2)
    else:
        lengde = len(liste1)
    for i in range(lengde):
        resultat.append(liste1[i] + liste2[i])
    return resultat


# Deloppgave 4
# Oppgave: Gitt klassene Punkt og Linje. Klassen Linje representerer ei linje som består av ei liste
# med punkter hvor det er rette linjer mellom nabopunkter i lista. Lag en funksjon som leser ei linje
# tekst i Well-Known Text format (forkortet WKT), oppgitt under, og lager et Linje objekt fra dette
# formatet. WKT-formatet er et format for å lagre geometriske objekter slik at de kan leses av både
# mennesker og maskiner. Linjer i WKT-format er representert som strenger i Python.
 
# Eksempel på WKT-format for ei linje:
 
# LINESTRING(5 10,10 10,10 15,5 20)
 
# Dette representerer ei linje som starter i punktet med x-kooridinat 5 og y-koordinat 10, heretter
# representert som (5, 10), går gjennom punktene (10, 10), (10, 15) og slutter i punktet (5, 20).
 
# Generell beskrivelse av formatet:
# LINESTRING(<punkt>, <punkt>, ..., <punkt>)
# Ei linje må inneholde minst to punkter, men kan inneholde så mange som trengs. Hvert punkt er
# oppgitt med sine x- og y-koordinater med åpenrom mellom seg. Merk at x- og y- koordinatene er
# bare skilt med dette åpenrommet.
 
# # Gitt, du kan anta at denne er korrekt
# class Punkt:
#     def __init__(self, x_koordinat, y_koordinat):
#         self.x_koordinat = x_koordinat
#         self.y_koordinat = y_koordinat
 
 
# # Gitt, du kan anta at denne er korrekt
# class Linje:
#     def __init__(self, startpunkt, sluttpunkt):
#         self.punktliste = list()
#         self.punktliste.append(startpunkt)
#         self.punktliste.append(sluttpunkt)
 
#     def legg_til_punkt(self, punkt):
#         self.punktliste.append(punkt)
 
 
# # Forslag til løsning
# def les_linje_fra_WKT(wkt_streng):
#     if wkt_streng.find('LINESTRING') == -1:
#         return None
#     punktliste = list()
#     punktliste_streng = wkt_streng[11:-1].split(',')
#     for punkt in punktliste_streng:
#         koordinater = punkt.split(' ')
#         x_koordinat = float(koordinater[0])
#         y_koordinat = float(koordinater[1])
#         punktliste.append(Punkt(x_koordinat, y_koordinat))
#     return Linje(punktliste[0], punktliste[1])
 
# Skriv ditt svar her
# Lager bare linje for de to første punktene, 
# må bruke metoden for legg_til_punkt på linje-objektet for resterende
def les_linje_fra_WKT(wkt_streng):
    if wkt_streng.find('LINESTRING') == -1:
        return None
    punktliste = list()
    punktliste_streng = wkt_streng[11:-1].split(',')    #5 10
    for punkt in punktliste_streng:
        koordinater = punkt.split(' ')
        x_koordinat = float(koordinater[0])
        y_koordinat = float(koordinater[1])
        punktliste.append(Punkt(x_koordinat, y_koordinat))
    linje = Linje(punktliste[0], punktliste[1]) 
    for punkt in punktliste[2:]:
        linje.legg_til_punkt(punkt)
    return linje