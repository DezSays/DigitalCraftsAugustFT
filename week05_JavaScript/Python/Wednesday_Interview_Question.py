#  There's a criminal on the loose! There's been a raid in your neighborhood and the suspect is at large. The GBI are searching for the suspect and know that the person of interest is within a 2 mile radius. Given a list of residences in the area, write a function that determines which homes should be searched, and in what order based on the details provided. Return a list of addresses to be submitted to the GBI in their search. The list should be in the order the addresses should be searched, so the function below will sort them by distance.

raid = [{  "name": "Bob",
    "distance": 1.2,
    "crimes_committed": 1,
    "address": "4325 Birch St"
},
{
    "name": "May",
    "distance": 0.3,
    "crimes_committed": 3,
    "address": "8903 Trolley St"
},
{
    "name": "Tyler",
    "distance": 0.8,
    "crimes_committed": 0,
    "address": "2348 Magnolia Dr"
},
{
    "name": "Reggie",
    "distance": 0.5,
    "crimes_committed": 1,
    "address": "3478 Seminole Ln"
},
{
    "name": "Seth",
    "distance": 3.2,
    "crimes_committed": 0,
    "address": "9803 Azul St"
},
{
    "name": "Ray",
    "distance": 2.9,
    "crimes_committed": 0,
    "address": "3467 Frost St"
},
{
    "name": "Kim",
    "distance": 0.1,
    "crimes_committed": 0,
    "address": "7893 Daisy Ln"
},
{
    "name": "Lisa",
    "distance": 1.2,
    "crimes_committed": 1,
    "address": "2345 Gale St"
},
{
    "name": "Ashley",
    "distance": 1.5,
    "crimes_committed": 5,
    "address": "6783 Sycamore St"
},
{
    "name": "Turner",
    "distance": 4.3,
    "crimes_committed": 1,
    "address": "8923 Pecan Ln"
},
]


def raidHome(raid: list) -> list:
    willRaid = []
    for person in raid:
        if person['distance'] < 2 and person['crimes_committed'] > 0:
            if len(willRaid) == 0:
                willRaid.append(person)
            else:
                for position in range(len(willRaid)):
                    if person['distance'] <= willRaid[position]['distance']:
                        willRaid.insert(position, person)
                        break 
                    elif person == len(willRaid) -1:
                        willRaid.append(person)
    return willRaid 


print(raidHome(raid))

