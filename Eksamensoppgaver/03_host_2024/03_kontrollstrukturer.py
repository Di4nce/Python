# Oppgaven går ut på å plassere de oppgitte kodeblokkene i riktig rekkefølge og velge ut de riktige
# kodeblokkene. Ikke alle kodeblokkene skal brukes. Kodeblokkene skal plasseres lik at de løser
# følgende oppgave:
# "Programmet skal skrive ut en serie med år og om året er skuddår eller ikke. Brukeren skal skrive
# inn hvilket år programmet skal starte og slutt på, og så skal programmet for hvert år fra og med
# startåret, til og med sluttåret, skrive ut om året er et skuddår eller ikke."
# Merk at symbolet "-->" er brukt for indentering siden vanlig indentering ikke er synlig i denne
# oppgaevtypen i Inspera.

# -->else:
# if skuddaar(aar):
# for aar in range(start_aar, slutt_aar+1): 
# -->if skuddaar(aar):
# else: 
# -->print(f"Året {aar} er ikke et skuddår")
# -->print(f"Året {aar} er et skuddår") 
# for aar in range(start_aar, slutt_aar):
# start_aar = int(input("Skriv inn startår: ")) #hører sammen
# slutt_aar = int(input("Skriv inn sluttår: ")) #hører sammen
# -->-->print(f"Året {aar} er et skuddår")
# for aar in range(start_aar+1, slutt_aar): 
# -->-->print(f"Året {aar} er ikke et skuddår")
 
# Score: 6%, 1% for hver riktig plasserte kodeblokk.
# Hjelp
# # Oppgitt funksjon
# def skuddaar(aaret):
#     if aaret%400 == 0:
#         return True
#     if aaret%100 == 0:
#         return False
#     if aaret%4 == 0:
#         return True
#     return False
 
# Flytt riktig kodebit til riktig sted for å skrive programmet. Rekkefølgen er viktig her. Å bruke riktig
# kodebit er også viktig, det er ikke alle kodebitene over som skal brukes.
#
#
#
#
#
#

#Oppgitt funksjon med samme markør for indentering som kodefragmentene du skal bruke i ditt
# svar bruker:
# def skuddaar(aaret):
# -->if aaret%400 == 0:
# -->-->return True
# -->if aaret%100 == 0:
# -->-->return False
# -->if aaret%4 == 0:
# -->-->return True
# -->return False
