# a) Skriv et Python program som implementerer følgende spill: (10%)
# Programmet skal lage et tilfeldig heltall mellom 1 og 100
# For hver runde skal spilleren (brukeren) gjette hvilket tall programmet har lagd. Spillet er
# ferdig om brukeren gjetter riktig. Hvis brukeren ikke gjetter riktig skal programmet skrive ut
# om brukeren sitt gjett er for lavt eller for høyt.
# Når spillet er ferdig skal programmet skrive ut antall runder spilleren brukte på å gjette riktig.
# Målet er å gjette riktig med færrest mulig runder.
 
# b) Utvid spillet med følgende tilleggsfunksjon. I alle runder etter første runde skal spillet skrive ut
# som spilleren gjettet nærmere eller lengre unna tallet programmet har lagd enn forrige runde. (4%)
 
# c) Håndter det at brukeren skriver inn verdier som ikke er heltall eller som er utenfor tillatt område.
# Tillatt område er mellom 1 og 100. Dette skal håndteres ved å skrive en feilmelding og så skal
# brukeren få prøve på nytt uten at dette teller som et forsøk på å gjette tallet. (4%)
 
# Skriv ditt svar her
import random as r

hemmeli = r.randint(1, 100)
spill_i_gang = True
runder = 0
langt_unna = None

def langt_unna_test(hemmeli, gjett, langt_unna):
    if langt_unna is None:
        pass
    elif abs(hemmeli - gjett) > langt_unna:
        print("Du er lenger unna enn sist")
    elif abs(hemmeli - gjett) < langt_unna:
        print("Du er nærmere enn sist")
    else:
        print("Du er like nærme som sist")

while spill_i_gang:
    try:
        gjett = int(input("Gjett et tall mellom og inkludert 1 og 100: "))
    except ValueError:
        print("Du må skrive inn et heltall")
        continue
    if gjett > 100 or gjett < 1:
        print("Du må skrive inn et tall mellom 1 og 100")
        continue
    runder += 1
    if gjett < hemmeli:
        print("Du har gjettet for lav")
        langt_unna_test(hemmeli, gjett, langt_unna)
    elif gjett > hemmeli:
        print("Du har gjettet for høyt")
        langt_unna_test(hemmeli, gjett, langt_unna)
    else:
        print(f"Du har gjettet riktig med {runder} runder, tallet var {hemmeli}.")
        spill_i_gang = False
    langt_unna = abs(hemmeli - gjett)