# Gitt Python-funksjonen skriv_ut_sum som er ment å leite gjennom ei liste tilsvarende den oppgitte
# variabelen "liste" og summere tallene for hver by. Lista inneholder en serie med strenger med
# navn på en by etterfulgt av kolon etterfulgt av et tall. For den oppgitte lista skal funksjonen skrive
# ut følgende:

# Oslo: 16
# Bergen: 12
# Trondheim: 7
# Stavanger: 2

# Beskriv hva som vil skje om man kjører koden under. Beskriv alle feilene som er i koden under og
# forklar enten med kode eller tekst hvordan å fikse problemene med koden. (10%)

# liste = ["Oslo: 5", "Bergen: 3", "Stavanger: 2", "Bergen: 9", "Oslo: 11", "Trondheim: 7"]

# def skriv_ut_sum(byliste):
#     sum_for_hver_by = dict()
#     for element in byliste:
#         komponenter = element.split(":")
#         antall = int(komponenter[1].strip())
#         sum_for_hver_by[komponenter[0]] = sum_for_hver_by[komponenter[0]] + antall
        
#     for i in range(len(sum_for_hver_by)):
#        print(sum_for_hver_by[i])
    
# if __name__ == "__main__":
#     skriv_ut_sum(liste)