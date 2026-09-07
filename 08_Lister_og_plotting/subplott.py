import matplotlib.pyplot as plt

tidspunkter = [1, 2, 3, 4, 5]
verdier = [2, 4, 5, 4, 3]
verdier_2 = [1, 3, 2, 3, 5]
verdier_3 = [7, 5, 4, 3, 3]

# marker, default ingen, verdier: hva som helst
# linestyle default solid, verdier: dashed, dotted, none
plt.subplot(2, 2, 1)
plt.plot(tidspunkter, verdier, marker="+", linestyle="dashed", label = "verdier")
plt.title("Eksempel 1")
plt.subplot(2, 2, 2)
plt.plot(tidspunkter, verdier_2, marker="+", linestyle="dashed", label = "verdier_2")
plt.title("Eksempel 2")
plt.subplot(2, 2, 3)
plt.plot(tidspunkter, verdier_3, marker="+", linestyle="dashed", label = "verdier_2")
plt.title("Eksempel 3")
plt.xlabel("Tispunkt i sekunder")
plt.ylabel("Absolutt aksellerasjon i m/(s*s)")
# plt.grid(True)
# plt.legend()
plt.show()