import math


def areal_sirkel(radius):
    areal = math.pi*radius*radius
    return areal


arealet = areal_sirkel(5)
print(f"Arealet er: {arealet}")
arealet = areal_sirkel(7)
print(f"Arealet er: {arealet}")
arealet = areal_sirkel(3)
print(f"Arealet er: {arealet}")