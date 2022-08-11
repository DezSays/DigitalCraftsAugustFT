# Given a key/value structure, write a function that returns the top three players with the highest score, each being assigned with a medal.

players = {
    'Kate' : 12,
    'Bill' : 23,
    'Joe' : 9,
    'Jackie' : 22,
    'Lin' : 18
}

highestScores = sorted(players, key=players.get, reverse=True)[:3]

def medalAssignment(players: dict) -> dict:
    print(highestScores[0], ": Gold")
    print(highestScores[1], ": Silver")
    print(highestScores[2], ": Bronze")
    
medalAssignment(players)


