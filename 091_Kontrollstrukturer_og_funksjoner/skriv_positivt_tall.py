# Script for å regne vloul av et rom

def skriv_inn_positivt_tall(beskjed):
    mangler_verdi = True
    while mangler_verdi:
        try:
            positivt_tall = float(input(beskjed))
        except ValueError:
            print("Du må skrive inn et tall")
            continue
        if positivt_tall < 0.0:
            print("Tallet må være positivt")
        else:
            mangler_verdi = False
    return positivt_tall

# Hvs dette er scriptet som kjøres, utfør denne blokken
# Hvis dette scriptet bli importert fra et annet script, ikke ufør denne blokken
if __name__ == "__main__":  # For å hindre at denne delen blir importert inn i andre scripts
    lengde = skriv_inn_positivt_tall("Skriv inn lengde: ")
    bredde = skriv_inn_positivt_tall("Skriv inn bredde: ")
    hoyde = skriv_inn_positivt_tall("Skriv inn høyde: ")
    volum = round((lengde*bredde*hoyde), 2)
    print(f"Volumet på rommet er {volum}m3!!")