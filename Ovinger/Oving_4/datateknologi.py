responstider = []   # Lager en tom liste
linjenummer = 0      # Counter til feilmedlingene
with open ("Ovinger/Oving_4/logg.txt", "w", encoding="UTF-8"):  # Sletter log før script begynner
    pass

with open("Ovinger/Oving_4/responstider_ms.txt", "r", encoding="UTF-8") as responstid:
    for linje in responstid:
        linjenummer += 1
        linje_strip = linje.strip(" ")
        if linje_strip[0] == "#":
            continue
        elif linje_strip == "\n":
            continue
        elif "," in linje_strip:
            linje_strip = linje_strip.replace(",", ".")
        if " ms" not in linje_strip:
            logg = open("Ovinger/Oving_4/logg.txt", "a", encoding="UTF-8")  # Kunne brukt with open, da hadde jeg sluppet å lukke
            logg.write(f"Feil eller manglende ms i linje {linjenummer}\n")
            logg.close()
        else:
            print(linje_strip, end="") # end="" for å unngå at den stopper på tom linjeskift