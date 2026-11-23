# Gitt eksemplet "Enkelt kortspill" fra forelesingene. Dette eksemplet er oppgitt nederst, under
# boksen hvor du skal skrive din egen kode. Bruk denne koden for å lage en elverkabal som
# beskrevet under. Importer klassene Spillkort og Kortstokk og bruk dem til å lage elverkabalen. Du
# kan anta at disse klassene ligger i ei fil "enkelt_kortspill.py" i samme mappe som din fil. 

# Elverkabal er et kortspill for en enkelt spiller hvor du starter med å legge et kort på 9 ulike
# plasser. Deretter kan du legge kort basert på følgende to regler:
# Du kan legge to kort på to ulike plasser hvor summen av verdien til kortene som allerede
# ligger der er 11.
# Du kan legge tre kort på tre ulike plasser hvor alle plassene inneholder bildekort (knekt,
# dame, konge)

# Målet for spillet er å bruke opp kortstokken på denne måten. Har du brukt opp kortstokken har
# kabalen gått opp. Klarer du ikke å legge noen nye kort har kabalen ikke gått opp. (17%) 

# Skriv svaret ditt her. Endringer blir lagret automatisk.




# import random 
# # Klasse for en spiller
# class Spiller:
#     def __init__(self, navn, kort = None):
#         self.navn = navn
#         self.kort = kort
#     def __str__(self):
#         if self.kort is None:
#             return "Spiller: " + self.navn + " som ikke har kort enda"
#         return "Spiller: " + self.navn + " som har kortet " + str(self.kort)

# # Klasse for et spillkort
# class Spillkort:
#     ESS = 1
#     KNEKT = 11
#     DAME = 12
#     KONGE = 13
    
#     KLOVER = 1
#     RUTER = 2
#     SPAR = 3
#     HJERTER = 4

#     def __init__(self, verdi, type):
#         self.__verdi = verdi
#         self.__type = type
    
#     @property
#     def verdi(self):
#         return self.__verdi
    
#     @property
#     def type(self):
#         return self.__type
    
#     def __str__(self):
#         # <kort-type> <verdi>
#         if self.type == Spillkort.KLOVER:
#             resultat = "Kløver "
#         elif self.type == Spillkort.RUTER:
#             resultat = "Ruter "
#         elif self.type == Spillkort.SPAR:
#             resultat = "Spar "
#         elif self.type == Spillkort.HJERTER:
#             resultat = "Hjerter "
#         else:
#             resultat = "Ugyldig type "
#         if self.verdi == Spillkort.ESS:
#             resultat += "Ess"
#         elif self.verdi == Spillkort.KNEKT:
#             resultat += "Knekt"
#         elif self.verdi == Spillkort.DAME:
#             resultat += "Dame"
#         elif self.verdi == Spillkort.KONGE:
#             resultat += "Konge"
#         elif self.verdi > Spillkort.KONGE or self.verdi < 1:
#             resultat += "Ugydig verdi"
#         else:
#             resultat += str(self.verdi)
#         return resultat

# # Klasse for en kortstokk
# class Kortstokk:
#     def __init__(self):
#         self.kortene = list()
    
#     def lag_stokken(self):
#         for type in (Spillkort.KLOVER, Spillkort.RUTER, Spillkort.SPAR, Spillkort.HJERTER):
#             for verdi in range(1, 14):
#                 nytt_kort = Spillkort(verdi, type)
#                 self.kortene.append(nytt_kort)
    
#     def stokk(self):
#         random.shuffle(self.kortene)
    
#     def trekk(self):
#         resultat = self.kortene[-1]
#         del self.kortene[-1]
#         return resultat
    
#     def legg(self,kortet):
#         self.kortene.append(kortet)
        
#     def __str__(self):
#         resultat = "Kortstokk: \n"
#         for teller, kort in enumerate(self.kortene):
#             resultat += str(teller) + ": " + str(kort) + "\n"
#         return resultat
    
# def lag_spillerne():
#     antall_spillere = int(input("Skriv inn antall spillere: "))
#     spillerne = list()
#     for i in range(antall_spillere):
#         navn = input(f"Navn til spiller {i+1}: ")
#         ny_spiller = Spiller(navn)
#         spillerne.append(ny_spiller)
#     return spillerne

# def kaare_en_vinner(spillerne):
#     liste_vinnere = list()
#     for spiller in spillerne:
#         if len(liste_vinnere) == 0:
#             liste_vinnere.append(spiller)
#         else:
#             if spiller.kort.verdi > liste_vinnere[0].kort.verdi:
#                 liste_vinnere.clear()
#                 liste_vinnere.append(spiller)
#             elif spiller.kort.verdi == liste_vinnere[0].kort.verdi:
#                 liste_vinnere.append(spiller)
#     return liste_vinnere

# def spillet():
#     spillerne = lag_spillerne()

#     # Lager kortstokken
#     stokken = Kortstokk()
#     stokken.lag_stokken()
#     stokken.stokk()
    
#     # Gir spillerne kortene sine
#     print("Spillerne med kort: ")
#     for spiller in spillerne:
#         spiller.kort = stokken.trekk()
#         print(spiller)
    
#     vinnere = kaare_en_vinner(spillerne)
    
#     while len(vinnere) > 1:
#         for vinner in vinnere:
#             vinner.kort = stokken.trekk()
#         vinnere = kaare_en_vinner(vinnere)
    
#     # Skriver ut vinneren
#     print(f"Vinneren ble: {vinnere[0]}")
    
# if __name__ == "__main__":
#     spillet()