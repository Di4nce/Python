# Deloppgave a)
def kinetisk_energi(masse_kg, fart_m_s):
    return 0.5*masse_kg*(fart_m_s**2)

# Deloppgave b)
masse_kg = float(input("Skriv inn masse: "))
fart_m_s = float(input("Fart i m/s: "))
energi = kinetisk_energi(masse_kg, fart_m_s)
print("Den kinetiske energien blir: ", energi)