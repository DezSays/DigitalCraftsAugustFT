# Object Oriented Programming

import random


# Define a class, class names are typically uppercase
class Pokemon:
    # Constructor: the defines the bare minimum to create an object
    def __init__(self, hp: int, name: str, type: tuple, weakness: tuple):
        self.hp = hp
        self.name = name
        self.type = type
        self.weakness = weakness
        self.damage = 0
        self.status = {
            "Frozen": False,
            "Burned": False,
            'Poisoned': False,
            'Paralyzed': False
        }

    
    def run(self):
        print('You fled the battle.')

    def useItem(self, item):
        print('You used the %s.' % item)


# Inheritance
# When a child class, takes on the properties of a parent class, we call that inheritance
# Since Pikachu 
class Pikachu(Pokemon):
    def __init__(self, hp: int, name: str, type: tuple, weakness: tuple):
        super().__init__(hp, name, type, weakness)
    def thunderbolt(self):
        print('%s used thunderbolt!' % self.name)
        damage = 50

    def quickAttack(self, name):
        print('%s used quick attack!' % name)
        damage = 30
    
    def thunderWave(self):
        damage = 0

    # Using setters to update a pokemon's hp
    def setHp(self, hp):
        if hp > 100:
            print('Error: Cannot heal pokemon by that amount')
        else:
            self.hp += hp
        

    def useItem(self, item):
        chance = random.random() * 100
        print("Chance: %f" % chance)
        if chance < 70:
            print(super().useItem('%s' % item))
        elif chance >= 70 and chance < 100:
            print('You used the %s.' % item)
            print("It's still Pikachu's turn.")


class Squirtle(Pokemon): 
    def surf(self):
        print('%s used surf!' % self.name)
        damage = 80

    def watergun(self):
        print('%s used watergun!' % self.name)
        damage = 40

    def bubble(self):
        print('%s used bubble!' % self.name)
        damage = 30

    def hydropump(self): 
        print('%s used hydro pump!' % self.name)
        damage = 120




class Bulbasaur(Pokemon):
    def vineWhip(self):
        print('%s used vine whip!' % self.name)
        damage = 45
        
    def razorLeaf(self):
        print('%s used razor leaf!' % self.name)
        damage = 55

    def synthesis(self):
        print('%s used synthesis!' % self.name)
        damage = 0

    def solarBeam(self):
        print('%s used solar beam!!!' % self.name)
        damage = 120



pikachu = Pokemon(40, 'Pikachu', 'electric', 'ground')
# You can access each field of the pokemon class using the dot operator
print(pikachu.hp)
pikachu.hp = 55
print(pikachu.hp)

squirtle = Pokemon(50, 'squirtle', 'water', 'grass')
print(squirtle.type)


squirtle.run()
pikachu.run()

pikachu.useItem('potion')

blaziken = Pokemon(120, 'Blaziken', ('fire', 'fighting'), ('water', 'psychic'))
print(blaziken.type)


# Notice that raichu can use thunderbolt and quick attack  and also has access to the parameters in the pokemon class
# raichu = Pikachu(100, 'Raichu', ('electric'), ('ground'))
# raichu.thunderbolt()

steven = Pikachu(100, 'Steven', ('electric'), ('ground'))
# steven.thunderbolt()


# shelly = Squirtle(50, 'Shelly', ('water'), ('grass', 'electric'))
# shelly.hydropump()

# ivy = Bulbasaur(50, 'Ivy', ('grass'), ('fire'))
# ivy.synthesis()

# steven.useItem('cure')
print(steven.hp)
steven.useItem('potion')

# Create a Cat/Dog game, create a class for both the cat and dog. Both animals should have the following properties:
#breed, weight, fur color, name
# Each animal will make their own unique sound
# Cat/Dog class which can do everything that both animals can do, but in its unique twist