sum_mat = 0
sum_drikke = 0
sum_annet = 0
# pris = 0 # Denne variablen manglet, trengs ikke like vel, blir laget lenger ned

def skriv_inn_pris():
    mangler_verdi = True
    while mangler_verdi: # Laget en while løkke slik at om man taster feil så prøver man igjen
        try:
            pris = float(input("Pris: ")) # La til float her i stedet
        except ValueError:
            print("Feilformatert pris")
            continue # Tilbake til start istedet for å returne none
        # if pris == "":
        #    print("Tast inn et tall!") Dette trengs ikke lenger, eller så må den legges inn før try, og dele opp input
        return round(pris, 2) # Retunerte ikke en pris, la til en avrunding allerede her
        # try:
        #    pris = float(pris) # Dette tror jeg ikke trengs, ser ikke helt hensikten?

def skriv_inn_vartype(pris):
    global sum_mat      # global for å hente inn eksterne variabler og kunne endre disse i funksjonen.
    global sum_drikke
    global sum_annet
    type_vare = input("Mat (m) eller drikke (d) eller annet (a): ")
    if type_vare[0].lower() == "m":
        sum_mat += pris
        # return sum_mat Denne trengs ikke likevel når jeg endrer en global variabel
    elif type_vare[0].lower() == "d":
        sum_drikke += pris
        # return sum_drikke
    else:
        sum_annet += pris
        # return sum_annet

fortsetter = True
print("Skriv inn priser på varer og type vare. Avslutt med negativ pris")
while fortsetter:
    pris = skriv_inn_pris() # Lagrer return prisen i variablen for pris
    if pris < 0.0:
        fortsetter = False
        break
    skriv_inn_vartype(pris) # Pris tastet inn blir input til funksjonen
print("Sum mat: ", sum_mat)
print("Sum drikke: ", sum_drikke)
print("Sum annet: ", sum_annet)
