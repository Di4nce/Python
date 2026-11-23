# Gitt klassen Land fra løsningsforslaget til øving 9:

# class Land:
#     def __init__(self, navn, befolkning=None, areal=None):
#         self.navn = navn
#         self.befolkning = befolkning
#         self.areal = areal
        
#     # Oppgave b)
#     def __str__(self):
#        resultat = "Land: " + self.navn + " "
#        if self.befolkning is not None:
#             resultat += f"Befolkning: {self.befolkning} "
#         if self.areal is not None:
#             resultat += f"Areal: {self.areal} "
#         return resultat
    
#     # Oppgave c)
#     def befolkningstetthet(self):
#         if self.befolkning is None or self.areal is None:
#             return 0
#         return self.befolkning/self.areal  

# Deloppgaver
# 1. Legg til en egenskap "grunnlagt" som inneholder hvilket år landet ble grunnlagt. Denne
# egenskapen skal settes i konstruktøren og være en ny parameter til konstruktøren. Den
# skal ikke ha noen default verdi. (2%)
# 2. Legg til en metode som returnerer hvor mange år det er siden landet ble grunnlagt. Du kan
# finne nåværende år ved å importere datetime-pakken og bruke setningen
# "datetime.datetime.now().year". (3%)
# Skriv svaret ditt her. Endringer blir lagret automatisk.