# Prompt:
# Given a key/value structure, write a function that returns the top three players with the highest score, each being assigned with a medal.





# Solution 1

# players1 = {
#     'Kate' : 12,
#     'Bill' : 3,
#     'Joe' : 9,
#     'Jackie' : 22,
#     'Lin' : 18
# }

# def medalAssignment(players: dict) -> list:
    
#     highestScores = sorted(players, key=players.get, reverse=True)
    
#     print(highestScores[0], ": Gold")
#     print(highestScores[1], ": Silver")
#     print(highestScores[2], ": Bronze")
    
# medalAssignment(players1)






# Solution 2

# def medals(playerScores: dict) -> dict:         #defines a function that takes in and returns dict
#     medalDict = {           #initializes return dict
#         'Gold' : '',
#         'Silver' : '',
#         'Bronze' : ''
#         }

#     #initializes variables for gold, silver, bronze
#     goldNum = 0
#     silverNum = 0
#     bronzeNum = 0
#     sortedScores = sorted(playerScores.values(), reverse = True)        #sorts scores in reverse order
#     sortedPlayers = {}                                          #initializes dict for sorting players
#     for x in sortedScores:                                      #cycles through each number in sorted scores
#         for y in playerScores.keys():                           #cycles through each value in submitted dict
#             if playerScores[y] == x:                    #checks if value in sorted score is equal to value in submitted dict
#                 sortedPlayers[y] = playerScores[y]      #sets key for value to equal the key that was submitted
    
#     for player in sortedPlayers.keys():         #cycles through each name in new sorted dict
#         if sortedPlayers.get(player) > goldNum:         #checks if number is higher than gold
#             medalDict['Gold'] = player                  #sets gold value
#             goldNum = sortedPlayers.get(player)
#         elif sortedPlayers.get(player) > silverNum:      #checks if number is higher than silver
#             medalDict['Silver'] = player                #sets silver value
#             silverNum = sortedPlayers.get(player)
#         elif sortedPlayers.get(player) > bronzeNum:     #checks if number is higher than bronze
#             medalDict['Bronze'] = player                #sets bronze value
#             bronzeNum = sortedPlayers.get(player)
#     return medalDict                                   #returns dict

# players = {
#     'Zeus' : 39,
#     'Hera' : 23,
#     'Athena' : 34,
#     'Ares' : 28,
#     'Aphrodite' : 22,
#     'Hades' : 25,
#     'Poseidon' : 35,
#     'Hermes' : 27
# }

# print(medals(players))








# Solution 3

# player1 = {
#     'Zeus' : 39,
#     'Hera' : 23,
#     'Athena' : 34,
#     'Aries' : 28,
#     'Aphrodite' : 22,
#     'Hades' : 25,
#     'Poseidon' : 35,
#     'Hermes' : 27}

# player2 = {
#     'Kate' : 12,
#     'Bill' : 3,
#     'Joe' : 9,
#     'Jackie' : 22,
#     'Lin' : 18
# }

# def winners(result: dict) -> dict:
#     first, second, third = ('', 0), ('', 0), ('', 0)
    
#     for player in result:
#         if result.get(player) > first[1]:
#             third = second 
#             second = first 
#             first = (player, result.get(player))
#         elif result.get(player) < first[1] and result.get(player) > third[1]:
#             third = second 
#             second = (player, result.get(player))
#         elif result.get(player) > third[1]:
#             third = (player, result.get(player))
#     return({'Gold': first[0], 'Silver': second[0], 'Bronze': third[0]})
# print(winners(player1))