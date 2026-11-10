# Kontekst:
# Gitt følgende spill:

# Hver spiller kaster tre terninger, og en spiller kan få poeng basert på verdien på de tre terningene
# på tre måter:
# 1. Spilleren får poeng lik den høyeste av terningene
# 2. Hvis spilleren har flere like terninger får spilleren poeng lik tallet på terningen ganget med
# antall like terninger
# 3. Hvis spilleren har flere terninger med tall rett etter hverandre får spilleren poeng lik summen
# av tallene på disse terningene
# Spilleren får den høyeste av poengsummene fra disse tre reglene. Eksempler:
# En spiller med terningkast 4-6-4 får 8 poeng (to terninger med verdien 4)
# En spiller med terningkast 6-2-2 får 6 poeng (termingen med verdi 6 gir en høyere score enn
# de to terningene med verdien 2)
# En spiller med terningkast 4-3-3 får 7 poeng (summen av de to terningene 3 og 4)

# Oppgaven:
# Skriv en funksjon som tar inn tre heltall. Hvert heltall er resultatet av ett treningkast. Funksjonen
# skal regne ut og returnere score for disse tre terningkastene.

# For full score på denne oppgaven skal funksjonen ta hensyn til at terningene ikke kommer inn i
# sortert rekkefølge og at rekkefølgen tallene står i i parameterlista ikke har noe å si, slik at hvis
# funksjonen blir kalt med parametrene 5, 2, 4 skal funksjonen returnere 9, summen av de to
# terningene 4 og 5.

# 12 poeng totalt. En løsning som antar at tallene kommer i sortert rekkefølge vil få maksimalt 9
# poeng.

# Skriv ditt svar her
def terningspill(terning1, terning2, terning3):
    hoyeste_tall = max(terning1, terning2, terning3)
    like_terninger = 0
    stigende = 0
    liste= [terning1, terning2, terning3]
    liste.sort() # Skal ikke legges i en variabel
    if terning1 == terning2 and terning2 == terning3:
        like_terninger = terning1 * 3
    elif terning1 == terning2 or terning1 == terning3:
        like_terninger = terning1 * 2
    elif terning2 == terning3:
        like_terninger = terning2 * 2
    if liste[0] == (liste[1] - 1) and liste[0] == (liste[2] - 2):
        stigende = liste[0] + liste[1] + liste[2]
    elif liste[0] == (liste[1] - 1):
        stigende = liste[0] + liste[1]
    elif liste[1] == (liste[2] - 1):
        stigende = liste[1] + liste[2]
    summen = max(hoyeste_tall, like_terninger, stigende)
    return summen