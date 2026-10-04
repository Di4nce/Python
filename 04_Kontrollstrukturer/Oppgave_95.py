varer = {
    "Rema": {"fisk": 80, "epler": 30, "salat": 25},
    "Spar": {"fisk": 100, "epler": 20, "salat": 20},
    "Joker": {"fisk": 70, "epler": 35, "salat": 30}
}
rema_pris = 0
spar_pris = 0
joker_pris = 0

# Finn billigste butikk når jeg kjøper en av hver.

teller = 0
for butikk in varer:
    butikk_info = varer[butikk]
    butikk_navn = list(varer.keys())[teller]
    teller += 1
    print(butikk_navn)
    print(butikk_info)
        for vare in butikk_info:
            butikk_navn += butikk_info["fisk"]
