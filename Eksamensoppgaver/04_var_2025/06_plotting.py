# Skriv et Python-script som bruker matplotlib til å plotte verdien på en bankkonto for hvert år i 30 år.
# Kontoen starter med 100 000 kroner og har en rente på 5%. Poeng: 6%
 
# Formelen for pengebeløp etter t år gitt et startbeløp s er: f(t) = s*1.05**t
import matplotlib.pyplot as plt

aar = []
konto = []
s = 100000

for ar in range(2014, 2044): # Velger bare ett årsspenn i stedet for 1-30
    aar.append(ar)

for t in range(30):
    pengebelop = s*1.05**(t)    # Husk, første året skal ikke ha renter, fikset nå
    konto.append(pengebelop)

plt.plot(aar, konto, label="Pengebeløp")
plt.xlabel("Årstall")
plt.ylabel("Penger på Konto")
plt.show()