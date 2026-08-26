import math

rekkevidde_km_str = input("Rekkevidden til din elbil i kilometer: ")
tur_lengde_km_str = input("Lengden til kjøreturen din i kilometer: ")
rekkevidde_km = int(rekkevidde_km_str)
tur_lengde_km = int(tur_lengde_km_str)

lade_start = rekkevidde_km * 0.2
rekkevidde_80 = rekkevidde_km * 0.8
lade_km = rekkevidde_80 - lade_start
første_lading = rekkevidde_km - lade_start

# antall_ladinger = tur_lengde_km // rekkevidde_km   # Hvorfor // burde det ikke rundes opp med math.ceil?? 2.4 ladinger == 3 ladinger i praksis?

if rekkevidde_km < tur_lengde_km:
    if (første_lading + lade_km) > tur_lengde_km:
        print("Du trenger 1 lading for turen")
    else:
        rest_km = tur_lengde_km - (første_lading + lade_km)
        antall_ladinger = math.ceil((rest_km / lade_km)) + 1
        print(f"Du trenger {antall_ladinger} ladinger")
elif (rekkevidde_km*0.8) <= tur_lengde_km:              # Kunne vært omstrukturert, men beholt den her for å svare oppgave a
    print(f"Du trenger 1 lading for sikkerhetsskyld.")
else:
    print("Du trenger ikke lade")