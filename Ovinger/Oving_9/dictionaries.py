# Lage et program som konverterer mellom ulige måleenheter for avstand.

maaleenheter = {"centimeter": [0.01, "cm"], "tomme": [0.0254, "in"], "fot": [0.3048, "ft"], "yard": [0.9144, "yd"], "meter": [1, "m"],
                "kilometer": [1000, "km"], "miles (engelsk)": [1609, "mi"], "nautisk mil": [1842, "nm"], "mil (skandinavisk)": [10000, "mil"]}

print(maaleenheter.keys())

def konvertering():
    tall = float(input("Skriv inn tall du ønsker konvertert fra: "))    
    # kunne laget try / expect loop med while her
    konvert_fra = input("Skriv inn måleenhet du ønsker konverter fra: ")
    konvert_til = input("Skriv inn måleenhet du ønsker konvertert til: ")

    maaleenhet_fra = maaleenheter[konvert_fra]    # Slår opp i dictionary for å finne verdi (liste)
    maaleenhet_til = maaleenheter[konvert_til]  

    # print(maaleenhet_fra)  # Til feilsøking
    # print(maaleenhet_til)  # Til feilsøking

    # Henter fra listen [0] er enhet i meter og [1] er kortform
    nytt_tall = ((tall * maaleenhet_fra[0]) / maaleenhet_til[0]) # Tenkte feil, det skal være ganger (ikke dele) maaleenhet_fra

    print(f"Konvertering: {tall} {maaleenhet_fra[1]} blir {nytt_tall} {maaleenhet_til[1]}")

if __name__ == "__main__":
    konvertering()