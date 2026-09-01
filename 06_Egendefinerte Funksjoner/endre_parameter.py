parameter = 9   # Forskjellig parameter enn parameteret som ligger inne i funksjonen. Litt uheldig navngivning

def testfunksjon(parameter):
    print(parameter)
    parameter += 5
    print(parameter)


testfunksjon(parameter)
print(parameter)