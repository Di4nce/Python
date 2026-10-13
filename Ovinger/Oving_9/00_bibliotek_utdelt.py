class Bok:
    def __init__(self, tittel, forfatter):
        self.tittel = tittel
        self.forfatter = forfatter

    def __str__(self):
        return f"{self.tittel} av {self.forfatter}"


# Oppretter noen bokobjekter
bok1 = Bok("Starting out with Python, 6. utgave", "Tony Gaddis")
bok2 = Bok("Python for realfag, 3. utgave", "Finn Aakre Hugen og Marius Lysaker")
bok3 = Bok("Objektorientert programmering med Python", "Henrik Hillestad Løvold")

# Skriver ut informasjon om bøkene
print(bok1)
print(bok2)
print(bok3)
