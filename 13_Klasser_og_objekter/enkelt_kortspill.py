# Du skal lage et enkelt kortspill for flere spillere. Antall
# spillere skal brukerne kunne oppgi ved start. Hver spiller
# trekker et kort fra en kortstokk. Vinneren er den spileren
# med høyest poeng på kortene. For bildekortene er konge høyere
# enn dame, og dame høyere enn knekt. Hvis flere spillere har samme
# Høyeste poengsum skal de trekke nye kort helt til de har ulik
# poengsum.

import random

class Spillkort:
    KNEKT = 11
    DAME = 12
    KONGE = 13

    KLOVER = 1
    RUTER = 2
    HJERTER = 3
    SPAR = 4

    def __init__(self, korttype, verdi):
        self.__korttype = korttype
        self.__verdi = verdi
        if self.korttype < 1 or self.korttype > 4:
            raise ValueError("gyldig kortype")
        if self.verdi < 1 or self.verdi > Spillkort.KONGE:
            raise ValueError(f"Ugyldig verdi: {verdi}")
        

    # Lager gettere men ikke settere for korttype og verdi siden disse egenskapene
    # ikke skal
    @property
    def korttype(self):
        return self.__korttype

    @property
    def verdi(self):
        return self.__verdi

    # Strengrepresentasjon på formatet "Korttype Verdi"
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
        
        if self.verdi <= 10:
            resultat += str(self.verdi)
        elif self.verdi == Spillkort.KNEKT:
            resultat += "Knekt"
        elif self.verdi == Spillkort.DAME:
            resultat += "Dame"
        elif self.verdi == Spillkort.KONGE:
            resultat += "Konge"

        return resultat

class Kortstokk:
    def __init__(self):
        # Foranderlig samling med spillkort med definert rekkefølge
        self.kortene = list()

    def lag_stokken(self):
        """
        Lager de 52 vanlige spillkortene og legger dem inn i stokken
        """
        for korttype in range(1, 5):
            for verdi in range(1, 14):
                self.kortene.append(Spillkort(korttype, verdi))

    def __str__(self):
        resultat = "Kortstokk: \n"
        for kort in self.kortene:
            resultat += str(kort) + "\n"
        return resultat

    def stokk(self):
        random.shuffle(self.kortene)

    def trekk(self):
        kortet = self.kortene[-1]
        del self.kortene[-1]
        return kortet

    def legg(self, nytt_kort):
        self.kortene.append(nytt_kort)

class Spiller:
    def __init__(self, navn, kort):
        self.navn = navn
        self.haand = list()
        self.haand.append(kort)

    def gi_kort(self, kortet):
        self.haand.append(kortet)

    def poengsum(self):
        poeng = 0           # Akkumulator
        for kort in self.haand:
            poeng += kort.verdi
        return poeng

    def __str__(self):
        resultat = "Spiller: " + self.navn + "\n"
        resultat += "Hånda til spilleren: \n"
        for kort in self.haand:
            resultat += str(kort) + "\n"
        resultat += f"Poengsum: {self.poengsum()} \n"
        return resultat

# Testekode
def testekode():
    testekort = Spillkort(Spillkort.KLOVER, Spillkort.DAME)
#    testekort.verdi = 7
    print(testekort)
    # testekort = Spillkort(3, 0)
    # print(testekort)
    stokken = Kortstokk()
    print(stokken)  # Inneholder ingen kort
    stokken.lag_stokken()
    print(stokken)
    stokken.stokk()
    print(stokken)
    kortet = stokken.trekk()
    print(stokken)
    print("Kortet: ", kortet)
    spiller = Spiller("Ola Nordmann", stokken.trekk())
    spiller.gi_kort(stokken.trekk())
    print(spiller)



def skriv_inn_positivt_tall(beskjed):
    mangler_verdi = True
    while mangler_verdi:
        try:
            positivt_tall = int(input(beskjed))
        except ValueError:
            print("Du må skrive inn et tall")
            continue
        if positivt_tall < 0:
            print("Tallet må være positiv")
        else:
            mangler_verdi = False
    return positivt_tall

def finn_vinner(spillere):
    maks_poengsum = 0
    vinnere = list()
    for spiller in spillere:
        if spiller.poengsum() > maks_poengsum:
            maks_poengsum = spiller.poengsum()
            vinnere.clear()
            vinnere.append(spiller)
        elif spiller.poengsum() == maks_poengsum:
            vinnere.append(spiller)
    return vinnere

def kjor_spill():
    antall_spillere = skriv_inn_positivt_tall("Antall spillere: ")
    spillere = list()
    stokken = Kortstokk()
    stokken.lag_stokken()
    stokken.stokk()
    for i in range(antall_spillere):
        navn = input(f"Skriv inn navn på spiller {i+1}: ")
        kort = stokken.trekk()
        spilleren = Spiller(navn, kort)
        spillere.append(spilleren)
    for spiller in spillere:
        print(spiller)
    vinnere = finn_vinner(spillere)
    while len(vinnere) > 1:
        print("Flere vinnere, gir nye kort.")
        for vinner in vinnere:
            print(vinner)
        for spiller in vinnere:
            spiller.gi_kort(stokken.trekk())
        vinnere = finn_vinner(spillere)
    print("Vinneren er: ")
    for vinner in vinnere:
        print(vinner)

if __name__ == "__main__":
    kjor_spill()