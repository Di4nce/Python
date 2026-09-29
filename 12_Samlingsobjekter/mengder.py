# Sets/mengder kan bare ha en av hver, ingen garanti for rekkefølge
lag_1 = set()
lag_1.add("Einar")
lag_1.add("Hans")
lag_1.add("Åsmund")
lag_1.add("Hans")

print(lag_1)
for element in lag_1:
    print(element)

liste4 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
tall_mengde = set(liste4)
print(tall_mengde)

tall_mengde.remove(3)
print(tall_mengde)

lag_2 = set()
lag_2.add("Hans")
lag_2.add("Martin")
lag_2.add("Henrik")
print(lag_2)

print(lag_1.union(lag_2))      # Slår sammen mengde
print(lag_1.intersection(lag_2))    # Alle som er med i begge
print(lag_1.difference(lag_2))      # Alle som er med i første men ikke andre