# Garden Simulator 
# Create the following classes to simulate a garden:
#     Tree - its shade decreases water loss by 2 
#     Gnome - each instance adds a 5% chance of rain 
#     Woodchuck - creates a 5% chance of a Tree disappearing 
#     Garden - has a separate lists for instancecs of Tree, Gnome, and Woodchuck

# Create a main while loop that runs your simulator. During each turn, your Garden may experience rain, or may have a Woodchuck move in. For each of its lists, tally up the various percents that an event will occur and use the built-in random module to decide what happens during that turn. 

# Every 10th turn, you have a random chance of earning another Tree or Gnome. 

# The simulation ends if you reach 10 Tree instances. 

# Bonus: Adding more classes 
# FruitTree (a subclass of Tree) - after its water_level reaches 100, it should increase its fruit attribute by 1

# Squirrel - each one adds a 5% chance that your fruit levels will decrease by 1. 

# The simulation ends if your FruitTree instances are able to produce 10 fruits. 


# Group one solution

# '''
# classes: Tree, Gnome, Woodchuck, Garden
# water gauge
# chance of rain
# chance of tree disappearing
# each turn: rain or woodchuck

# '''

# import random
# from unicodedata import name

# # Classes
# class Tree:
#     def __init__(self):
#         self.shade = -2

# class Woodchuck:
#     def __init__(self):
#         self.disappearingTreeChance = 5
  
# class Gnome: 
#     def __init__(self):
#         self.rainChance = 5
    
# class Garden:
#     def __init__(self):
#         self.trees = []
#         self.woodchucks = []
#         self.gnomes = []
#         self.waterLevel = 300
#         self.waterLoss = 20
#         self.rainChance = 20
#         self.woodchuckChance = 10
#         self.disappearingTreeChance = 0

# # Functions        
#     def addTree(self):
#         tree = Tree()
#         self.trees.append(tree)
        
#     def addGnome(self):
#         gnome = Gnome()
#         self.gnomes.append(gnome)
#         self.rainChance += gnome.rainChance
        
#     def addWoodchuck(self):
#         woody = Woodchuck()
#         self.woodchucks.append(woody)
#         self.disappearingTreeChance += woody.disappearingTreeChance

#     def rain(self):
#         self.waterLevel += 60


# # Simulation loop
# ourGarden = Garden()

# i = 1
# newTree = 0
# rainChance = ourGarden.rainChance
# while len(ourGarden.trees) < 10 and ourGarden.waterLevel > 0:
#     print('Round %d' % i)
#     print('Water Level: %d' % ourGarden.waterLevel)
#     print('Trees: %d' % len(ourGarden.trees))
#     print('Gnomes: %d' % len(ourGarden.gnomes))
#     print('Woodchucks: %d' % len(ourGarden.woodchucks))
    
#     chance = random.random() * 100
#     if chance < rainChance:
#         ourGarden.rain()
#         newTree += 1
#         print('It rained! Water levels increased.')

#     if newTree % 3 == 0 and newTree > 0:
#         ourGarden.addTree()
#         print('A new tree has blossomed!')

#     chance = random.random() * 100
#     if chance < ourGarden.woodchuckChance:
#         ourGarden.addWoodchuck()
#         print('A pesky woodchuck has entered the garden!')

#     if i % 10 == 0:
#         chance = random.random() * 100
#         if chance > 50:
#             ourGarden.addTree()
#             print('A tree was added to the garden')
#         else:
#             ourGarden.addGnome()
#             print('The garden has been blessed with a new gnome!')

#     chance = random.random() * 100
#     if chance < ourGarden.disappearingTreeChance and len(ourGarden.trees) > 0:
#         del ourGarden.trees[0]
#         print('The woodchucks destroyed a tree!')
#     decrease = ourGarden.waterLoss - (len(ourGarden.trees) * 2)
#     ourGarden.waterLevel -= decrease


#     input('Enter any character to continue: ')
#     i += 1



# # Win and lose conditions
# if len(ourGarden.trees) >= 10:
#     print('You have won!')
# elif ourGarden.waterLevel <= 0:
#     print('You have lost!')










# Group 2 solution

# import random

# def intput(phrase: str) -> int:
#     num = input(phrase)                     #gets input/num
#     if str.isdigit(num) == True:            #checks if num is a num
#         return int(num)
#     while str.isdigit(num) == False:
#         if str.isdigit(num[1:]) == True:    #checks if num is neg.
#             return int(num) 
#         else:                               #cycle again
#             num = input("Try again. ")
#             continue
#     return int(num)

