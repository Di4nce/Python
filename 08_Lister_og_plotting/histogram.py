import matplotlib.pyplot as plt

# En liste mellom 2 og 20
verdier = [2, 20, 9, 6, 7, 5, 7, 4, 5, 6, 7, 8, 4, 3, 4, 11, 12, 14, 5, 6, 9, 8, 15]

plt.hist(verdier, 5, range=(2, 20)) # Antall søyler 5. range () er en touple, og tilsvarer to verdier. Touples kan ikke endres
plt.show()