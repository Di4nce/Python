class Bok:
    def __init__(self, tittel, forfatter, utgivelsesaar=9999, utgave=1):
        self.tittel = tittel
        self.forfatter = forfatter   # Lagrer dette som en liste, nei, fikser dette lenger nede
        self.utgivelsesaar = utgivelsesaar    # Ny egenskap
        self.utgave = utgave    # Lagt til slutt i init for å ikke lage krøll

class Utlaan:
    def __init__(self, bok, antall_totalt=1):
        self.bok = bok
        self.antall_totalt = antall_totalt
        self.antall_naa = self.antall_totalt

    def __str__(self):
        tilgjengelig = "Alle eksemplarer er utlånt"
        if self.antall_naa > 0:
            tilgjengelig = "Tilgjengelig for utlån"
        forfatter_tekst = ""
        if type(self.bok.forfatter) is list:
            for forfatter in self.bok.forfatter:
                forfatter_tekst = forfatter_tekst + str(forfatter) + ", "   # For å unngå å vise som en liste
            forfatter_strippet = forfatter_tekst.strip(", ") # Skal fjerne de ytterste (i dette tilfellet siste , )
        else:
            forfatter_strippet = self.bok.forfatter     # Egentlig ikke strippet, men kaller det det for enkelt hets skyld
        return f"{self.bok.tittel} av {forfatter_strippet}. Utgitt: {self.bok.utgivelsesaar}. {tilgjengelig}"

    def laan_ut(self):  # laget metode for utlån
        if self.antall_naa > 0:  # Sjekker om det er noe igjen på "lager"
            self.antall_naa -= 1 # Trekker fra en om en kan låne ut
            return True # Retunerer True om en får lånt ut 
        else:
            return False    # Retunerer false om en ikke får lånt ut

    def lever_inn(self):
        if self.antall_naa >= self.antall_totalt:
            raise ValueError("Alle bøker er allerede levert inn")   # Ingen anelse hvilken errro som passer best
        else:
            self.antall_naa +=1
        

class Bibliotek:
    def __init__(self, booker = None):
        self.booker = booker
        if booker == None:
            self.booker = []
    
    def legg_til_bok(self, utlaan):
        self.booker.append(utlaan) # Legger en bok-objekt til på listen

    def vis_alle_boker(self):
        print("Liste med bøker på biblioteket:")
        for bok in self.booker:  # Printer alle bokene i booker-listen, kunne laget [0] index for bare navn
            print(bok)

    def antall_utlaant(self):
        self.antall = 0
        for bok in self.booker:
            antall = bok.antall_totalt - bok.antall_naa
            self.antall += antall
        print("Antall bøker utlånt: ", self.antall)
        

# Oppretter noen bokobjekter
bok1 = Bok("Starting out with Python, 6. utgave", "Tony Gaddis")
bok2 = Bok("Python for realfag, 3. utgave", "Finn Aakre Hugen og Marius Lysaker")
bok3 = Bok("Objektorientert programmering med Python", "Henrik Hillestad Løvold")
bok4 = Bok("Hvorfor er jorden rund??", ["Fred", "Kåre", "Anette"])

bok1_utlaan = Utlaan(bok1)
bok2_utlaan = Utlaan(bok2, 2) # Tester om det det fungerer å legge til antall 2 (standard er 1)
bok3_utlaan = Utlaan(bok3)
bok4_utlaan = Utlaan(bok4)

sandnes = Bibliotek([bok1_utlaan, bok3_utlaan, bok4_utlaan])  # Oppretter et bibliotek

# sandnes.antall_utlaant()

