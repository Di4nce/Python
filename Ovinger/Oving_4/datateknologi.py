def skriv(melding):
    logg = open("Ovinger/Oving_4/logg.txt", "a", encoding="UTF-8")  # Kunne brukt with open, da hadde jeg sluppet å lukke
    logg.write(f"{melding} i linje {linjenummer}\n")
    logg.close() 

responstider = []   # Lager en tom liste
linjenummer = 0      # Counter til feilmedlingene
for_hoy_maaling = 0
ok_maaling = 0

with open ("Ovinger/Oving_4/logg.txt", "w", encoding="UTF-8"):  # Sletter log før script begynner
    pass

try:    # Tester om gyldig fil og at skript virker
    with open("Ovinger/Oving_4/responstider_ms.txt", "r", encoding="UTF-8") as responstid:
        for linje in responstid:
            linjenummer += 1
            linje_strip = linje.strip(" ")
            if linje_strip[0] == "#":
                skriv("Kommentar")
                continue
            elif not linje_strip: # Skal hoppe over tomme linjer og linjer med bare \n
                skriv("Tomt")
                continue
            elif "," in linje_strip:
                linje_strip = linje_strip.replace(",", ".")
            if " ms" not in linje_strip:
                skriv("Feil eller manglende ms")
            else:
                # print(linje_strip, end="") # end="" for å unngå at den stopper på tom linjeskift  # Bare brukt under testing av skript
                tid = float(linje_strip.replace(" ms\n", "")) # For å unngå at den legger til linjeskift i listen, må også gjøre om til float for å kunne regne på
                if tid > 20:
                    for_hoy_maaling += 1
                elif tid < 15:
                    ok_maaling += 1
                responstider.append(tid)
except FileNotFoundError:       # Hvis Try ikke virker og får error (som skrevet her)
    print("Klarer ikke skrive til filen")
except IOError:                 # Hvis Try ikke virker og får error (som skrevet her)
    print("Feil under formatering til fil")

print(responstider)

antall = len(responstider)
print("Antall gyldige målinger:", antall)
sum = sum(responstider)
print("Sum responstider:", sum)
minimum = min(responstider)
print("Minste responstid:", minimum)
maksimum = max(responstider)
print("Største responstid:", maksimum)
gjennomsnitt = sum / antall
print("Gjennomsnittet var:", gjennomsnitt )
print("For høye målinger:", for_hoy_maaling)
print("Ok målinger:", ok_maaling)