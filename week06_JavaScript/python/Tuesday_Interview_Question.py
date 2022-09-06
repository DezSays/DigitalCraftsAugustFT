# Using python, make an API call to the random user api. Retrieve 10 users and store the first and last name of each user you retrieve. Store the list of users in alphabetical order by last name.

# https://random-data-api.com/documentation

import requests


def getUser():
    newList = []
    # Get 10 users
    for i in range(10):
        response = requests.get('https://random-data-api.com/api/v2/users?size=1').json()
        userName = (response['first_name'],response['last_name'])
        newList.append(userName)
   
    # Bubble sort to organize
    for i in range(len(newList)):
        for y in range(len(newList)-1-i):
            if(newList[y][1] > newList[y+1][1]):
                temp = newList[y+1]
                newList[y+1] = newList[y]
                newList[y] = temp 
                
    print(newList)
getUser()