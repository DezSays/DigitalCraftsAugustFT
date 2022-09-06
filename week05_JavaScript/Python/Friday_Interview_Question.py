# Your task is to write a program that calculates how much of a tip to leave at a restaurant.
# Prompt the user for two things:
# The total bill amount
# The level of service, which can be one of the following: good, fair, or bad
# Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:
# good -> 20%
# fair -> 15%
# bad -> 10%
# Allow the ability to divide the check into equal parts amount a number of people. The user will enter the number of people to be divided amongst


def checkPlease():

    bill = float(input('Total bill amount? $'))
    print("$%.2f" % bill)

    splitCheck = input("Would you like to split the check? Please enter yes or no. ")

    service = input("""
                    Level of service? 
                    
                    Good
                    Fair
                    Bad
                    
                    """)

    if service.lower() == 'good':
        tip = (bill * 0.2)
        total = bill + tip
        if splitCheck.lower() == 'yes':
            splitInput = int(input("How many ways would you like the check equally divided? Please enter a digit from 2-50. "))
            splitTip = ((bill * 0.2) / splitInput)
            splitTotal = int((bill + tip) // splitInput)
            print("Overall bill: $%.2f" % bill)
            print("Your selected tip amount: $%.2f" % splitTip)
            print("Total bill per person: $%.2f" % splitTotal)
        elif splitCheck.lower() == 'no':
            print("Tip amount: $%.2f" % tip)
            print("Total amount: $%.2f" % total)
    elif service.lower() == 'fair':
        tip = (bill * 0.15)
        total = bill + tip
        if splitCheck.lower() == 'yes':
            splitInput = int(input("How many ways would you like the check equally divided? Please enter a digit from 2-50. "))
            splitTip = ((bill * 0.15) / splitInput)
            splitTotal = int((bill + tip) // splitInput)
            print("Overall bill: $%.2f" % bill)
            print("Your selected tip amount: $%.2f" % splitTip)
            print("Total bill per person: $%.2f" % splitTotal)
        elif splitCheck.lower() == 'no':
            print("Tip amount: $%.2f" % tip)
            print("Total amount: $%.2f" % total)
    elif service.lower() == 'bad':
        tip = (bill * 0.1)
        total = bill + tip
        if splitCheck.lower() == 'yes':
            splitInput = int(input("How many ways would you like the check equally divided? Please enter a digit from 2-50. "))
            splitTip = ((bill * 0.1) / splitInput)
            splitTotal = int((bill + tip) // splitInput)
            print("Overall bill: $%.2f" % bill)
            print("Your selected tip amount: $%.2f" % splitTip)
            print("Total bill per person: $%.2f" % splitTotal)
        elif splitCheck.lower() == 'no':
            print("Tip amount: $%.2f" % tip)
            print("Total amount: $%.2f" % total)
    else:         
        print('Invalid entry. Please try again.')
        

checkPlease()

