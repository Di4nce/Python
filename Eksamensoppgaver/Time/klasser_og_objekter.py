class Rom:
    def __init__(self, romnavn, romtype, kapasitet):
        self.romtype = romtype
        self.romnavn = romnavn
        self.kapasitet = kapasitet

    def __str__(self):
        return f"{self.romnavn}: {self.romtype}, kapasitet: {self.kapaistet}"