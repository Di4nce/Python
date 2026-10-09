class Oppslag:
    def __init__(self, navn, telefonnummer, e_post):
        self.navn = navn
        self.telefonnummer = telefonnummer
        self.e_post = e_post
        telefonbok[self.navn] = [self.telefonnummer, self.e_post]

    def print_info(self):
        print(self.navn, self.telefonnummer, self.e_post)

telefonbok = {}

person1 = Oppslag("Fredrik", 12345678, "fred@ni.com")
person2 = Oppslag("Karen", 87654321, "ka@fa.no")
person3 = Oppslag("Kim", 11223344, "ki@ti.eu")

# person1.print_info()
for name in telefonbok:
    print(name, telefonbok[name])