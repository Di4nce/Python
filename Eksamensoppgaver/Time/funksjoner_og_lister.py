def funksjon(liste1, liste2):
    lengde = min(len(liste1), len(liste2))
    resultat = list()
    for i in range(lengde):
        if liste2[i] > 0:
            resultat.append(liste1[i])
        else:
            resultat.append(0)
        return resultat

def alternativ_funksjon(liste1, liste2):
    lengde = min(len(liste1), len(liste2))
    resultat = list()
    for i in range(lengde):
        resultat.append(0)
    for i in range(lengde):
        if liste2[i] > 0:
            resultat[i] = liste1[i]
    return resultat

# Deloppgave b)
liste1 = [6, 3, -1, 4, 2, 4]
liste2 = [1, 3, -1, -1- 3, 2, -1, 6, 5]
resultat = funksjon(liste1, liste2)
print(resultat)