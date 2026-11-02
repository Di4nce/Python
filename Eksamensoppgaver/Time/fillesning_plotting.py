import matplotlib.pyplot as plt
import funksjoner_og_lister as f
import numpy as np

tider = list()
hastigheter = list()
with open("hastigheter.txt", encoding="UTF8") as fila:
    # Feil1 hopper ikke over linje1
    fila.readline()
    for linje in fila:
        komponenter = linje.split(";") # Feil 2 skiller ikke på ,

        # Deloppgae 2 hopper over feilformaterte linjer
        if len(komponenter) < 2:
            continue

        try:
            tid = int(komponenter[0])
            hastighet = float(komponenter[1].replace(",", "."))
            tider.append(tid)
            hastigheter.append(hastighet) # Feil 3 hastighet er et flyttall
        except ValueError:
            continue
print(tider)
print(hastigheter)

# Deloppgave 3
plt.subplot(2, 1, 1)
plt.plot(tider, hastigheter)
plt.subplot(2, 1, 1)
tider_np = np.array(tider)
hastigheter_np =np.array(hatigheer)
energi = f.kinetisk_energi(10, hastigheter_np)
plt.plot(tider_np, energi)
plt.show()