import math

def fakultet(fakultet_av):
    resultat = 1    # Akkumulator
    for tall in range(1, fakultet_av+1):
        resultat = resultat * tall
    return resultat

def e(x=2, M=40):
    sum_verdi = 0
    for n in range(0, M + 1):
        sum_verdi = sum_verdi + (x**n) / fakultet(n)
    return sum_verdi

verdi = e()
differanse = abs(math.sqrt(verdi) - math.e) # Tror vi må bruke standard e fra math modulen?

print(f"Kvadratroten av e(x): {math.sqrt(verdi)}")
print(f"Tallet e: {math.e}" )
print(f"Differansen er: {differanse}")

for m in range(1, 101):
    verdi = e(M=m)
    differanse = abs(math.sqrt(verdi) - math.e)
    print(f"M = {m}: differanse = {differanse}")