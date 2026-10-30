# Dictionaries
# Gitt ei liste av strenger på følgende format:
# [«1984: 3», «1987: 6», «1979: 2», «1984: 2», ...]
# Hvor det før kolonet er et årstall.
# Deloppgave 1: Skriv en funksjon som tar inn ei slik liste og lager og returnerer et dictionary med
# en nøkkel for hvert år og med summen av tallene bak kolonet for det året som verdi. Merk at det
# vil være flere innslag for mange av årene i lista. Det ikke er innslag i lista for hvert år og innslagene
# ikke nødvendigvis er sortert etter år. (6%)
# Deloppgave 2: Skriv en funksjon eller et script som skriver ut dictionariet som blir returnert i forrige
# deloppgave sortert etter år. Hint: Du kan hente ut et liste med nøkler fra et dictionary som ligger i
# variabelen "dictionary" med linja oppgitt under: (3%)
# nokkel_liste = list(dictionary.keys())
# Skriv ditt svar her
def lag_dictionary(liste):
    dictionary = {}
    for element in liste:
        element_liste = element.split(":")
        key = int(element_liste[0].strip())
        value = int(element_liste[1].strip())
        if key not in dictionary.keys():
            dictionary[key] = value
        else:
            dictionary[key] = value + dictionary.get(key) # eller bare += value
    return dictionary

def sorter_print(dictionary):
    # dict_sortert = dict(sorted(dictionary.items()))
    # print(dict_sortert)   
    # Denne ville teknisk sett virket, men løsningen nedenfor er nost riktigst opp mot pensum og for å få en fin liste
    nokkel_liste = list(dictionary.keys())
    nokkel_liste.sort()
    for key in nokkel_liste:
        print(key, ":", dictionary[key])