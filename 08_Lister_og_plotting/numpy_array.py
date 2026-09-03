import numpy as np

lista = [4, 6, 8, 10]
array_1 = np.array(lista)
print(array_1)

array_2 = np.zeros(7)
print(array_2)

array_3 = np.arange(4) 
print(array_3)

for verdi in np.arange(0, 3, 0.2):  # Kan lage steglengde på flyttall, kan ikke dette i vanlig python
    print(f"{verdi:4.2f}")

array_5 = array_1 + array_3     # Summerer element for element
print(array_5)                  # Får feilmelding siden de er forskjellig lengde (4 og 7)