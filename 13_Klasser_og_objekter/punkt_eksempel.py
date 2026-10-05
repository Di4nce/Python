import math


class Punkt:
    # Konstruktør (Constructor)
    def __init__(self, x_koordinat = 0.0, y_koordinat = 0.0):
        # Lager instansvariabel x_koordinat
        self.x_koordinat = x_koordinat
        self.y_koordinat = y_koordinat

    # Spørremetode (query)
    def avstand_origo(self): # Alltid self som en av parameterne
        return math.sqrt(self.x_koordinat**2 + self.y_koordinat**2)

    # Endremetode (mutator): Relativ forflytting
    def flytt(self, avstand_x, avstand_y):
        self.x_koordinat += avstand_x
        self.y_koordinat += avstand_y

    def avstand(self, annet_punkt):
        xdiff = self.x_koordinat - annet_punkt.x_koordinat
        ydiff = self.y_koordinat - annet_punkt.y_koordinat
        return math.sqrt(xdiff**2 + ydiff**2)

    # Spørremetode
    # Strengrepresentasjon som skal vises til brukeren
    def __str__(self): # Spesialmetode for å si hvordan objektet skal skrives ut
        return f"Punkt: {self.x_koordinat}, {self.y_koordinat}"

    # Strengrepresentasjon til intern bruk for utvikleren
    def __repr__(self):
        return str(self)

class RettLinje:
    def __init__(self, start: Punkt, slutt: Punkt):
        self.start = start
        self.slutt = slutt

def avstanden(punkt1: Punkt, punkt2: Punkt):
    xdiff = punkt1.x_koordinat - punkt2.x_koordinat
    ydiff = punkt1.y_koordinat - punkt2.y_koordinat
    return math.sqrt(xdiff**2 + ydiff**2)

# Eksempel for å vise referanser
def funksjon_endrer_objekt(punktet: Punkt):
    punktet.x_koordinat = punktet.x_koordinat + 5
    print("Avslutter funksjonen") # Bare til bruk for debugging prosessen

if __name__ == "__main__":
    punkt1 = Punkt()
    punkt2 = Punkt(3, 4)
    punkt3 = punkt1
    punkt1.y_koordinat = 3
    print(punkt3.x_koordinat)
    print(punkt1.y_koordinat) # Henter ut verdien inne i objekt
    print(punkt2.y_koordinat)
    avstand = punkt2.avstand_origo()
    print(avstand)
    avstand = punkt1.avstand_origo()
    print(avstand)
    punkt1.flytt(6, 1)
    avstand = punkt1.avstand_origo()
    print(avstand)
    print(punkt1)
    avstand = punkt1.avstand(punkt2)    # Bruk av metode (funksjonn inne i klassen)
    print(avstand)
    avstand = avstanden(punkt1, punkt2) # Bruk av funksjon
    print(avstand)

    print(punkt1)
    funksjon_endrer_objekt(punkt1)
    print(punkt1)   # Punktet er en mutable objekt lik som en liste