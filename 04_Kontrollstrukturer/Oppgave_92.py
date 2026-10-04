boker = []

for i in range(4):
    ny_bok = input("Skriv inn en av dine favoritt filmer/bøker:")
    boker.append(ny_bok)
# print(boker)

boker.append("Harry Potter")
boker.append("Ringenes Herre")

index = 0
for bok in boker:
    if bok == "Harry Potter":
        print(boker)
        print(f"Harry Potter er på indeks: {index}")
        break
    index += 1