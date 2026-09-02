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

# print(e()) # test virker
# print(e(1, 10)) # test virker

x_inn = int(input("Skriv inn et heltall for x: "))
m_inn = int(input("Skriv inn et heltall for M: "))

print("Resutatet av funksjonen er", e(x_inn, m_inn))