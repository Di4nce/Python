# Lage et program som konverterer mellom ulige måleenheter for avstand.

måleenheter = {"centimeter": 0.01, "tomme": 0.0254, "fot": 0.3048, "yard": 0.9144, "meter": 1,
                "kilometer": 1000, "miles (engelsk)": 1609, "nautisk mil": 1842, "mil (skandinavisk)": 10000}

print(måleenheter)

tall = float(input("Skriv inn tall du ønsker konvertert fra: "))    # kunne lage en try /expect her ved behov
konvert_fra = input("Skriv inn måleenhet du ønsker konverter fra: ")
konvert_til = input("Skriv inn måleenhet du ønsker konvertert til: ")

måleenhet_fra = måleenheter[konvert_fra]    # Slår opp i dictionary for å finne verdi
måleenhet_til = måleenheter[konvert_til]  

# print(måleenhet_fra)  # Til feilsøking
# print(måleenhet_til)  # Til feilsøking

nytt_tall = ((tall * måleenhet_fra) / måleenhet_til) # Tenkte feil, det skal være ganger (ikke dele) måleenhet_fra

print(f"Konvertering: {tall} {konvert_fra} blir {nytt_tall} {konvert_til}")