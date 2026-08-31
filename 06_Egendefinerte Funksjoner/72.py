a = "Hei"
b = " på deg"

def slå_sammen_tekst(a, b):
    sammen = a +b

print(sammen)   # Denne vil ikke virke siden sammen ikke er en global variabel, må lage en return fra funksjonen