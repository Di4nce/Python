# Gitt følgende program som lager ei liste:
 
# liste = list() 
# liste.append(1) 
# liste.append(1) 
# for i in range(2, 10): 
#       liste.append(liste[i-1] + liste[i-2])
 
# Fortsett dette programmet slik at det bruker matplotlib til å plotte verdiene i lista "liste". Den første
# verdien i lista skal plottes på x-koordinat 1, det neste på x-koordinat 2 og så videre fram til slutten
# av lista.

# egne notater for liste = [1, 1, 2, 3] | 2 = [1] + [0] = 1 + 1 = 2 | 3 = [2] + [1] = 2 + 1 = 3 | 4 =... trengs ikke

# import matplotlib.pyplot as plt   # står ikke i oppgaven, men må for å få kodne til å virke

# x_koordinat = list()
# for i in range(len(liste)):
#   x_koordinat.append(i+1)
#
# plt.plot(x_koordinat, liste)
# plt.show()