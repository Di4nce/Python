def skriv_logg(melding, linje):
    logg = open("Ovinger/Oving_4/logg.txt", "a", encoding="UTF-8")  # Kunne brukt with open, da hadde jeg sluppet å lukke
    logg.write(f"{melding} i linje {linjenummer}. Innhold i linje: {linje}")
    logg.close()

def rapport_logg(melding, tall):
    logg = open("Ovinger/Oving_4/logg.txt", "a", encoding="UTF-8")
    logg.write(f"{melding} {tall}\n")
    logg.close()

def skriv_rapport(melding): # Tenkte feil, dette gjøres bare en gang og trenger ikke være en def
    logg = open("Ovinger/Oving_4/rapport.txt", "w", encoding="UTF-8")  # w for write istedet for a for append
    logg.write(melding)
    logg.close()

responstider = []   # Lager en tom liste
linjenummer = 0      # Counter til feilmedlingene
for_hoy_maaling = 0
ok_maaling = 0
rapport = ""    # Akkumulator
tom_linje = 0
feil_linje = 0

with open ("Ovinger/Oving_4/logg.txt", "w", encoding="UTF-8"):  # Sletter log før script begynner
    pass

try:    # Tester om gyldig fil og at skript virkerrapport_logg("Minimum", round(minimum, 2))
    with open("Ovinger/Oving_4/responstider_ms.txt", "r", encoding="UTF-8") as responstid:
        for linje in responstid:  
            if "cs" in linje:
                enhet = 10
                beskrivelse = "cs"
            elif "ds" in linje:
                enhet = 100
                beskrivelse = "ds"
            else:
                enhet = 1   # Standard enhet for ms, og antar om ikke noe står så bruker vi ms
                beskrivelse = "ms"
            linjenummer += 1
            linje_strip = linje.strip()
            if not linje_strip: # Skal hoppe over tomme linjer og linjer med bare \n
                skriv_logg("Kommentar", linje)
                tom_linje += 1
                continue
            elif linje_strip[0] == "#":
                skriv_logg("Tomt", linje)
                tom_linje +=1
                continue
            elif "," in linje_strip:
                linje_strip = linje_strip.replace(",", ".")
            #if "ms" not in linje_strip:
            #    skriv_logg("Feil eller manglende ms")
            #    feil_linje += 1
            try:
                # print(linje_strip, end="") #  Kunne brukt with open, da hadde jeg sluppet å lukkeend="" for å unngå at den stopper på tom linjeskift  # Bare brukt under testing av skript
                tid = float(linje_strip.replace(beskrivelse, "")) * enhet # Må gjøre om til float for å kunne regne på
                if tid > 20:
                    for_hoy_maaling += 1
                elif tid < 15:
                    ok_maaling += 1
                responstider.append(tid)
            except ValueError:
                skriv_logg("Feil", linje)
                feil_linje += 1
except FileNotFoundError:       # Hvis Try ikke virker og får error (som skrevet her)
    print("Klarer ikke skrive til filen")
except IOError:                 # Hvis Try ikke virker og får error (som skrevet her)
    print("Feil under formatering til fil")

print(responstider)

antall = len(responstider)
print("Antall gyldige målinger:", antall)
rapport += "Antall gyldige målinger: " + str(antall) + "\n" # Lage en def med to atributter her enklere?

if antall == 0:
    print("Ingen gyldige målinger")
    rapport += "Ingen gyldige målinger"
    skriv_rapport(rapport)
else:
    summen = sum(responstider)
    print("Sum responstider:", summen)
    rapport += "Sum responstider: " + str(summen) + "\n"

    minimum = min(responstider)
    print("Minste responstid:", minimum)
    rapport += "Minste responstid: " + str(minimum) + "\n"

    maksimum = max(responstider)
    print("Største responstid:", maksimum)
    rapport += "Største responstid: " + str(maksimum) + "\n"

    gjennomsnitt = summen / antall
    print("Gjennomsnittet var:", gjennomsnitt )
    rapport += "Gjennomsnittet var: " + str(gjennomsnitt) + "\n"

    print("For høye målinger:", for_hoy_maaling)
    rapport += "For høye målinger: " + str(for_hoy_maaling) + "\n"

    print("Ok målinger:", ok_maaling)
    rapport += "Ok målinger: " + str(ok_maaling) + "\n"

    # print(rapport)
    skriv_rapport(rapport)

    rapport_logg("Minimum:", round(minimum, 2))
    rapport_logg("Maksimum:", round(maksimum, 2))
    rapport_logg("Gjennomsnitt:", round(gjennomsnitt, 2))

rapport_logg("", "")    # Lager en mellomrom i loggen til rapporten
rapport_logg("Antall gyldige målinger:", antall)
rapport_logg("Ignorerte linjer:", tom_linje)
rapport_logg("Linjer med feil:", feil_linje)