# class Garden:
#     def __init__(self, tree: int, gnome: int, woodchuck: int):
#         self.tree = tree
#         self.gnome = gnome
#         self.woodchuck = woodchuck
#         self.isRaining = False
#         self.waterlevel = 0
#         self.waterloss = 10
#         self.waterlossConstant = 10

#     def waterLoss(self):  # its shade decreases water loss by 2
#         self.waterloss = 10

#         if self.waterlevel - self.waterloss - (self.tree * 2) <= 0:
#             self.waterlevel = 0
#             # print("Water level has increased by %s! " % abs(self.waterloss)) #added increased by abs value
#         else:
#             self.waterloss = self.waterloss - (self.tree * 2)
#             if self.waterloss < 0:
#                 self.waterlevel = self.waterlevel - self.waterloss
#                 print("Water level has decreased by %s! " % self.waterloss)

#     def waterGain(self):
#         self.waterlevel = self.waterlevel + 25

#     def rainChance(self): # each instance adds a 5% chance of rain
#         numGnome = self.gnome
#         randomNum = random.random() * 100
#         randomNum = int(randomNum)
#         #print('The chance for rain is ' + str(int(randomNum)) + '%')
#         if numGnome * 5 >= randomNum:
#             print("It started to raining! ")
#             self.isRaining = True
#         else:
#             print("Guess there's no rain today.")

#     def treeLoss(self): # each woodchuck adds a 5% chance of lossing a tree
#         numWoodchuck = self.woodchuck
#         randomNum = random.random() * 100
#         randomNum = int(randomNum)
#         # print('The chance for losing a tree is ' + str(int(randomNum)) + '%')
#         if numWoodchuck * 5 >= randomNum:
#             print('A woodchuck destroyed a tree!')
#             self.tree = self.tree - 1

#     def treeGain(self):
#         if self.waterlevel >= 100:
#             self.tree = self.tree + 1 # changed self.tree to numTree -Khanh
#             print("A tree has risen from the ground. ")
#             self.waterlevel = 0

#     def woodchuckGuest(self):
#         randomNum = random.random() * 100
#         randomNum = int(randomNum)
#         if 5 >= randomNum:
#             self.woodchuck += 1 
#             print('A woodchuck has moved into your neighborhood!')
            
#     def moreRain(self):
#         randomNum = random.random() * 100
#         randomNum = int(randomNum)
#         if 5 >= randomNum:
#             isRaining = True
#             self.waterGain()
#             print('Its a miracle! It has started to rain!')

# # Run the game
# #-----------------------------------------------------------
# treeNum = intput("Enter the amount of trees. ")
# gnomeNum = intput("Enter the amount of gnomes. ")
# woodchuckNum = intput("Enter the amount of woodchucks. ")
# DcGarden = Garden(treeNum,gnomeNum,woodchuckNum)

# #DcGarden = Garden(4,5,2)

# turn = 1
# while DcGarden.tree < 11:
#     DcGarden.isRaining = False
#     print('Turn: #%d ' % turn)
#     DcGarden.rainChance()
#     if DcGarden.isRaining == True:
#         DcGarden.waterGain()
#         print("ran water gain. ")
#     else:
#         DcGarden.waterLoss()
#     DcGarden.treeGain()
#     DcGarden.treeLoss()
#     DcGarden.woodchuckGuest()
#     DcGarden.moreRain()
#     #print("")
#     print("Water level:",DcGarden.waterlevel)
#     print('We have ' + str(int(DcGarden.tree)) + ' trees.')

#     if DcGarden.tree == 10:
#         print("You Won! ")
#         break
#     elif DcGarden.tree == 0:  #or DcGarden.waterlevel < 0:
#         print("You Lost! ")
#         break
#     if turn % 10 == 0:
#         randNum = random.randint(0,9)
#         if randNum >= 5:
#             print("You have gained a FREE tree! ")
#             DcGarden.tree += 1
#         elif randNum < 5:
#             print("You have gained a FREE gnome! ")
#             DcGarden.gnome += 1
#     print("")
    
#     turn += 1











# Group 3 solution

# import random
# #Create the environment
# #-----------------------------------------------------------

