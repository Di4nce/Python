for i in range(12, 0, -1):  # Oppgaven skal egentlig ha (12) og print(i+1)
    print(i)

fra = input("Tast inn fra valuta: ")
til = input("Tast inn til valuta: ")
kurs = float(input("Tast inn kurs: "))
antall = int(input("Tast inn antall konverteringer: "))

for i in range(antall):
    belop = float(input(f"Skriv inn beløpet i {fra}: "))
    ny_belop = round((belop * kurs), 2)
    print(f"Du har {ny_belop} i {til}!")