# Du skal lage en funksjon som lager ei ny liste fra ei eksisterende liste av tall. Funksjonen skal ta
# den eksisterende lista som parameter og returnere den nye lista. Annenhvert element i den nye
# lista skal være et element fra lista som kommer inn. Resten av elementene skal genereres tilfeldig
# og skal være mellom sine to nabo-elementer. Hvis funksjonen får inn ei tom liste skal den
# returnere ei tom liste. Hvis funksjonen får inn ei liste med ett element skal den returnere ei ny liste
# med det ene elementet i.
 
# Eksempel: Hvis funksjonen blir kalt på lista [5, 9, 6] skal den returnere ei liste med verdiene [5, X,
# 9, Y, 6] hvor X er et tilfeldig tall mellom 5 og 9 og Y er et tilfeldig tall mellom 6 og 9. (10%)
 
# Skriv et script som bruker funksjonen med lista [5, 8, 17, 16, 8, 5, 16, 23, 18, 11] og skriver ut
# resultatet. (3%)
 
# Skriv ditt svar her
import random

def ny_liste(liste):
    lengde = len(liste)
    counter = 0
    ny_liste = []
    for element in liste:
        ny_liste.append(element)
        if (counter + 1) != lengde:
            tall = random.randint(min(liste[counter], liste[counter+1]), max(liste[counter], liste[counter+1]))
            ny_liste.append(tall)
        counter += 1
    return ny_liste

liste1 = [5, 8, 17, 16, 8, 5, 16, 23, 18, 11]
liste2 = ny_liste(liste1)
print(liste2)