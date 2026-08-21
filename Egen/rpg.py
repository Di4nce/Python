import random, sys

def d20():
    return random.randint(1,20)
def d8():
    return random.randint(1,8)
def d6():
    return random.randint(1,6)

# class entity:
  #  def __init__(self, name, to_hit, ac):
   #     self.name = name
    #    self.to_hit = to_hit
     #   self.ac = ac
        # self.hp = d8()

monster = "Goblin"
monster_to_hit = 1
monster_ac = 11
monster_hp = d8()

print("Welcome to to the RPG-game")
player_name = input("What is the name of your character? ")
print(f"Hello, {player_name}!")
to_hit = int(input("What is your to hit? (enter a number between 0 and 5) "))
ac = int(input("What is your AC? (enter a number between 10 and 20) "))
hp = d8()
print(f"You have created a character named {player_name}, with {ac} AC, +{to_hit} to hit and {hp} HP. Good luck!")
print("-----------------------------------------------------")
fight = input("Do you want to fight or run away? (Fight / Run) ")

if fight == "Run":
    print("You ran away to live and fight another day.")
    sys.exit()
else:
    print(f"You meet a {monster}")

# while hp > 0:

