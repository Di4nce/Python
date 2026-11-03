class Rom:
    def __init__(self, romnavn, romtype, kapasitet):
        self.romtype = romtype
        self.romnavn = romnavn
        self.kapasitet = kapasitet

    @property
    def romnavn(self):
        return self.__romnavn

    @romnavn.setter
    def romnavn(self, ny_verdi):
        komponenter = ny_verdi.split("-")
        if len(komponenter) != 2:
            raise ValueError("Romnummer må ha to komponenter")
        if len(komponenter[0]) == 1 or not komponenter[0].isalpha():
            raise ValueError("Romnavn må starte med en bokstav")
        
        tall = int(komponenter[1])
        self.romnavn = ny_verdi


    def __str__(self):
        return f"{self.romnavn}: {self.romtype}, kapasitet: {self.kapaistet}"