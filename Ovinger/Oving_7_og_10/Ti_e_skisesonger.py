# Plott antall dager med skiføre for hver sesong det er nok data for. 
# Plott separate grafer i samme plott for alle aktuelle værstasjoner. Det er nok data 
# hvis det er data for minst halvparten av dagene i skisesongen
import Ti_b_anall_pr_aar as s
import matplotlib.pyplot as plt

# for aar in skidager_sortert:
#     print(len(skidager_sortert[aar]))
# # For å sjekke hvor mange dager som er i en normal skisesong = 212

# ------------------------- Script for skisesong --------------------------------- #
def plot_skisesonger(csv, farge="blue", sted="ukjent"):
    tider, maks, middel, nedbor, vind, snodybde = s.les_vaerdata(csv)
    tider.pop()     # Fjerner siste tomme linje
    snodybde.pop()  # Fjerner siste tomme linje
    antall_skidager = {}    # Lager en dictonary for å kunne legge skiseseongene inn som år.
    for tid in tider:   # Fyller opp dictionary med årene
        antall_skidager[int(tid[6:])] = [] # Legger inn alle årene som int
    laveste_aar = min(antall_skidager) # Finner laveste år i målingen
    antall_skidager[laveste_aar - 1] = [] # Må legge til en tidlgiere skisesong, siden skisesongene varer fra november til mai (neste år)
    teller = 0
    for tid in tider:
        if int(tid[3:5]) >= 11:     # Fra og med november legges på årets sesong
            if snodybde[teller] != "-":
                antall_skidager[int(tid[6:])].append(float(snodybde[teller].replace(",", ".")))
            teller += 1
        elif int(tid[3:5]) <= 5:    # til og med mai legges på fjorårets sesong
            if snodybde[teller] != "-":
                antall_skidager[int(tid[6:]) - 1].append(float(snodybde[teller].replace(",", "."))) 
                # Trekker fra en for å telle i fjorårets sesong
            teller += 1
        else:
            teller += 1
    skidager_sortert = dict(sorted(antall_skidager.items())) # Sorterer basert på år
    antall_skidager = {}    # Lager en ny dictionary for antall
    for ar in skidager_sortert:
        antall_skidager[ar] = []    # Legger til året som key i dictionary
        snodag = 0
        if len(skidager_sortert[ar]) > 212/2:    # Sjekker om det er nok data for minst halvparten
            for dybde in skidager_sortert[ar]:
                if dybde >= 20:
                    snodag += 1
            antall_skidager[ar] = snodag
        else:
            antall_skidager[ar] = None # Legger ikke til en verdi om det ikke er nok data
    plt.plot(antall_skidager.keys(), antall_skidager.values(), color=farge, label = sted, linewidth=1)


# ------------------------ Script for å kalle oppgaven --------------------------------- #
if __name__ == "__main__":  # Må ha denne slik at hovedscript ikke hentes inn om en skal importere funksjonen

    plot_skisesonger("Nye CSV/oslo_blindern_1954_2025_med_makstemperatur.csv", "red", "Oslo")
    plot_skisesonger("Nye CSV/roeros_1954_2025_med_makstemperatur.csv", "blue", "Røros")
    plot_skisesonger("Nye CSV/tromsoe_1954_2025_med_makstemperatur.csv", "purple", "Tromsø")
    plot_skisesonger("Nye CSV/vaernes_1954_2025_med_makstemperatur.csv", "green", "Værnes")
    plot_skisesonger("Nye CSV/venabu_1954_2025_med_makstemperatur.csv", "orange", "Venabu")
    plt.title("Skidager pr. sesong")
    plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left")
    plt.tight_layout()
    plt.grid(alpha=0.3)
    plt.xlabel("År")
    plt.ylabel("Dager med skiføre")
    plt.show()