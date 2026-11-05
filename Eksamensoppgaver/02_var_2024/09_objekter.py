# Gitt klassene Punkt og Linje oppgitt under og i vedlagt fil, løs følgende deloppgaver. 5% pr.
# deloppgave:
 
# a) Skriv en __str__ metode for klassen Linje. Metoden skal skrive ut at det er ei linje og skrive ut
# koordinatene til alle punktene i linja.
# b) Skriv en metode "lengde" for klassen Linje. Metoden skal returnere lengden til linja. Lengden til
# ei linje er summen av avstanden mellom alle naboer i punktlista. Er det for eksempel tre punkter i
# punktlista så lengden være avstanden mellom element 0 og 1 i punktlista pluss avstanden mellom
# element 1 og 2 i punktlista.
# c) Bruk klassen Punkt som utgangspunkt for en klasse for en fri 3D vektor. En fri vektor er en
# vektor som går fra koordinat 0,0,0 til et annet koordinat. Klassen trenger derfor bare å inkludere x,
# y og z verdier for ett koordinat (punkt). Du skal lage konstruktør, __str__ metode og en metode
# som regner ut lengden til vektoren, Lengden til en 3D vektor er lengde = sqrt(x**2 + y**2 + z**2)
# d) Skriv en funsjon som legger sammen to 3D vektorer og returnerer resultatet som en ny 3D
# vektor. For å legge sammen to vektorer så legger man sammen koordinatene separat.



# Skriv ditt svar her
class Punkt:
    def __init__(self, x_koordinat, y_koordinat):
        self.x_koordinat = x_koordinat
        self.y_koordinat = y_koordinat
    def avstand(self, annet_punkt):
        avstand = ((self.x_koordinat - annet_punkt.x_koordinat)**2 +
                  (self.y_koordinat - annet_punkt.y_koordinat)**2)**0.5
        return avstand
    def __str__(self) -> str:
        return f"({self.x_koordinat}, {self.y_koordinat})"

import math as m    # må importeres for oppgave c

class Vektor:   # Svar på oppgave c)
    def __init__(self, x_koordinat, y_koordinat, z_koordinat):
        self.x_koordinat = x_koordinat
        self.y_koordinat = y_koordinat
        self.z_koordinat = z_koordinat
    def __str__(self):
        return f"Koordinator for vektor er: X: {self.x_koordinat}, Y: {self.y_koordinat}, Z: {self.z_koordinat}"
    def lengde(self):
        lengde = m.sqrt(self.x_koordinat**2 + self.y_koordinat**2 + self.z_koordinat**2)
        return lengde
    def legg_sammen(self, annen_vektor):    # Svar på oppgave d)
        ny_vektor = Vektor(self.x_koordinat + annen_vektor.x_koordinat, self.y_koordinat + annen_vektor.y_koordinat, self.z_koordinat + annen_vektor.z_koordinat)
        return ny_vektor

class Linje:
    def __init__(self, startpunkt, sluttpunkt):
        self.punktliste = list()
        self.punktliste.append(startpunkt)
        self.punktliste.append(sluttpunkt)
    def legg_til_punkt(self, punkt):
        self.punktliste.append(punkt)
    def __str__(self):  # Svar på oppgave a)
        return f"Objektet er en linje med følgende koordinater: {self.punktliste}"
    def lengde(self):   # Svar på oppgave b)
        lengde = 0
        for i in range(len(self.punktliste)-1):
            punkt_avstand = self.punktliste[i].avstand(self.punktliste[i+1])
            lengde += punkt_avstand
        return lengde
 
 
if __name__ == "__main__":
    punkt1 = Punkt(1, 2)
    punkt2 = Punkt(1, 6)
    print(punkt1.avstand(punkt2))
    linje = Linje(punkt1, punkt2)
    punkt3 = Punkt(8, 6)
    punkt4 = Punkt(1, 2)
    linje.legg_til_punkt(punkt3)
    linje.legg_til_punkt(punkt4)
    print(linje)