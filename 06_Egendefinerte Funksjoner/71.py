tall_1 = float(input("Tast inn tall 1: "))
tall_2 = float(input("Tast inn tall 2: "))
operator = input("Tast inn operator (+, -, * eller /): ")

def summer(a, b):
    c = a + b
    print(c)

def subtraher(a, b):
    c = a - b
    print(c)

def multipliser(a, b):
    c = a * b
    print(c)

def divider(a, b):
    c = a / b
    print(c)

if operator == "+":
    summer(tall_1, tall_2)
elif operator =="-":
    subtraher(tall_1, tall_2)
elif operator =="*":
    multipliser(tall_1, tall_2)
elif operator =="/":
    divider(tall_1, tall_2)
else:
   print("Du har valgt en ugyldig operator :-\\")