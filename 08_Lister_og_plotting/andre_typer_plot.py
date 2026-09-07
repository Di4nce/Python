import matplotlib.pyplot as plt

# Stolplediagram
tidspunkter = [1, 2, 3, 4, 5]
verdier = [2, 4, 5, 4, 3]
verdier_2 = [1, 3, 2, 3, 5]

plt.bar(tidspunkter, verdier)
plt.show()

plt.pie(verdier, labels=tidspunkter)
plt.show()
