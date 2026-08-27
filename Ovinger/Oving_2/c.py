import random

hoyeste_tall = int(input("Hva er det høyeste tallet du vil gjette på? "))

mitt_Tall = random.randint(1, hoyeste_tall)
ditt_tall = 0
antall_forsok = 0
spill = True        # Legger inn en variabel som holder while løkken i gang, endrer denne til false når man vinner
# sist_gjettet = 0
gjettet = 0         # Kunne gjort enda mer komplekst og hoppet over første gang/ hvis gjetter = 0

print(f"Jeg har et tall mellom 1 og {hoyeste_tall}. Du ska gjette mitt tall på færrest mulig forsøk")
while spill:
    ditt_tall = int(input("Hva gjetter du? "))
    if ditt_tall < mitt_Tall:
        antall_forsok += 1      # Lagt in teller på feilet forsøk
        print("Ditt tall er mindre enn mitt tall.")
        if abs(mitt_Tall - gjettet) > abs(mitt_Tall - ditt_tall):
            print("Nærmere enn sist! ;-D")
        elif abs(mitt_Tall - gjettet) < abs(mitt_Tall - ditt_tall):
            print("Lenger unna enn sist :-O")
        else:
            print("Samme som sist :-)")
        gjettet = ditt_tall

    elif ditt_tall > mitt_Tall:
        antall_forsok += 1      # Lagt in teller på feilet forsøk
        print("Ditt tall er større enn mitt tall.")
        if abs(mitt_Tall - gjettet) > abs(mitt_Tall - ditt_tall):
            print("Nærmere enn sist! ;-D")
        elif abs(mitt_Tall - gjettet) < abs(mitt_Tall - ditt_tall):
            print("Lenger unna enn sist :-O")
        else:
            print("Samme som sist :-)")
        gjettet = ditt_tall
    else:
        antall_forsok += 1      # Flyttet teller til før svar slik at antall forsøk blir korrekt
        print(f"Gratulerer! Du gjettet riktig. Du brukte {antall_forsok} forsøk.")
        spill = False
