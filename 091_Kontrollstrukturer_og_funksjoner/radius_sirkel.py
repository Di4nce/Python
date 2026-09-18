import math
from skriv_positivt_tall import skriv_inn_positivt_tall # undermappe.skriv_positivt_tall

def areal_sirkel(radius: float) -> float: # type hint til VSCode, radius er en float, og skal retunere en float. 
    print("Inne i areal sirkel")
    areal = math.pi*radius*radius
    return areal

tall = skriv_inn_positivt_tall("Skriv inn radius til sirkelen: ")
if tall > 2 or areal_sirkel(tall) < 10:
    print("Sant")

#arealet = areal_sirkel(5)
#print(f"arealet er: {arealet}")

