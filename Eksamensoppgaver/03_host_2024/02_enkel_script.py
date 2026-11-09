# Enkelt script
# a) Skriv et Python script som regner ut bremselengden til en bil. Brukeren skal oppgi hastigheten
# til bilen i kilometer pr. time. Scriptet skal skrive ut hvor mange meter det tar å bremse opp. Bruk
# formelen (X*X)/2  (X opphøyd i andre og deretter delt på to) hvor X er hastigheten/10. (6%)
# b) La brukeren i tillegg oppgi om det er tørr eller våt asfalt. Bremselengden i forrige oppgave
# gjelder tørr asfalt. Bremselengden er doblet på våt asfalt. (3%)

hastighet = float(input("Skriv inn hastigheten tl bilen i km pr time: "))
vaat = input("Er asfalten våt? Skriv J eller N her: ")
x = hastighet / 10
if vaat.lower() == "n":
    bremselengde = (x**2) / 2
    print(bremselengde)
elif vaat.lower() == "j":
    bremselengde = x**2
    print(bremselengde)
else:
    print("Du må skrive enten J eller N!")