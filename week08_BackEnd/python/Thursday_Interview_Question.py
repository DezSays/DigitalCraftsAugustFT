# Mastermind

# A low-level implementation of the classic game “Mastermind”. We need to write a program that generates a four-digit random code and the user needs to guess the code in 10 tries or less. If any digit out of the guessed four-digit code is wrong, the computer should print out “B”. If the digit is correct but at the wrong place, the computer should print “Y”. If both the digit and position is correct, the computer should print “R”.

# Correct Digit: 5348 -> User Guess: 5182 -> RBYB

# Write a function that starts the game, it should either win or loss depending on the result, write a unit test to verify that your game works



import random
# Step 1: Create a function that generates a random 4 digit number

# Step 2: Prompt user to enter a value and store it

# Step 3: Compare the answer to the guess, create hint based on the guess

# Step 4: Have the game run until user guesses right or 10 turns have been used 

def mastermind():
    # Generate each number individually then concatenate them
    answer = generateNumber()
    turns = 0
    win = False
    print('Welcome to Mastermind!')
    while turns <= 10 and win == False:
        guess = input('Enter a number: ')
        if checkGuess(guess, answer) == True:
            win = True
            print("You've Won!, the answer was ", answer)
        
    if turns >= 10:
        print("You've lost!")

def generateNumber() -> str:
    number = ''
    for num in range(0,4):
        number += str(random.randint(0,9))

    return number

# Check if the guess is equal to the answer
def checkGuess(guess: str, answer:str) -> bool:
    hint = ''
    for i in range(0,4):
        # If the guess at this index is the same as the answer, add a R
        if guess[i] == answer[i]:
            hint += 'R'
        # Check if answer contains the guessed number, add Y if true
        elif guess[i] in answer:
            hint += 'Y'
        # If the number is not in the answer at all add a B
        else:
            hint += 'B'
    print(hint)
    return hint == 'RRRR'

mastermind()