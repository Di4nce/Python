import math


class Punkt:
    # Konstruktør (Constructor)
    def __init__(self, x_koordinat = 0.0, y_koordinat = 0.0):
        # Lager instansvariabel x_koordinat
        self.x_koordinat = x_koordinat
        self.y_koordinat = y_koordinat

    @property
    def x_koordinat(self):
        return self.__x_koordinat

    @x_koordinat.setter
    def x_koordinat(self, ny_verdi):
        if ny_verdi < 0:
            raise ValueError("X-koordinat må være positiv")
        self.__x_koordinat = ny_verdi
    

    @property
    def r(self):
        return self.avstand_origo()

    @r.setter
    def r(self, ny_verdi):
        if ny_verdi < 0:
            raise ValueError("R kan ikke være negativ!")
        gammel_theta = self.theta
        self.x_koordinat = ny_verdi*math.cos(gammel_theta)
        self.y_koordinat = ny_verdi*math.sin(gammel_theta)

    @property
    def theta(self):
        return math.acos(self.x_koordinat/self.r)

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

    def kopi(self):
        return Punkt(self.x_koordinat, self.y_koordinat)

    # Spørremetode
    # Strengrepresentasjon som skal vises til brukeren
    def __str__(self): # Spesialmetode for å si hvordan objektet skal skrives ut
        return f"Punkt: ({self.x_koordinat}, {self.y_koordinat})"

    # Strengrepresentasjon til intern bruk for utvikleren
    def __repr__(self):
        return str(self)

    # For å definere er-lik sammenligningen
    def __eq__(self, annet_objekt):
        if type(annet_objekt) != Punkt:
            return False
        if self.x_koordinat == annet_objekt.x_koordinat and \
            self.y_koordinat == annet_objekt.y_koordinat:
            return True
        return False

class RettLinje:
    def __init__(self, start: Punkt, slutt = None):
        self.start = start
        if slutt is None:
            self.slutt = Punkt(0,0)
        else:
            self.slutt = slutt

    def __str__(self):
        return f"Rett linje, start {self.start} og slutt {self.slutt}."

    def lengde(self):
        return avstand(self.start, self.slutt)

    def flytt(self, avstand_x, avstand_y):
        self.start.flytt(avstand_x, avstand_y)
        self.slutt.flytt(avstand_x, avstand_y)

    

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

    print(punkt2.x_koordinat)
    print(punkt2.r)
    print(punkt2.theta)

    punkt2.r = 6  #Får en atributeError når en forsøker å skrive til den, en readonly-egenskap
    print(punkt2)
    print(punkt2.r)
    print(punkt2.theta)

    punkt2.x_koordinat = 7
    print(punkt2)
    # print(punkt2.__x_koordinat) vil ikke virke
