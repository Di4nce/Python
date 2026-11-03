# Lag et Python-script som regner ut arealet til en leilighet. For hvert rom skal brukeren skrive inn
# lengde og bredde til rommet. Arealet til et rom er lengde*bredde. Arealet til hele leiligheten er
# summen av arealene av alle rommene. Ulike leiligheter kan ha ulikt antall rom. Du kan velge en av
# to måter å angi antall rom på: (7%)
 
# 1: Brukeren oppgir antall rom før hen oppgir lengde og bredde til første rom.
# 2: Brukeren oppgir et negativt tall for lengde når brukeren er ferdig med å oppgi rom.

areal = 0
antall_rom = int(input("Skriv inn antall rom: "))

for i in range(antall_rom):
    romnummer = i + 1
    lengde = float(input(f"Skriv inn rom {romnummer} sitt lengde: "))
    bredde = float(input(f"Skriv inn rom {romnummer} sitt bredde: "))
    areal += (lengde*bredde)

print(areal) # Trengs strengt tatt ikke som en del av oppgaven.