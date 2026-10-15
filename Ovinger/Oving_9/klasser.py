class Bok:
    def __init__(self, tittel, forfatter, utgivelsesår=2099, antall_totalt=1):
        self.tittel = tittel
        self.forfatter = forfatter
        self.utgivelsesår = utgivelsesår    # Ny egenskap
        self.antall_totalt = antall_totalt  # Ny egenskap
        self.antall_nå = self.antall_totalt # Settes likt som total ved opprettelse (endres senere)

    def __str__(self):
        tilgjengelig = "Alle eksemplarer er utlånt"
        if self.antall_nå > 0:
            tilgjengelig = "Tilgjengelig for utlån"
        return f"{self.tittel} av {self.forfatter}. Utgitt: {self.utgivelsesår}. {tilgjengelig}"

    def laan_ut(self):  # laget metode for utlån
        if self.antall_nå > 0:  # Sjekker om det er noe igjen på "lager"
            self.antall_nå -= 1 # Trekker fra en om en kan låne ut
            return True # Retunerer True om en får lånt ut 
        else:
            return False    # Retunerer false om en ikke får lånt ut

    def lever_inn(self):
        if self.antall_nå >= self.antall_totalt:
            raise ValueError("Alle bøker er allerede levert inn")   # Ingen anelse hvilken errro som passer best
        else:
            self.antall_nå +=1

class Bibliotek:
    def __init__(self, booker = None):
        self.booker = booker
        if booker == None:
            self.booker = []
    
    def legg_til_bok(self, bok):
        self.booker.append(bok) # Legger en bok-objekt til på listen

    def vis_alle_boker(self):
        print("Liste med bøker på biblioteket:")
        for bok in self.booker:  # Printer alle bokene i booker-listen, kunne laget [0] index for bare navn
            print(bok)
        

# Oppretter noen bokobjekter
bok1 = Bok("Starting out with Python, 6. utgave", "Tony Gaddis")
bok2 = Bok("Python for realfag, 3. utgave", "Finn Aakre Hugen og Marius Lysaker")
bok3 = Bok("Objektorientert programmering med Python", "Henrik Hillestad Løvold")

# Skriver ut informasjon om bøkene
# print(bok1)
# print(bok2)
# print(bok3)

# Til testing av oppgave c) laan_ut metoden
# print(bok1.antall_nå)
# bok1.laan_ut()
# print(bok1.antall_nå)
# bok1.lever_inn()
# print(bok1.antall_nå)
# bok1.lever_inn()  # Får en feil som forventet

sandnes_biblio = Bibliotek([bok1, bok3])  # Tester om biblioklassen virker
# sandnes_biblio.vis_alle_boker()
# sandnes_biblio.legg_til_bok(bok2)
# sandnes_biblio.vis_alle_boker()

avslutt = False
while avslutt == False:
    print("// Velkommen til bibliotekets menyside \\\\")
    print("Tast 1 for å legge til ny bok")
    print("Tast 2 for å låne en bok")
    print("Tast 3 for å levere en bok")
    print("Tast 4 for å skrive ut alle bøker")
    print("Tast 5 for å avslutte")
    kommando = input("Tast inn 1-5: ")
    if kommando == "1":
        tittel = input("Skriv inn tittel for ny bok: ")
        forfatter = input("Skriv inn forfatter på boken: ")
        utgivelsesaar = input("Skriv inn utgivelsesåret: ")
        antall = int(input("Skriv inn antall eksemplarer: "))
        ny_bok = Bok(tittel, forfatter, utgivelsesaar, antall)
        sandnes_biblio.legg_til_bok(ny_bok)
        print("Følgende bok er lagt til: ", ny_bok.tittel)
    elif kommando == "2":
        print("Bøker på bibloteket: ")
        for bok in sandnes_biblio.booker:
            print(bok)
        laan_bok = input("Skriv inn tittel på bok du ønsker å låne: ")
        for bok in sandnes_biblio.booker:
            if bok.tittel == laan_bok and bok.antall_nå > 0: # sjekker opp mot tittel og om den er tilgjengelig
                print("Utlån registrert på", bok.tittel)
                bok.laan_ut()
            elif bok.tittel == laan_bok and bok.antall_nå <= 0:
                print(f"{laan_bok} finnes ikke på biblioteket")
    elif kommando == "3":
        print("Bøker på bibloteket: ")
        for bok in sandnes_biblio.booker:
            print(bok)
        lever_bok = input("Skriv inn tittel på bok du ønsker å levere inn: ")
        for bok in sandnes_biblio.booker:
            if bok.tittel == lever_bok and bok.antall_totalt != bok.antall_nå: # sjekker opp mot tittel
                print("Innlevering registrert på", bok.tittel)
                bok.lever_inn()
            elif bok.tittel == lever_bok and bok.antall_totalt == bok.antall_nå:
                print("Alle bøker er allerede levert inn. Forsøk et annet bibliotek.")
    elif kommando == "4":
        sandnes_biblio.vis_alle_boker()
    elif kommando == "5":
        avslutt = True
    print("\n")