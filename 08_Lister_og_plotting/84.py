kategorier = {
    "Barnefilm": ["Frozen", "Pingu", "Bukkene Bruse"],
    "Voksenfilm": ["Star Wars", "MacGyver"]
}

# a
print(kategorier["Voksenfilm"][1])

# b
kategorier["Barnefilm"].append("Donald Duck")
print(kategorier["Barnefilm"])

# c
lengde = len(kategorier["Voksenfilm"])
counter = 0
for i in range(lengde):
    print(kategorier["Voksenfilm"][counter])
    counter += 1