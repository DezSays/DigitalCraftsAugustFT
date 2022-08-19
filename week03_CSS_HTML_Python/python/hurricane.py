import random

class Hurricane:
    def __init__(self, depCounter, nsCounter):
        self.category = ''
        self.destination = ''
        self.speed = 0
        self.name = ''
        self.storms = []
        self.depCounter = depCounter
        self.nsCounter = nsCounter

        self.assignCategory()

    stormList = ['Ann', 'Beth', 'Charlie', 'Darlene', 'Ethan', 'Francis', 'George', 'Harry', 'Ingram', 'Jane', 'Karl', 'Lisa', 'Martin', 'Nicole',
    'Owen', 'Phillippe', 'Rina', 'Shary', 'Tammy', 'Virginie',
    'Walter']

    places = ['Honolulu', 'Miami', 'Atlanta', 'Charlotte', 'Boston', 'New York', 'D.C.', 'Baltimore', 
        'Cape Hatteras', 'Morehead', 'Wilmington', 'Savannah', 'Myrtle Beach']

    def assignCategory(self):
        severity = random.randint(0,99)
        if severity < 20:
            self.category = 'Tropical Depression'
            self.speed = random.randint(1, 20)
            self.destination = self.places[random.randint(0, 12)]
            self.name = self.depCounter
            self.depCounter += 1

        elif severity >= 20 and severity < 38:
            self.category = 'Tropical Storm'
            self.speed = random.randint(1, 20)
            self.destination = self.places[random.randint(0, 12)]
            self.name = self.stormList[self.nsCounter]

        elif severity >= 38 and severity < 50:
            self.category = 'Category 1'
            self.speed = random.randint(1, 20)
            self.destination = self.places[random.randint(0, 12)]
            self.name = self.stormList[self.nsCounter]

        elif severity >= 50 and severity < 60:
            self.category = 'Category 2'
            self.speed = random.randint(1, 20)
            self.destination = self.places[random.randint(0, 12)]
            self.name = self.stormList[self.nsCounter]

        elif severity >= 60 and severity < 66:
            self.category = 'Category 3'
            self.speed = random.randint(1, 20)
            self.destination = self.places[random.randint(0, 12)]
            self.name = self.stormList[self.nsCounter]

        elif severity >= 66 and severity < 69:
            self.category = 'Category 4'
            self.speed = random.randint(0, 20)
            self.destination = self.places[random.randint(0, 12)]
            self.name = self.stormList[self.nsCounter]

        elif severity >= 69 and severity < 70:
            self.category = 'Category 4'
            self.speed = random.randint(1, 20)
            self.destination = self.places[random.randint(0, 12)]
            self.name = self.stormList[self.nsCounter]

def simulate():
    number = 0
    nsCounter = 0
    depCounter = 1
    storms = []

    while number < 24:
        storms.append(Hurricane(depCounter, nsCounter))
        if storms[number].category == 'Tropical Depression':
            depCounter += 1
        elif storms[number].category == 'Tropical Storm':
            nsCounter += 1
        elif len(storms[number].category) != 0 and storms[number].category[0] == 'C':
            nsCounter += 1
        number += 1

    for storm in storms:
        if storm.name != '':
            print("Name: %s \nCategory: %s \nSpeed: %s \nDestination: %s" % (storm.name, storm.category, storm.speed, storm.destination))
            print('---------------------------------')
        


simulate()
