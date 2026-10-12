from punkt_eksempel_properties import Punkt

class By:
    def __init__(self, navn: str, befolkning: int, posisjon: Punkt):
        self.navn = navn
        self.befolkning = befolkning
        # Komposisjon til objekt "inneholder" et annet gjennom å referere
        # til det andre objektet
        self.posisjon = posisjon

    # Eksempel på delegering: Få et "indre" objekt til å gjøre en operasjon
    # gjennom å kalle en metode på det indre objektet og retunere
    # resultatet
    def lengdegrad(self):
        return self.posisjon.x_koordinat

