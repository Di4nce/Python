# Listebyggere / listcomprehensions

# For hvert element i range(10), inkluder elementer selv  lista
liste = [x for x in range(10)]
print(liste)

# For hvert element i lista, legg element**2 til lista 2
liste2 = [x**2 for x in liste]
print(liste2)

# Tilsvarende som for-løkke
liste2 = list()
for x in liste:
    liste2.append(x**2)

# For hvert tall i range(20), hvis tall%2 er 1, inkluder tallet i listen
liste3 = [tall for tall in range(20) if tall%2 == 1]
print(liste3)

if 8 in liste3:
    print("8 er med")
else:
    print("8 er ikke med")

print(liste3.index(9))

liste4 = [1, 2,3, 4, 5, 3, 2, 1]
print(liste4.index(3))  # Finner første
# print(liste4.index(7))  # Gir en valueerror, må enten sjekke først med en if eller lage en try

liste5 = ["liste", "av", "flere", "ord"]
liste5.insert(2, "mange")  # legger inn
# liste5[2] = "mange"  # Oversirkiver
print(liste5)

liste5.remove("flere")  # Fjerner første forekomst av en verdi
print(liste5)
# liste4.remove(-1) # Får en ValueError om den ikek finnes
# print(liste4)

del liste5[2]   # Fjerner elementet på en bestemt index
print(liste5)

liste4.sort()
print(liste4)

liste4.reverse()
print(liste4)