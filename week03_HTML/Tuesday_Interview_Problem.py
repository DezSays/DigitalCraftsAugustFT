# An animal rescue center in Atlanta is overcrowded and needs to send some of their dogs to nearby location. They will be sending any dogs with brown fur or that weighs over 50 pounds to the new shelter. Write a function that returns the current allocation of dogs at each center.

import unittest

dogs = [{
        "breed": "German Shepard", 
        "weight": 88, 
        "color":("brown", "black")
    }, 
{
        "breed": "Golden Retriever", 
        "weight": 45, 
        "color": "tan"
    }, 
{
        "breed": "Terrier", 
        "weight": 29, 
        "color": "black"
        }, 
{
        "breed": "French Bulldog", 
        "weight": 12, 
        "color": "black"
        }, 
{
        "breed": "Terrier", 
        "weight": 30, 
        "color": "brown"
        }, 
{
        "breed": "Pit", 
        "weight": 55, 
        "color":("brown", "white")
        }]



def sendDoggos(doggos:list) -> list:
    newShelter = []
    for dog in doggos:
        if dog["weight"] >= 50 or dog["color"] == "brown":
            newShelter.append(dog)
    return(newShelter)
    
print(sendDoggos(dogs))



class TestDoggos(unittest.TestCase):

    def testsendDoggos(self):
        self.assertEqual(sendDoggos(dogs), [{'breed': 'German Shepard', 'weight': 88, 'color': ('brown', 'black')}, {'breed': 'Terrier', 'weight': 30, 'color': 'brown'}, {'breed': 'Pit', 'weight': 55, 'color': ('brown', 'white')}])

unittest.main()
