strengen = "En test av strenger og metoder"
en_annen_streng = "En annen streng"
testestreng = "     en streng med whitespace   \n"

store_bokstaver = strengen.upper
smaa_bokstaver = strengen.lower
print(store_bokstaver)
print(strengen)
print(en_annen_streng)
print(testestreng)
strippet = testestreng.strip()  # Fjerner whitespaces og newline foran og bak
print(strippet)

hvor = strengen.find("av")
print(hvor) # printer 8, posisjonen fra bokstaven a (telt fra null), gir -1 om den ikke finner strengen
print(strengen.isdigit())
tallstreng = 456
# print(tallstreng.isdigit())
tallstreng = 34.23
# print(tallstreng.isdigit())
tall_norsk = "345,23"
tall_engelsk = tall_norsk.replace(",", ".") # Erstatter "," med "."
print(tall_engelsk)
enkeltord = strengen.split(" ") # Gir ut en liste med ord splittet i " "
print(enkeltord)