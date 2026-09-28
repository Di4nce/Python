liste1 = list()
# liste2 = []

liste1.append(5)
liste1.append(7)
liste1.append("Tester tekst")
print(liste1)

# Viser liste inni liste
liste2 = [6, 7]
liste1.append(liste2)
for element in liste1:
    print(element)

print()
print(liste1[3][0]) # Henter elementer fra inni elementer, virker ikke på eks. en int

# List slicing
liste3 = list(range(20))
print(liste3)
print(liste3[2:5])
print(liste1[2][1:6])
print(liste3[:6]) # Fra start og til men ikke med indeks 6
print(liste3[6:]) # Fra index 6 og ut liste
print(liste3[1:8:2]) # fra 1 til men ikke med 8, og steglengde 2
print(liste3[15:25]) # Skriver bare ut listen, gir ikke en exception

# Aldri modifiser liste i en for-each løkke
# liste4 = [1, 2, 3, 4, 5]
#for element in liste4:
 #   liste4.append(element + 2)
  #  print(element)

liste4 = [1, 2, 3, 4, 5]
elementer = len(liste4)
for i in range(elementer):
    liste4.append(liste4[i] + 2)
    print(liste4[i])
print(liste4)