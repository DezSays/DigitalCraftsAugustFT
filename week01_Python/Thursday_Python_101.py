# When you are looking for a length of a string, keep in mind that the space will count as a character. 
name = 'Dez Bryan'

# To get the length of the string above and get a numerical output (in this case the number should be 9), you can use the len() function as shown below:
print(len(name))

# What if I wanted to print just the z from Dez? We would use the index as shown below:
print(name[2])

# What if you wanted to print the length of a list? In the list below, we have 5 things in this list. 
drinks = ['Sprite', 'Green Tea', 'Coffee', 'Coke', 'Pepsi']
print(len(drinks))

# How to get the type, in this case a list, you will need to use the type() function:
print(type(drinks))

# How to get the type, in this case an integer, you will need to use the type() function:
print(type(len(drinks)))

# You can also set the length of something to a variabe as shown below:
length_of_drinks_list = len(drinks)
print(length_of_drinks_list)

# Using a for loop 
for drink in drinks: 
    print(drink)
    
# Example 2 of a for loop, this time using integers
nums = [1,2,3,4,5]

for x in nums:
    print(x)
    
# Example of a while loop. It is important to increment the value, otherwise you will get an endless loop.
value = 0
while value < length_of_drinks_list:
    print(drinks[value])
    value = value + 1
    
# How to iterate through a string using a for loop, such as my name listed at the top:
for letter in name:
    print(letter)

# How to do the same thing we just did but using a while loop
letter = 0
while letter < len(name):
    print(name[letter])
    letter = letter + 1
    
# For loop example to print each number that is evenly divisible by 4. 
    
numbers = [1,2,3,4,5,6,7,8,9,10]

for i in numbers:
    if i % 4 == 0: #on this line, it is saying that if i is evenly divisible by 4, and will give you a remainder of zero, then we move to the next line and print that number. The % is called a modulo, and you can only use it with dividing integers, not floats.  
        print(i)
        
# Print all the odd numbers from the list above
for i in numbers:
    if i % 2 == 1:
        print(i)

# Let the user decide what to print. 
try:
    userChoice = int(input("What would you like each number to be divided by? "))
    for i in numbers:
        if i % userChoice == 0:
            print(i)
except ValueError:
    print("The input was not a valid integer.")
    
# How to do a lexicon comparison. It is important to note that capital letters will always display as being before lower case. See below for example:
mysteryLetter = 'F'
firstNameLetter = 'd'
if firstNameLetter < mysteryLetter:
    print('first name comes before mystery letter')
else:
    print('mystery letter comes before first name')
    
# Exercise: Place students in breakout rooms and organize them by their first name. Pay attention to capitalization! If your cutoff letter is a lower case but all the student are upper case, the upper case will always display before the lower case letters. Use the .lower() function to resolve this. 
students = ['Matt', 'Carlos', 'An', 'Jordan B.']
breakoutRoom1 = []
breakoutRoom2 = []
cutOffLetter = 'i'

for element in students:
    if element[0].lower() <= cutOffLetter:
        breakoutRoom1.append(element)
    elif element[0].lower() > cutOffLetter:
        breakoutRoom2.append(element)
        
        
print(breakoutRoom1)
print(breakoutRoom2)

# Concatenate String example:
fName = 'Dez'
lName = 'Bryan'
fullName = fName + ' ' + lName
print(fullName)