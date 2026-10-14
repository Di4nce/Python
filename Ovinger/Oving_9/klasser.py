class Bok:
    def __init__(self, tittel, forfatter, utgivelsesår=2099, antall_totalt=1):
        self.tittel = tittel
        self.forfatter = forfatter
        self.utgivelsesår = utgivelsesår    # Ny egenskap
        self.antall_totalt = antall_totalt  # Ny egenskap
        self.antall_nå = self.antall_totalt # Settes likt som total ved opprettelse (endres senere)

    def __str__(self):
        tilgjengelig = "Alle eksemplarer er utlånt"
        if self.antall_nå > 0:
            tilgjengelig = "Tilgjengelig for utlån"
        return f"{self.tittel} av {self.forfatter}. Utgitt: {self.utgivelsesår}. {tilgjengelig}"

    def laan_ut(self):  # laget metode for utlån
        if self.antall_nå > 0:  # Sjekker om det er noe igjen på "lager"
            self.antall_nå -= 1 # Trekker fra en om en kan låne ut
            return True # Retunerer True om en får lånt ut 
        else:
            return False    # Retunerer false om en ikke får lånt ut

    def lever_inn(self):
        if self.antall_nå >= self.antall_totalt:
            raise ValueError("Alle bøker er allerede levert inn")   # Ingen anelse hvilken errro som passer best
        else:
            self.antall_nå +=1

class Bibliotek:
    def __init__(self, booker = None):
        self.booker = booker
        if booker == None:
            self.booker = []
    
    def legg_til_bok(self, bok):
        self.booker.append(bok)
        

# Oppretter noen bokobjekter
bok1 = Bok("Starting out with Python, 6. utgave", "Tony Gaddis")
bok2 = Bok("Python for realfag, 3. utgave", "Finn Aakre Hugen og Marius Lysaker")
bok3 = Bok("Objektorientert programmering med Python", "Henrik Hillestad Løvold")

# Skriver ut informasjon om bøkene
print(bok1)
print(bok2)
print(bok3)

# Til testing av oppgave c) laan_ut metoden
print(bok1.antall_nå)
bok1.laan_ut()
print(bok1.antall_nå)
bok1.lever_inn()
print(bok1.antall_nå)
# bok1.lever_inn()  # Får en feil som forventet