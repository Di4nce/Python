lagret_brukernavn = "Donald"
lagret_passord = "dolly_duck"

def login(brukernavn, passord):
    if (brukernavn == lagret_brukernavn) and (passord == lagret_passord):
        print("Du har logget inn korrekt")
    else:
        print("Feil i brukernavn eller passord?!?!")

input_bruker = input("Skriv inn brukernavnet ditt: ")
input_pass = input("Skriv inn passordet ditt: ")

login(input_bruker, input_pass)