avslutt = False
while avslutt == False:
    print("// Velkommen til bibliotekets menyside \\\\")
    print("Tast 1 for å legge til ny bok")
    print("Tast 2 for å låne en bok")
    print("Tast 3 for å levere en bok")
    print("Tast 4 for å liste opp alle bøker")
    print("Tast 5 for å skrive bøkene til fil")
    print("Tast 6 for å lese fra fil")
    print("Tast 7 for å søke etter bok")
    print("Tast 8 for å avslutte")
    kommando = input("Tast inn 1-8: ")
    print("\n")

    if kommando == "1":
        tittel = input("Skriv inn tittel for ny bok: ")
        antall_forfattere = input("Er det flere enn en forfatter Ja/Nei: ")
        if antall_forfattere == "Nei":
            forfatter = input("Skriv inn forfatter på boken: ")
        else:
            forfatter = []
            loop = True
            while loop:
                forfatter_liste = input("Skriv inn en av forfatterne (tast 5 for å avslutte): ")
                if forfatter_liste == "5":
                    loop = False
                else:
                    forfatter.append(forfatter_liste)
        utgivelsesaar = input("Skriv inn utgivelsesåret: ")
        antall = int(input("Skriv inn antall eksemplarer: "))
        utgave = int(input("Skriv inn utgaven: "))  # Legger til utave for alle nye bøker
        ny_bok = Bok(tittel, forfatter, utgivelsesaar, utgave)
        ny_utlaan = Utlaan(ny_bok, antall)
        sandnes.legg_til_bok(ny_utlaan)
        print("Følgende bok er lagt til: ", ny_bok.tittel)
        print("\n")
        input("Trykk Enter på tastaturet for å gå tilbake til meny")

    elif kommando == "2":
        print("Bøker på bibloteket: ")
        for bok in sandnes.booker:
            print(bok)
        print("\n")
        laan_bok = input("Skriv inn tittel på bok du ønsker å låne: ")
        bok_ok = False      # Kansje enklere å lage en mer kompleks if loop med en egen metode for å sjekke om de er tilgjengelige
        for bok in sandnes.booker:
            if bok.bok.tittel == laan_bok and bok.antall_naa > 0: # sjekker opp mot tittel og om den er tilgjengelig
                print("Utlån registrert på", bok.bok.tittel)
                bok.laan_ut()
                bok_ok = True
            elif bok.bok.tittel == laan_bok and bok.antall_naa <= 0:
                print(f"Alle {laan_bok} er utlånt")
        if bok_ok == False:  # Gir en beskjed om om boken ikke er tilgjengelig
            print("Valgte bok finnes ikke")
        print("\n")
        input("Trykk Enter på tastaturet for å gå tilbake til meny")

    elif kommando == "3":
        print("Bøker på bibloteket: ")
        bok_ok = False      # Kansje enklere å lage en mer kompleks if loop med en egen metode for å sjekke om de er tilgjengelige
        for bok in sandnes.booker:
            print(bok)
        print("\n")
        lever_bok = input("Skriv inn tittel på bok du ønsker å levere inn: ")
        for bok in sandnes.booker:
            if bok.bok.tittel == lever_bok and bok.antall_totalt != bok.antall_naa: # sjekker opp mot tittel
                print("Innlevering registrert på", bok.bok.tittel)
                bok.lever_inn()
                bok_ok = True
            elif bok.bok.tittel == lever_bok and bok.antall_totalt == bok.antall_naa:
                print("Alle bøker er allerede levert inn. Forsøk et annet bibliotek.")
                bok_ok = True
        if bok_ok == False:  # Gir en beskjed om om boken ikke er tilgjengelig
            print("Valgte bok finnes ikke")
        print("\n")
        input("Trykk Enter på tastaturet for å gå tilbake til meny")

    elif kommando == "4":
        sandnes.vis_alle_boker()
        print("\n")
        sandnes.antall_utlaant()
        input("Trykk Enter på tastaturet for å gå tilbake til meny")

    elif kommando == "5":
        with open("Ovinger/Oving_9/bok.txt", "w", encoding="utf-8") as filen:
            for bok in sandnes.booker:
                linje = bok.bok.tittel + ".    Antall tilgjengelige: " + str(bok.antall_naa) + "\n"
                filen.write(linje)

    elif kommando == "6":
        with open("Ovinger/Oving_9/bok.txt", "r", encoding="utf-8") as filen:
                for line in filen:
                    print(line)

    elif kommando == "7":
        sokeord = input("Skriv inn søkeord, adskilt med mellomrom: ")
        sokeord_sma = sokeord.lower()
        sokeord_liste = sokeord_sma.split(" ")
        soke_suksee = False
        for bok in sandnes.booker: # Går gjennom alle bøkene
            bok_funnet = True      # Starter med funnet
            tittel_sma = bok.bok.tittel.lower()
            for ord in sokeord_liste:   # Går gjennom ordene
                if ord not in tittel_sma:
                    bok_funnet = False            # Setter til feil bok om ett av ordene ikke passer (fra oppgaven)
            if bok_funnet == True: # Sier ifra om vi gjør en match
                print(f"Funnet bok med match på alle søkeord: {bok.bok.tittel}")
                soke_suksee = True
        if not soke_suksee:
            print("Ingen bøker funnet med de søkeordene")

        print("\n")
        input("Trykk Enter på tastaturet for å gå tilbake til meny")

    elif kommando == "8":
        avslutt = True
    print("*************************************************************************")