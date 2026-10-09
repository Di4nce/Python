klasser = ["Første", "Andre"]
pris_første = 500
pris_andre = 250
seteantall = 60 # kunne laget en liste som sjekket for duplikater, men ligger utenfor omfanger av oppgaven

class Togbilett:
    def __init__(self, klasse, setenummer):
        self.klasse = klasse
        self.setenummer = setenummer
        self.pris = 999
        if self.klasse not in klasser:
            print("Skriv enten Første eller Andre")
        elif self.setenummer < 1 or self.setenummer > 60:
            print("Velg et setenummer mellom 1 og 60!")
        else:
            if self.klasse == "Første":
                self.pris = pris_første
            elif self.klasse == "Andre":
                self.pris = pris_andre
            print(f"Du har kjøpt en {self.klasse}-klasse bilett på sete nr {self.setenummer}. Prisen er: {self.pris}.")

bilett1 = Togbilett("Første", 39)
bilett2 = Togbilett("Andre", 26)
bilett3 = Togbilett("førjte", 56)
bilett3 = Togbilett("Første", 69)