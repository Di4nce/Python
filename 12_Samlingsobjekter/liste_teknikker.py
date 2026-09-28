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