# class Garden:
#     def __init__(self, tree: int, gnome: int, woodchuck: int):
#         self.tree = tree
#         self.gnome = gnome
#         self.woodchuck = woodchuck
#         self.isRaining = False
#         self.waterlevel = 0
#         self.waterloss = 10

#     def waterLoss(self):  # its shade decreases water loss by 2
#         self.waterloss = 10

#         if self.waterlevel - (self.waterloss - (self.tree * 2)) <= 0:
#             self.waterlevel = 0
#         else:
#             self.waterloss = self.waterloss - (self.tree * 2)
#             if self.waterloss > 0:
#                 self.waterlevel = self.waterlevel - self.waterloss
#                 print("Water level has decreased by %s! " % self.waterloss)

#     def waterGain(self):
#         self.waterlevel = self.waterlevel + 40

#     def rainChance(self): # each instance adds a 5% chance of rain
#         numGnome = self.gnome
#         randomNum = random.random() * 100
#         randomNum = int(randomNum)
#         #print('The chance for rain is ' + str(int(randomNum)) + '%')
#         if numGnome * 5 >= randomNum:
#             print("It started to raining! ")
#             self.isRaining = True
#         else:
#             print("Guess there's no rain today.")

#     def treeLoss(self): # each woodchuck adds a 5% chance of lossing a tree
#         numWoodchuck = self.woodchuck
#         randomNum = random.random() * 100
#         randomNum = int(randomNum)
#         # print('The chance for losing a tree is ' + str(int(randomNum)) + '%')
#         if numWoodchuck * 5 >= randomNum:
#             print('A woodchuck destroyed a tree!')
#             self.tree = self.tree - 1

#     def treeGain(self):
#         if self.waterlevel >= 100:
#             self.tree = self.tree + 1 # changed self.tree to numTree -Khanh
#             print("A tree has risen from the ground. ")
#             self.waterlevel = 0

#     def woodchuckGuest(self):
#         randomNum = random.random() * 100
#         randomNum = int(randomNum)
#         if 5 >= randomNum:
#             self.woodchuck += 1 
#             print('A woodchuck has moved into your neighborhood!')
            
#     def moreRain(self):
#         randomNum = random.random() * 100
#         randomNum = int(randomNum)
#         if 5 >= randomNum:
#             isRaining = True
#             self.waterGain()
#             print('Its a miracle! It has started to rain!')

# # Run the game
# #-----------------------------------------------------------
# # treeNum = useful.intput("Enter the amount of trees. ")
# # gnomeNum = useful.intput("Enter the amount of gnomes. ")
# # woodchuckNum = useful.intput("Enter the amount of woodchucks.\n ")
# # DcGarden = Garden(treeNum,gnomeNum,woodchuckNum)

# DcGarden = Garden(4,3,1)

# turn = 1
# while DcGarden.tree < 11:
#     DcGarden.isRaining = False
#     print('Turn: #%d ' % turn)
#     DcGarden.rainChance()
#     if DcGarden.isRaining == True:
#         DcGarden.waterGain()
#         print("The water level has risen. ")
#     else:
#         DcGarden.waterLoss()
#     DcGarden.treeGain()
#     DcGarden.treeLoss()
#     DcGarden.woodchuckGuest()
#     DcGarden.moreRain()
#     #print("")
#     print("Water level:",DcGarden.waterlevel)
#     print('We have ' + str(int(DcGarden.tree)) + ' trees.')

#     if DcGarden.tree == 10:
#         print("The Gods rejoice your victory! ")
#         break
#     elif DcGarden.tree == 0:  #or DcGarden.waterlevel < 0:
#         print("The Gods laugh at your defeat! ")
#         break
#     if turn % 10 == 0:
#         randNum = random.randint(0,9)
#         if randNum >= 5:
#             print("The Goddess of the Forest has blessed you with a tree! ")
#             DcGarden.tree += 1
#         elif randNum < 5:
#             print("The God of Storms has bestowed you a gnome! ")
#             DcGarden.gnome += 1
#     print("")
#     #input("")
    
#     turn += 1










# Group 4 solution

# import random
# from types import MethodType

# class Garden:
#     def __init__(self, turn):
#         self.turn = turn

#     treeList = []
#     gnomeList = []
#     woodChuckList = []

# class Tree:
#     def __init__(self, waterLevel):
#         self.waterLevel = waterLevel

# class WoodChuck:
#     def __init__(self,name,chopPercent):
#         self.name = name
#         self.chopPercent = chopPercent

