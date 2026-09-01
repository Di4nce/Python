import math
from forste_eksempel import skriv_inn_positivt_tall as positiv  # Kunne bare importet direkte forste eksempel, men da må man skrive navn.def()


def areal_sirkel(radius):           # verdier inn er parametere
    areal = math.pi*radius*radius
    # omkrets = ... nei, en fuknsjon bør bare brukes til en ting om gangen
    return areal                    # verdier ut er returverdier


arealet = areal_sirkel(5)
print(f"Arealet er: {arealet}")
arealet = areal_sirkel(7)
print(f"Arealet er: {arealet}")

tall = areal_sirkel(positiv("Radius til sirkelen: "))
arealet = areal_sirkel(tall)
print(f"Arealet er: {arealet}")