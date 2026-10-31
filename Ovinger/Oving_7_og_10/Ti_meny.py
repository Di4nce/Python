import matplotlib.pyplot as plt
import Ti_b_anall_pr_aar as b
import Ti_e_skisesonger as e
import Ti_a_agregering as a
import Oppgave_d as d

# ------------------------ Meny ------------------------ #
fortsett = True
while fortsett:
    print("Oppgave ti, velg deloppgave: ")
    print("Tast 1 for a) Plotting og aggregering")
    print("Tast 2 for b) Antal sommerdager pr. år")
    print("Tast 3 for c) Temperatursammelikning")
    print("Tast 4 for d) Plotte statistikk")
    print("Tast 5 for e) Skisesonger")
    print("Tast annet for å avslutte")
    valg = input("Tast 1-5: ")

    if valg == "1":
        aarstall=input("Skriv inn årstall:")
        a.vis_statestikk(aarstall)
    elif valg == "2":
        fortsett_under = True
        while fortsett_under:
            print("*************************************")
            print("Sommerdager pr år, velg målestasjon: ")
            print("Tast 1 for Oslo")
            print("Tast 2 for Røros")
            print("Tast 3 for Tromsø")
            print("Tast 4 for Værnes")
            print("Tast 5 for Venabu")
            print("Tast annet for å gå til bake til hovedmeny")
            valg_2 = input("Tast 1-5: ")
            if valg_2 == "1":
                tider, maks, middel, nedbor, vind, snodybde = b.les_vaerdata("Nye CSV/oslo_blindern_1954_2025_med_makstemperatur.csv")
                # "Jukset" litt og måtte søke nettet for oppskriften for hvordan å opprette flere variabler på en gang
                b.antall_pr_aar(tider, maks, "Oslo")
            elif valg_2 == "2":
                tider, maks, middel, nedbor, vind, snodybde = b.les_vaerdata("Nye CSV/roeros_1954_2025_med_makstemperatur.csv")
                b.antall_pr_aar(tider, maks, "Røros")
            elif valg_2 == "3":
                tider, maks, middel, nedbor, vind, snodybde = b.les_vaerdata("Nye CSV/tromsoe_1954_2025_med_makstemperatur.csv")
                b.antall_pr_aar(tider, maks, "Tromsø")
            elif valg_2 == "4":
                tider, maks, middel, nedbor, vind, snodybde = b.les_vaerdata("Nye CSV/vaernes_1954_2025_med_makstemperatur.csv")
                b.antall_pr_aar(tider, maks, "Værnes")
            elif valg_2 == "5":
                tider, maks, middel, nedbor, vind, snodybde = b.les_vaerdata("Nye CSV/venabu_1954_2025_med_makstemperatur.csv")
                b.antall_pr_aar(tider, maks, "Venabu")
            else:
                fortsett_under = False
            print("*************************************")
    elif valg == "3":
        d.temperatursammenlikning()
    elif valg == "4":
        tider, maks, middel, nedbor, vind, snodybde=d.les_vaerdata("Nye CSV/oslo_blindern_1954_2025_med_makstemperatur.csv")
        d.vind_pr_maaned(tider, vind)
    elif valg == "5":
        e.plot_skisesonger("Nye CSV/oslo_blindern_1954_2025_med_makstemperatur.csv", "red", "Oslo")
        e.plot_skisesonger("Nye CSV/roeros_1954_2025_med_makstemperatur.csv", "blue", "Røros")
        e.plot_skisesonger("Nye CSV/tromsoe_1954_2025_med_makstemperatur.csv", "purple", "Tromsø")
        e.plot_skisesonger("Nye CSV/vaernes_1954_2025_med_makstemperatur.csv", "green", "Værnes")
        e.plot_skisesonger("Nye CSV/venabu_1954_2025_med_makstemperatur.csv", "orange", "Venabu")
        plt.title("Skidager pr. sesong")
        plt.legend(bbox_to_anchor=(1.02, 1), loc="upper left")
        plt.tight_layout()
        plt.grid(alpha=0.3)
        plt.xlabel("År")
        plt.ylabel("Dager med skiføre")
        plt.show()
    else:
        fortsett = False
    print("*************************************")
