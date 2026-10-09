class Lagersystem:
    def __init__(self):
        self.varer = []
        self.antall = 0

    def legg_til(self, vare):
        self.varer.append(vare)
        self.antall += 1

    def selg_vare(self, vare):
        if vare in self.varer:
            self.varer.remove(vare)
            self.antall -= 1
        else:
            print(f"{vare} finnes ikke i sortimentet av totalt {self.antall} varer. Gyldige varer er: {self.varer}")

butikk = Lagersystem()
butikk.legg_til("Is")
butikk.legg_til("Pizza")
# print(butikk.varer)
butikk.selg_vare("Hamburger")
butikk.selg_vare("Is")
print("Varerliste:", butikk.varer, "Antall varer:", butikk.antall)