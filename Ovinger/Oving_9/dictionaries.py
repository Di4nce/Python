# Lage et program som konverterer mellom ulige måleenheter for avstand.

måleenheter = {"centimeter": [0.01, "cm"], "tomme": [0.0254, "in"], "fot": [0.3048, "ft"], "yard": [0.9144, "yd"], "meter": [1, "m"],
                "kilometer": [1000, "km"], "miles (engelsk)": [1609, "mi"], "nautisk mil": [1842, "nm"], "mil (skandinavisk)": [10000, "mil"]}

print(måleenheter.keys())

def konvertering():
    tall = float(input("Skriv inn tall du ønsker konvertert fra: "))    
    # kunne laget try / expect loop med while her
    konvert_fra = input("Skriv inn måleenhet du ønsker konverter fra: ")
    konvert_til = input("Skriv inn måleenhet du ønsker konvertert til: ")

    måleenhet_fra = måleenheter[konvert_fra]    # Slår opp i dictionary for å finne verdi (liste)
    måleenhet_til = måleenheter[konvert_til]  

    # print(måleenhet_fra)  # Til feilsøking
    # print(måleenhet_til)  # Til feilsøking

    # Henter fra listen [0] er enhet i meter og [1] er kortform
    nytt_tall = ((tall * måleenhet_fra[0]) / måleenhet_til[0]) # Tenkte feil, det skal være ganger (ikke dele) måleenhet_fra

    print(f"Konvertering: {tall} {måleenhet_fra[1]} blir {nytt_tall} {måleenhet_til[1]}")

konvertering()