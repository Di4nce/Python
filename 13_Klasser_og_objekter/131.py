class Bil:
    def __init__(self, eier, merke):
        self.merke = merke
        self.eier = eier
    def gass(self):
        print(f"{self.eier} øker farten på sin {self.merke}! Vrom vrom")
    def brems(self):
        print(f"{self.eier} breeeemser med sin {self.merke}!")

bil1 = Bil("Lasjern", "Mæsje")
bil2 = Bil("Tusjen", "Påsje")

bil1.gass()
bil2.brems()