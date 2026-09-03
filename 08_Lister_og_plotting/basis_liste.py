lista = [4, 6, 8, 10]

print(lista[1])

print(lista[0])

lista[2] = 9
print(lista)

print(lista[-1])

# print(lista[4])

lista.append(12)
print(lista[4])
print(lista)

print(len(lista))

print("\n test for løkke")
for element in lista:
    print(element)

strengen = "En test av strenger og metoder"
ordene = strengen.split(" ")
print(f"Antall ord: {len(ordene)}")
for ord in ordene:
    print(ord)
for posisjon, ord in enumerate(ordene):
    print(posisjon, ",", ord)
print("Andre ord: ", ordene[1])

liste2 = list()
liste2.append(2)
liste2.append(1)
liste2.append(2)
print(liste2)

liste3 = lista + liste2
print(liste3)

streng2 = "en annen streng til"
streng3 = strengen + streng2
print(streng3)
print(len(streng3))
print(streng3[1])

liste4 = liste2*3
print(liste4)

lista.append(-3)
print(lista)
print(min(lista))
print(max(lista))

liste5 = lista + ordene     # Liste med streng og tall
print(liste5)
# print(min(liste5))        # Vil få en TypeError, kan ikke sammenligne tall og ord

for index in range(min(len(lista), len(liste2))):      # Får IndexError om du velger en lenger index enn den korteste listen
    print(f"Lista: {lista[index]}, liste2 {liste2[index]} " )