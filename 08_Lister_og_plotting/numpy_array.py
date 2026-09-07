# pip3 install numpy / apt install python-numpy
import numpy as np

lista = [4, 6, 8, 10]
array_1 = np.array(lista)
print(array_1)

liste_1 = [4, 6, 8, 10]

# Lager en array med syv 0-er
array_2 = np.zeros(7)
print(array_2)

# Lager likt som en range, men arrange kan bruke med flyttall
array_3 = np.arange(4) 
print(array_3)

for verdi in np.arange(0, 3, 0.2):  # Kan lage steglengde på flyttall, kan ikke dette i vanlig python
    print(f"{verdi:4.2f}")

array_5 = array_1 + array_3     # Summerer element for element
print(array_5)                  # Får feilmelding siden de er forskjellig lengde (4 og 7)

# Linspace: start (fra og med), slutt (til og med), antall elementer. (blir lagt gjevnt fordelt)
array_6 = np.linspace(1, 10, 5)
print("Linspace", array_6)

array_7 = array_1 * 3
print(array_7)

todimensjonale_array = np.zeros((3, 4)) # Bruker ekstra () for å lage en touple
print(todimensjonale_array)
print(todimensjonale_array[1, 2])   # Legg merke til anderledes syntax enn vanlig liste [1][2]

liste6 = list() # Mulig å legge lister inne i lister
liste6.append(lista)
liste6.append(liste_1)
print(liste6)
print(liste6[0][3]) # Henter første element (lista) og fjerde element i lista, [][] anderledes syntax enn nymphy