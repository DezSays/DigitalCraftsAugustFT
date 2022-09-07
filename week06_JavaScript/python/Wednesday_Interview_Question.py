# Create simulated tic tac toe game. The game should consist of 2 players, one using 'X' and the other 'O'. After each turn, player should mark a space on the board according to their corresponding marker. Once a player successfully gets 3 pieces across or diagonally, print who won. If there is no winner, print 'Tie game'.


gameBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_key = []

for key in gameBoard:
    board_key.append(key)

# The board that the user will see
def printBoard(board):
    print('')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    

# Gameplay functionality
def ticTacToe():
    player = 'X'
    count = 0

    for XorO in range(10):
        printBoard(gameBoard)
        print(f"\nIt's your turn {player}. Move to which place?\n")

        move = input()        

        if gameBoard[move] == ' ':
            gameBoard[move] = player
            count += 1
        else:
            print(f"\nThe place you selected has already been filled. {player}, please select an available placement.\n")
            continue

        # Win conditions 
        if count >= 5:
            if gameBoard['7'] == gameBoard['8'] == gameBoard['9'] != ' ': # across the top
                printBoard(gameBoard)
                print("\nGame Over.\n")                
                print(player + " won!")                
                break
            elif gameBoard['4'] == gameBoard['5'] == gameBoard['6'] != ' ': # across the middle
                printBoard(gameBoard)
                print("\nGame Over.\n")                
                print(player + " won!")
                break
            elif gameBoard['1'] == gameBoard['2'] == gameBoard['3'] != ' ': # across the bottom
                printBoard(gameBoard)
                print("\nGame Over.\n")                
                print(player + " won!")
                break
            elif gameBoard['1'] == gameBoard['4'] == gameBoard['7'] != ' ': # down the left side
                printBoard(gameBoard)
                print("\nGame Over.\n")                
                print(player + " won!")
                break
            elif gameBoard['2'] == gameBoard['5'] == gameBoard['8'] != ' ': # down the middle
                printBoard(gameBoard)
                print("\nGame Over.\n")                
                print(player + " won!")
                break
            elif gameBoard['3'] == gameBoard['6'] == gameBoard['9'] != ' ': # down the right side
                printBoard(gameBoard)
                print("\nGame Over.\n")                
                print(player + " won!")
                break 
            elif gameBoard['7'] == gameBoard['5'] == gameBoard['3'] != ' ': # diagonal left to right
                printBoard(gameBoard)
                print("\nGame Over.\n")                
                print(player + " won!")
                break
            elif gameBoard['1'] == gameBoard['5'] == gameBoard['9'] != ' ': # diagonal right to left
                printBoard(gameBoard)
                print("\nGame Over.\n")                
                print(player + " won!")
                break 

        # Tie Condition
        if count == 9:
            print("\nGame Over.\n")                
            print("\nIt's a Tie!\n")

        # Toggle players
        if player =='X':
            player = 'O'
        else:
            player = 'X'        
    
    # Play again?
    restartGame = input("\nDo want to play Again?(y/n)\n")
    restart = restartGame.lower()
    if restart == "y":  
        for key in board_key:
            gameBoard[key] = " "

        ticTacToe()
    else:
        print('Thank you for playing!')

ticTacToe()
