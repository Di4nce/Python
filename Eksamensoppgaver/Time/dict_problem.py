liste1 = ["Ullandhaugveien", "Møllebukta", "Gosen", "Ullandhaugveien", "Møllebukta",
"Ullandhaugveien"]
liste2 = [9550, 14231, 7023, 10342, 14965, 10056]

summer = dict()
antall = dict()
for i in range(len(liste1)):
    if liste1[i] not in summer:
        summer[liste1[i]] = 0
        antall[liste1[i]] = 0
    antall[liste1[i]] = antall[liste1[i]] + 1
    summer[liste1[i]] += liste2[i]

for nokkel in summer:
    gjennomsnitt = summer[nokkel] / antall[nokkel]
    print(f"Gjennomsnitt for målestasjon {nokkel} er {gjennomsnitt}")
    print(f"Mplestasjonen {nokkel} har {antall[nokkel]}, summen er {summer[nokkel]} og gjennomsnittet er {gjennomsnitt}")