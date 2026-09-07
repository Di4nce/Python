def perfekt(a):
    sum = 1 # Akkumulator, 1 skal vistnokk altid være med.
    for i in range(2, int(a/2+1)):
        if a % i == 0:  # Litt usikker på matten her, men tolket oppgaven så godt jeg kan og det gir korrekt svar
            sum += i
    return sum == a
        

tall = int(input("Skriv inn et heltall: "))
perfekt_tall = perfekt(tall)
print(perfekt_tall)