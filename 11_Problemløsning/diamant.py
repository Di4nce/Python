











def skriv_linje(storrelse, linjenummer, nedstigende=False):
    for tegn in range(storrelse):
        if linjenummer == tegn:
            print("*", end="")
        elif (not(nedstigende) and linjenummer < tegn) or (nedstigende and linjenummer > tegn):
            print("-", end="")
        else:
            print(" ", end="")


storrelse = int(input("Skriv in størrelsen: "))
for linje in range(storrelse):
    skriv_linje(storrelse, storrelse-linje-1)
    skriv_linje(storrelse, linje-1, True)
    print()
for linje in range(1 , storrelse):
    skriv_linje(storrelse, linje)
    skriv_linje(storrelse, storrelse-linje-2, True)
    print()
