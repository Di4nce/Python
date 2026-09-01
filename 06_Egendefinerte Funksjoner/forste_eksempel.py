# Script for å reagne ut volum av et rom

def skriv_inn_positivt_tall(beskjed):
    mangler_verdi = True
    while mangler_verdi:
        try:
            positivt_tall = float(input(beskjed))
        except ValueError:
            print("Du må skrive inn et tall")
            continue
        if positivt_tall < 0.0:
            print("Tallet må være positiv")
        else:
            mangler_verdi = False
    return positivt_tall

if __name__ == "__main__":  # For å hindre at denne delen blir importert inn i andre scripts
    lengde = skriv_inn_positivt_tall("Skriv inn lengde: ")
    bredde = skriv_inn_positivt_tall("Skriv inn bredde: ")
    hoyde = skriv_inn_positivt_tall("Skriv inn høyde: ")
    volum = round((lengde*bredde*hoyde), 2)
    print(f"Volumet på rommet er {volum}m3!!")
