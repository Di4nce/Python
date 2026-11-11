# I denne oppgaven er det oppgitt 5 alternative Python-script for følgende oppgavetekst. Du skal
# krysse av for alle korrekte svaralternativer. Score: Maks 6 poeng for riktig svar. Du får
# minuspoeng for feil avkrysninger, men du får minimum 0 poeng på oppgaven som helhet.
 
# Oppgavetekst: "Du skal lage en funksjon som går gjennom ei liste med strenger på formen "
# <Navn>;<antall>". Det vil være flere navn, men samme navn vil også forekomme flere ganger. Du
# skal lage en funksjon som for hvert navn finner det høyeste tallet i lista og returnerer dette som et
# dictionary. Alle tallene er 0 eller større.
 
# Eksempel-liste:
# ["Stavanger;5",
# "Oslo;10",
# "Stavanger;3",
# "Bergen;7",
# "Trondheim;4",
# "Oslo;12",
# "Trondheim;2",
# "Oslo;7"]
 
# Velg ett eller flere alternativer
# Alternativ 1
# Alternativ 5  # Denne skal virke
# Alternativ 3
# Alternativ 2
# Alternativ 4  # Denne skal virke

# Alternativ 1
# def maks_for_liste(liste):
#     elementer = dict()
#     for element in liste:
#         komponenter = element.split(";")
#         by = komponenter[0]
#         antall = int(komponenter[1])
#         if antall not in elementer:
#             elementer.append(by)
#         elementer[by] = max(antall, elementer[by])
#     return elementer
 
# # Alternativ 2
# def maks_for_liste(liste):
#     elementer = dict()
#     for element in liste:
#         komponenter = element.split(";")
#         by = komponenter[0]
#         antall = int(komponenter[1])
#         if antall not in elementer:
#             elementer[antall] = by
#         elementer[max(antall, elementer[by])] = by
#     return elementer

# # Alternativ 3
# def maks_for_liste(liste):
#     elementer = dict()
#     for element in liste:
#         komponenter = element.split(";")
#         by = komponenter[0]
#         antall = int(komponenter[1])
#         if by in elementer:
#             elementer[by] = max(antall, elementer[by])
#         else:
#             elementer.append(by)
#     return elementer
 
# # Alternativ 4
# def maks_for_liste(liste):
#     elementer = dict()
#     for element in liste:
#         komponenter = element.split(";")
#         by = komponenter[0]
#         antall = int(komponenter[1])
#         if by in elementer:
#             elementer[by] = max(antall, elementer[by])
#         else:
#             elementer[by] = antall
#     return elementer
       
# # Alternativ 5
# def maks_for_liste(liste):
#     elementer = dict()
#     for element in liste:
#         komponenter = element.split(";")
#         by = komponenter[0]
#         antall = int(komponenter[1])
#         if by not in elementer:
#             elementer[by] = 0
#         elementer[by] = max(antall, elementer[by])
#     return elementer