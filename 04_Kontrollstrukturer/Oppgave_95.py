varer = {
    "Rema": {"fisk": 80, "epler": 25, "salat": 25},
    "Spar": {"fisk": 100, "epler": 20, "salat": 20},
    "Joker": {"fisk": 70, "epler": 35, "salat": 30}
}
summer = {}

# Finn billigste butikk når jeg kjøper en av hver.

for butikk in varer:
    sum = 0
    butikk_info = varer[butikk]
    # print(butikk)
    # print(butikk_info)
    for vare in butikk_info:
       # print(butikk_info[vare])
       sum += butikk_info[vare]
       summer[butikk] = sum
print(summer)
billigste = min(summer, key=summer.get)
laveste_pris = min(summer.values())
    
print(f"{billigste} er billigste butikk. Prisen for en av hver blir: {laveste_pris}")
