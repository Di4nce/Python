# def en_funksjon(liste = []): # Lager en tom liste når listen defineres, kan skape krøll med at flere referer til samme liste
   # liste.append(12)
    # return liste

# Hvordan lage en liste med default verdi på en måte som
# ikke gir forvirrende resultater senere
def en_funksjon(liste = None):
    if liste == None:
        liste = []
    liste.append(12)
    return liste

et_tall = 5
tall_to = et_tall
et_tall += 6
print(et_tall)
print(tall_to)

liste1 = [1, 2, 3, 4, 5]
liste2 = liste1
liste_kopi = liste1[:] # Lager en kopi av liste1 (ikke bare en referanse)

print(liste2)
liste1.append(6)
print(liste2)
print(liste_kopi)

en_funksjon(liste1)
print(liste1)

streng1 = "En streng"
streng2 = "5,7"
streng3 = streng1 + streng2
streng4 = streng2.replace(",", ".")
print(streng2)
print(streng3)
print(streng4)

liste5 = en_funksjon()
print("liste5", liste5)
liste5.append(5)
liste5.append(7)
liste6 = en_funksjon()
print("liste6", liste6)
print("liste5 etter endring", liste5)