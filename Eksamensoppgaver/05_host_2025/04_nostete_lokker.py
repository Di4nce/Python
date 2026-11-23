# Skriv en funksjon som tar inn ei liste "liste" og et heltall "antall_elementer". Funksjonen skal regne
# ut det høyeste snittet av antall_elementer etterfølgende elementer i lista.  

# Eksempel: Gitt lista [2, 9, 5, 6, 7, 8, 7, 6, 5, 3] og antall_elementer 3. Høyeste snitt over tre
# etterfølgende elementer blir 7,3 som er gjennomsnitt av elementene 7, 8 og 7. 

# Funksjonen din skal håndtere alle lister med tall. Hvis lista ikke er lang nok (den må ha minst et
# antall elementer lik parameteren "antall_elementer") skal funksjonen returnere gjennomsnittet av
# alle elementene i lista. (8%) 

# Skriv svaret ditt her. Endringer blir lagret automatisk.
def sjekk_gjennomsnitt(liste, antall_elementer):
    hoyeste_snitt = 0
    if len(liste) < antall_elementer:
        summen = 0
        for tall in liste:
            summen += tall
        hoyeste_snitt = sum / len(liste)
    else:
        index_tall = 0  # Må huske hvilket tall man er på
        for tall in range(len(liste)-antall_elementer+1):
            index = index_tall  # For midlertidig telling av de neste tallene fra hovdtallet
            ny_sum = 0
            for i in range(antall_elementer):
                ny_sum += liste[index]
                index += 1
            ny_snitt =  ny_sum / antall_elementer
            if ny_snitt > hoyeste_snitt:
                hoyeste_snitt = ny_snitt
            index_tall += 1
    return hoyeste_snitt