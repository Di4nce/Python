# Lag en script som teller antall forekomster av hvert ord i
# en tekstfil

# Lager en dict medord som nøkkel og antall forekomster så langt
# som verdi

ordforekomster = {}
with open("12_Samlingsobjekter/eksempelfil.txt", encoding="UTF-8") as fila:
    for linje in fila:
        ordene = linje.split(" ")
        for ordet in ordene:
            ordet = ordet.lower()
            ordet = ordet.strip()
            ordet = ordet.strip(",-()\"—")
            if ordet in ordforekomster:
                ordforekomster[ordet] += 1
            else:
                ordforekomster[ordet] = 1
    # for ordet in ordforekomster:
    #     print(f"{ordet}: {ordforekomster[ordet]}")

    ordliste = list(ordforekomster.keys())
    ordliste.sort()
    for ordet in ordliste:
        print(f"{ordet}: {ordforekomster[ordet]}")