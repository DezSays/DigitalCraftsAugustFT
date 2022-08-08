# Object Oriented Programming

# Define a class, class names are typically uppercase. 
class Pokemon:
    # A constructor is needed to define the bare minimum needed to create an object. See below
    def __init__(self, hp: int, name: str, type: tuple, weakness: tuple, damage: int, status: dict ):
        self.hp = hp 
        self.name= name 
        self.type = type 
        self.weakness = weakness
        self.damage = 0 
        self.status = {
            "Frozen": False,
            "Burned": False,
            "Poisoned": False,
            "Paralyzed": False,
        }
    
    def run(self):
        print('You ran away. Chicken.')
        
    def useItem(self, item):
        print('You used the %s.' % item)
        

        
        
pikachu = Pokemon(40, 'Pikachu', 'electric', 'ground', 0, False)
print(pikachu.hp) # If you wanted to print pikachus hp, use the dot operator as shown here.
# What if I wanted to update the hp? See below
pikachu.hp = 88
print(pikachu.hp)

squirtle = Pokemon(50, 'Squirtle', 'water', 'grass', 0, False)
print(squirtle.type)

squirtle.run()
pikachu.run()
pikachu.useItem('potion')

blaziken = Pokemon(120, 'Blaziken', ('fire', 'fighting'), ('water', 'psychic'), 0, False)
print(blaziken.type[1]) # this will print out the type in the index position 1, which in this case is fighting.

# What if I want a class special for my pikachu? This makes sense, since not all pokemon have the same effects as Pikachu. On line 39, you will see we are creating a new class and passing in Pokemon. This gives Pikachu access to everything in the Pokemon class, as well as what we define in the Pikachu class. See below:

class Pikachu(Pokemon): 
    def thunderbolt(self, name):
        print('%s used thunderbolt!' % name)
        damage = 50
        
    def quickAttack(self):
        print('%s used quick attack!' % self.name)
        damage = 30
        
    def thunderWave(self):
        damage = 0
        
        
raichu = Pikachu(100, 'Raichu', ('electric'), ('ground'), 0, False)

raichu.thunderbolt(raichu.name)

doug = Pikachu(100, 'Doug', ('electric'), ('ground'), 0, False)
doug.quickAttack()