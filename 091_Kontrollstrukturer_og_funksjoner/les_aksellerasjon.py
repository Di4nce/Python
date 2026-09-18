from typing import Tuple

import matplotlib.pyplot as plt

def les_linje(linje: str) -> Tuple[float, float]:# Type hint string
    """ Docstring
    Leser en linje fra filen og trekker ut tidspunkt og total aksellerasjon
    fra filen.

    linje: linjen som skal leses
    return: tidspunkt og aksellersjon som flyttall
    """
    komponenter = linje.split(";") # Foreslår .split siden VSCode vet at det er en string
    tidspunkt = float(komponenter[0])
    aksellerasjon = float(komponenter[4])
    return tidspunkt, aksellerasjon

try:
    with open("kan kopiere relativ path fra filen og lime inn", "r", 
            encoding="UTF-8") as fila:
    # Kan klikke enter og dele inne i en parantes for å få plass til alt evt. kan \ brukes utenfor ()
        fila.readline()
        tidspunkter = list()
        aksellerasjoner = list()
        for linje in fila:
            tidspunkt, aksellerasjon = les_linje(linje)
            tidspunkter.append(tidspunkt)
            aksellerasjoner.append(aksellerasjon)
    print(tidspunkter)
    print(aksellerasjoner)


    # Tar inn to lister og lager en plot, x-retning og y-retning, må være like lange
    plt.plot(tidspunkter, aksellerasjoner, marker="*")  # Marker er frivillig for å lage en stjerne i hver verdi
    plt.title("Noe etellerannet")
    plt.grid(True)
    plt.show()

except FileNotFoundError as e:
    print("Finner ikke filen")
    print(e) # Printer hele feilmeldingen
    print("Tester filnavn: ", e.filename)
except IOError as e:
    print("En feil oppstod under lesning av fil")
    print(e)
else:
    print("I else-blokk, alt gikk fint.")
finally:
    print("Kjøres uansett om det blir en exception eller ikke") #Før with open fantes, lukket man filen her. Sikret at den ikke stod åpen hvis feil