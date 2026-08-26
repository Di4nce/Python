pris = float(input("Tast inn pris for en liter bensin: "))
liter_km = float(input("Tast inn antall liter pr. 10 km for valgt kjøretøy: "))
lengde = float(input("Tast inn kjørelengde i km: "))

total_pris = (pris * (liter_km / 10) * lengde)
print(f"Total pris på kjøreturen er {total_pris:.2f} Kr") # .2 er to desimaler etter . og f er for float