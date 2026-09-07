import matplotlib.pyplot as plt

tidspunkter = [1, 2, 3, 4, 5]
verdier = [2, 4, 5, 4, 3]
verdier_2 = [1, 3, 2, 3, 5]

# marker, default ingen, verdier: hva som helst
# linestyle default solid, verdier: dashed, dotted, none
plt.plot(tidspunkter, verdier, marker="+", linestyle="dashed", label = "verdier")
plt.plot(tidspunkter, verdier_2, marker="+", linestyle="dashed", label = "verdier_2")
plt.title("Aksellerasjon av mobiltelefon")
plt.xlabel("Tispunkt i sekunder")
plt.ylabel("Absolutt aksellerasjon i m/(s*s)")
# plt.grid(True)
plt.legend()
plt.show()