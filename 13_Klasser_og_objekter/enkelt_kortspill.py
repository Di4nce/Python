# Du skal lage et enkelt kortspill for flere spillere. Antall
# spillere skal brukerne kunne oppgi ved start. Hver spiller
# trekker et kort fra en kortstokk. Vinneren er den spileren
# med høyest poeng på kortene. For bildekortene er konge høyere
# enn dame, og dame høyere enn knekt. Hvis flere spillere har samme
# Høyeste poengsum skal de trekke nye kort helt til de har ulik
# poengsum.

class Spillkort:
    KNEKT = 11
    DAME = 12
    KONGE = 13

    KLOVER = 1
    RUTER = 2
    HJERTER = 3
    SPAR = 4

    def __init__(self, korttype, verdi):
        if self.korttype < 1 or self.korttype > 4:
            raise ValueError("gyldig kortype")
        if self.verdi < 1 or self.verdi > Spillkort.KONGE:
            raise ValueError(f"Ugyldig verdi: {verdi}")
        self.__korttype = korttype
        self.__verdi = verdi

    @property
    def korttype(self):
        return self.__korttype

    @property
    def verdi(self):
        return self.__verdi

    # Format Korttype: Verdi
    def __str__(self):
        if self.korttype == Spillkort.SPAR:
            resultat = "Spar "
        elif self.korttype == Spillkort.RUTER:
            resultat = "Ruter "
        elif self.korttype == Spillkort.KLOVER:
            resultat = "Kløver "
        elif self.korttype == Spillkort.HJERTER:
            resultat = "Hjerter "
        else:
            resultat = "Ugyldig korttype "
        return resultat

if __name__ == "__main__":
    testekort = Spillkort(Spillkort.KLOVER, Spillkort.DAME)
#    testekort.verdi = 7
    print(testekort)
