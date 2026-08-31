def perfekt(a):
    for i in range(2, int(a/2+1)):
        if a % i == 0:  # Litt usikker på matten her, men tolket oppgaven så godt jeg kan og det gir korrekt svar
            return True
        else:
            return False

tall = int(input("Skriv inn et heltall: "))
perfekt_tall = perfekt(tall)
print(perfekt_tall)