# class Gnome: 
#     def __init__(self, name, gnomeRainPercent):
#         self.name = name
#         self.gnomeRainPercent = gnomeRainPercent

# #   ****Garden object instantiated********
# myGardenObj = Garden(0)

# #   ****Gnome object instantiated******** 
# theGnome = Gnome("Steven", 0)

# #  ****WoodChuck object instantiated******** 
# theWoodChuck = WoodChuck("Chuck",0)

# #****Tree object instantiated******** 
# theTree = Tree(0)

# def fiftyFiftyChance(methodOne: MethodType,MethodTwo: MethodType):
#     randomNumber = random.randint(0,1)
#     if(randomNumber == 0 ):
#         methodOne
#     else:
#         MethodTwo
#         print("you did not win the FiftyFifty")

# def chanceOfShade():
#     print()
    
# def treeCreator():
#     myGardenObj.treeList.append(theTree)

# def gnomeCreator():
#     myGardenObj.gnomeList.append(theGnome)


# def chanceOfTreeLoss():
#     randomNumber = random.randint(1, 100)
#     for chuck in myGardenObj.woodChuckList:
#         theWoodChuck.chopPercent += 5

#     print(f"this is the newChuck percent{theWoodChuck.chopPercent}")
#     if(theWoodChuck.chopPercent <= randomNumber):
#         myGardenObj.treeList.remove
#         theWoodChuck.chopPercent = 0 
#         print(f"this was removed {myGardenObj.treeList.remove}")
#     if(theTree.waterLevel <=0):
#         myGardenObj.treeList.remove
#         print(f"this was removed {myGardenObj.treeList.remove}")

# def woodChuckCreator():
#     myGardenObj.woodChuckList.append(theWoodChuck)
# def woodChuckTreeChop():
#     if(theWoodChuck.chopPercent>= 100):
#         myGardenObj.treeList.remove
#         theWoodChuck.chopPercent = 0 


# # removes water per turn but not too much
# def waterRemover():
#     theTree.waterLevel -= 5
#     if(theTree.waterLevel < 0):
#         theTree.waterLevel = 0

# # adds water but not too much
# def addsWater():
#     theTree.waterLevel += 25
#     if(theTree.waterLevel > 100):
#         theTree.waterLevel = 100

# def addRainChanceAndReset():
#     randomNumber = random.randint(1, 100)
#     for x in myGardenObj.gnomeList:
#         theGnome.gnomeRainPercent += 5
#     if(theGnome.gnomeRainPercent >= 100):
#         treeCreator()
#         theGnome.gnomeRainPercent = 0
#     elif(randomNumber <= theGnome.gnomeRainPercent):
#         addsWater()
#         #print(f"its gonna rain! the random number is:{randomNumber} the gnomeRainPercent number is :{theGnome.gnomeRainPercent}")
#     else:
#         print()
#         #print(f"It did not rain my dude! the random number is:{randomNumber} the gnomeRainPercent number is :{theGnome.gnomeRainPercent}"                                                                        )

# userInput = input()

# def gameStatus():
#     print(f"This is turn number {myGardenObj.turn}")
#     print(f"The tree count is at {len(myGardenObj.treeList)} ")
#     print(f"The gnome count is at {len(myGardenObj.gnomeList)} ")
#     print(f"The woodchuck count is at {len(myGardenObj.gnomeList)} ")
#     print(f"The water level is at {theTree.waterLevel} ")
#     print(f"The chance of rain is at {theGnome.gnomeRainPercent} ")
#     print(f"The chance of you losing a tree caused by a woodchuck is {theWoodChuck.chopPercent}")

# def userDecision():
#     print()

# tenthTurn = 0
# i = 0
# while len(myGardenObj.treeList) < 10:
#     myGardenObj.turn += 1
#     i += 1
#     tenthTurn += 1
#     if(tenthTurn == 10):
#         fiftyFiftyChance(treeCreator(),gnomeCreator())
#         tenthTurn = 0
#     chanceOfShade()
#     waterRemover()
#     fiftyFiftyChance(addRainChanceAndReset(),woodChuckCreator())
#     gnomeCreator()
#     chanceOfTreeLoss()
#     woodChuckTreeChop()
#     gameStatus()
#     userDecision()
#     #print ("Number of items in the list = ", len(myGnomeListObj.gnomeList))