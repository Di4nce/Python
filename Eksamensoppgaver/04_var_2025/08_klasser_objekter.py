# a) Skriv en klasse for rektangler. Skriv konstruktør for klassen. Et rektangel skal ha x- og y-
# koordinater for et startpunkt samt lengde og bredde. (4%)
 
# b) Skriv en metode "areal" for klassen rektangel som du lagde i forrige deloppgave. Metoden skal
# returnere arealet til rektanglet, som er lengden ganger bredden. (4%)
 
# c) Skriv en metode er_inni, som tar inn x- og y- koordinatene til et punkt. Metoden skal sjekke om
# punktet er inni rektanglet. Et punkt er inni et rektangel om både:
# x-koordinaten til punktet er større enn startpunktet sitt x-koordinat, men avstanden mellom
# de to x-koordinatene er lavere enn bredden til rektanglet.
# y-koordinaten til punktet er større enn startpunktet sitt y-koordinat, men avstanden mellom
# de to y-koordinatene er mindre enn høyden til rektanglet. (4%)
# Skriv ditt svar her

class Retangler:
    def __init__(self, x_koordinat, y_koordinat, lengde, bredde):
        self.x_koordinat = x_koordinat
        self.y_koordinat = y_koordinat
        self.lengde = lengde
        self.bredde = bredde
    def areal(self):
        areal = self.lengde * self.bredde
        return areal
    def er_inni(self, x_test, y_test):
        self.x_test = x_test
        self.y_test = y_test
        x_inni = False
        y_inni = False
        er_inni = False
        if x_test > self.x_koordinat and (x_test - self.x_koordinat) < self.bredde:
            x_inni = True
        if y_test > self.y_koordinat and (y_test - self.y_koordinat) < self.lengde: # Antar feil i oppgaven og lengde = høyde
            y_inni = True
        if y_inni and x_inni:
            er_inni = True
        return er_inni
