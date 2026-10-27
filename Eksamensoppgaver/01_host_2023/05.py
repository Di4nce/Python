# Deloppgave 1:
# Gitt følgende oppgavetekst for en funksjon:
 
# Lag en funksjon som lar brukeren skrive inn et heltall som er større enn eller lik 0. Hvis brukeren
# ikke skriver inn et lovlig heltall skal brukeren få beskjed om det og få prøve på nytt. Du trenger
# bare å teste for om tallet er under 0, du trenger ikke å teste for om det brukeren skriver inn ikke er
# et tall.
 
# Her er det oppgitt fire alternative svar på denne oppgaven. Tre av dem er korrekte, det siste er feil.
# Vis hvilket svar som er feil i valgboksen under.
 
# # Alternativ 1
# def les_positivt_heltall1(beskjed):
#     tall = int(input(beskjed))
#     while tall < 0:
#         print("Du må skrive inn et ikke-negativt heltall!")
#         tall = int(input(beskjed))
#     return tall
 
# # Alternativ 2
# def les_positivt_heltall1(beskjed):
#     tall = int(input(beskjed))
#     while tall < 0:
#         print("Du må skrive inn et ikke-negativt heltall!")
#     tall = int(input(beskjed))
#     return tall
 
# # Alternativ 3
# def les_positivt_heltall1(beskjed):
#     streng = input(beskjed)
#     tall = int(streng)
#     while tall < 0:
#         print("Du må skrive inn et ikke-negativt heltall!")
#         streng = input(beskjed)
#         tall = int(streng)
#     return tall
 
# # Alternativ 4
# def les_positivt_heltall1(beskjed):
#     fortsetter = True
#     while fortsetter:
#         tall = int(input(beskjed))
#         if tall < 0:
#             print("Du må skrive inn et ikke-negativt heltall!")
#         else:
#             fortsetter = False
#     return tall

# Velg hvilken av løsningene som ikke er korrekt:

# Alternativ 3 [ ]
# Alternativ 4 [ ]
# Alternativ 1 [ ]
# Alternativ 2 [x]
 

# Deloppgave 2:
 
# Gitt samme oppgave som i del 1 bortsett fra at den også må håndtere at brukeren skriver inn noe
# som ikke er et tall. Her er fire alternative løsninger. Tre av dem er feil, et av dem er korrekt. Velg
# hvilket av alternativene som er korrekt i valgboksen under.
 
# # Alternativ 1
# def les_positivt_heltall_med_eh(beskjed):
#     fortsetter = True
#     while fortsetter:
#         try:
#             tall = int(input(beskjed))
#             fortsetter = False
#         except ValueError:
#             print("Du må skrive inn et heltall!")
#             continue
#         if tall < 0:
#             print("Du må skrive inn et ikke-negativt heltall!")
#     return tall
 
# # Alternativ 2
# def les_positivt_heltall_med_eh(beskjed):
#     fortsetter = True
#     while fortsetter:
#         try:
#             tall = int(input(beskjed))
#         except ValueError:
#             print("Du må skrive inn et heltall!")
#             continue
#     if tall < 0:
#         print("Du må skrive inn et ikke-negativt heltall!")
#     else:
#         fortsetter = False
#     return tall

#  # Alternativ 3
#  def les_positivt_heltall_med_eh(beskjed):
#     fortsetter = True
#     while fortsetter:
#         try:
#             tall = int(input(beskjed))
#         except ValueError:
#             print("Du må skrive inn et heltall!")
#             continue
#         if tall < 0:
#             print("Du må skrive inn et ikke-negativt heltall!")
#             fortsetter = False
#     return tall
 
# # Alternativ 4
# def les_positivt_heltall_med_eh(beskjed):
#     fortsetter = True
#     while fortsetter:
#         try:
#             tall = int(input(beskjed))
#         except ValueError:
#             print("Du må skrive inn et heltall!")
#             continue
#         if tall < 0:
#             print("Du må skrive inn et ikke-negativt heltall!")
#         else:
#             fortsetter = False
#     return tall
# Velg hvilken av de fire løsningene som er korrekt
 
# Poeng: 5% per korrekt svar, 0% for feil eller manglende svar.
# Alternativ 3 [ ]
# Alternativ 2 [ ]
# Alternativ 1 [ ]
# Alternativ 4 [x]
