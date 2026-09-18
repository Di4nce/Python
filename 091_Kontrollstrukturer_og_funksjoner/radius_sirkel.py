import math
# from skriv_positivt_tall import skriv_inn_positivt_tall

def areal_sirkel(radius):
    print("Inne i areal sirkel")
    areal = math.pi*radius*radius
    return areal

tall = skriv_inn_positivt_tall("Skriv inn radius til sirkelen: ")
if tall > 2 and areal_sirkel(tall) < 10:
    print("Sant")

arealet = areal_sirkel(5)
print(f"arealet er: {arealet}")

