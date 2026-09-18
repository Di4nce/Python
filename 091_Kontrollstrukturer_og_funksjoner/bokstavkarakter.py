# Eksempel for testing av script


def finn_bokstavkarakter(prosentscore):
    if prosentscore >= 90:
        return("A")
    elif prosentscore >= 80:
        return("B")
    elif prosentscore >= 60:
        return("C")
    elif prosentscore >= 50:
        return("D")
    elif prosentscore >= 40:
        return("E")
    else:
        return("F")

def test_finn_bokstavkarakter():
    # Test alle veier gjennom funksjonen
    karakter = finn_bokstavkarakter(90)
    if karakter != "A":
        print("Test feiler på A")
    karakter = finn_bokstavkarakter(80)
    if karakter != "B":
        print("Test feiler på B")
    karakter = finn_bokstavkarakter(60)
    if karakter != "C":
        print("Test feiler på C")
    karakter = finn_bokstavkarakter(50)
    if karakter != "D":
        print("Test feiler på D")
    karakter = finn_bokstavkarakter(40)
    if karakter != "E":
        print("Test feiler på E")
    karakter = finn_bokstavkarakter(10)
    if karakter != "F":
        print("Test feiler på F")

test_finn_bokstavkarakter()