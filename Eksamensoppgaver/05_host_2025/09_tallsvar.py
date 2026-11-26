# Gitt klassen Punkt oppgitt under, hva blir skrevet ut av følgende Python script? Skriv inn bare
# koordinatene som tall. 2% for hvert korrekte tall. 

# punkt1 = Punkt(9, 2)
# punkt2 = Punkt(5, 10)
# punkt1.y_koordinat = 4
# print(punkt1) 
# Hva blir skrevet ut av siste linje her?  ( 9 , 4  )

# punkt1 = Punkt(9, 2)
# punkt2 = Punkt(5, 10)
# punkt3 = punkt1
# flytt_til_midten(punkt1, punkt2)
# print(punkt3)
# Hva blir skrevet ut av siste linje her?  ( 7.0 , 6.0  )

# Gitt følgende script:
# variabel = set([2, 4, 2, 3])
# print(sum(variabel))
# Hva blir skrevet ut her? 9 (2+4+3)

# class Punkt:    
#     # Konstruktør (engelsk Constructor)
#     def __init__(self, x_koordinat_start=0, y_koordinat_start=0):
#         self.x_koordinat = x_koordinat_start
#         self.y_koordinat = y_koordinat_start

#     # Sjekker avstanden fra punktet til origo (koordinatet 0,0)
#     def avstand_origo(self):
#         return math.sqrt(self.x_koordinat**2 + self.y_koordinat**2)

#     # Flytter et punkt fra nåværende posisjon en oppgitt    
#     # distanse i x-retning og y-retning
#     def flytt(self, delta_x, delta_y):
#         self.x_koordinat += delta_x
#         self.y_koordinat += delta_y

#     # Definerer hvorden et punkt skal skrives ut eller
#     # konverteres til en streng.
#     def __str__(self):
#         return f"({self.x_koordinat}, {self.y_koordinat})" 
    
#     def flytt_til_midten(punkt1: Punkt, punkt2: Punkt):
#         midt_x = (punkt1.x_koordinat + punkt2.x_koordinat)/2
#         midt_y = (punkt1.y_koordinat + punkt2.y_koordinat)/2
#         punkt1.x_koordinat = midt_x
#         punkt2.x_koordinat = midt_x
#         punkt1.y_koordinat = midt_y
#         punkt2.y_koordinat = midt_y 
        
# Maks poeng: 10