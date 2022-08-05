# Intro to Python Types

# Integers
# Assigning the left hand side(the variable), then the assignment operator(=) which assigns the value on the right hand side(26) to the variable on the left hand side(age). The age is only considered an integer because it is a whole number!
age = 26
print(age)

#Float (a number that is not a whole number. Think of pi, 3.14. It is not considered an integer because it is not a whole number.)
pi = 3.14159
print(pi)

# Statement is a general term for a single instruction that uses or manipulates a value. Lines 5,6,9, and 10 are all examples of statements. These comments are NOT considered a statement.

#Boolean - can only have a true or false value. Must capitalize True and False. 
isRaining = False

#Strings: a combination of alphanumeric values. All of the following are examples of strings:
name = 'Dez'
team = 'Braves'
birthday = "October 7, 1995"
# if you want multiple lines, like a paragraph, do the following:
months = '''
Jan,
Feb,
March,
April,
Etc.'''

print(months)
print(name)

#List - this is a sequence of values. These values can be numbers, integers, floats, etc. 
scores = [12,54,896,15]
names = ['dez', 'tri', 'doug']

# Dictionary: this is a sequence of labeled values
NBATeams = {"Atlanta": "Hawks", "Houston": "Rockets", "Orlando": "Magic"}
print(NBATeams["Atlanta"])

# Special characters:
# \b - backspace
# \n - new line
# \t - horizontal tab
# \v - vertical tab
# \r - carriage return

username = input("Type in your username: ")
password = input('Type in your password: ')
print(username)
print(password)

# Using a variable within the print command in a more personalized way by using the interpolation operator. The interpolation operator takes values that are stored in variables and places them within the string. 
print("Welcome %s" % username)

myAge = '26'
print('I am %s' % myAge)

# Using a float, you will use %f. If you only want a few numbers after the decimal, say you want 3 after the decimal, you would write it as you see below. It will round the number!:
print('Pi: %.3f' % pi)

# Division: The below will return the result as a float (2.0), NOT as an integer.
result = 4/2
print('Result: ', result)

# Absolute value
positiveNumber = abs(-45)
print(positiveNumber)

# Exponents and Rounding
exponents = pow(2,2)

rounding = round(pi)

print(exponents)
print(rounding)

# How to control the flow using an if statement. 

currentTemp = 35
freezingTemp = 32

if currentTemp < freezingTemp:
    print('It is way too cold out here man!')
elif currentTemp > freezingTemp:
    print('Ahh, warm weather!')
elif currentTemp == freezingTemp:
    print('It is right at the freezing point. Better buy some milk and bread!')
else: 
    print('There seems to be an error. Check your code')
    
# Here are examples of multiple conditions
# isRaining = False -- this does not need to be listed again, because we already assigned isRaining to False on line 15.

isSunny = False

# AND - meaning both conditions on either side of the and must be true
if currentTemp < freezingTemp and isRaining == True:
    print('It is freezing and raining. Snow/hail time yall.')
elif currentTemp > freezingTemp and isRaining == False:
    print('What a lovely day!')
else:
    print('It is not a lovely day.')
    
# OR - only one needs to be true
if currentTemp < freezingTemp or isRaining == True:
    print('It is freezing or it is raining. Either way, stay inside today guys.')
elif currentTemp > freezingTemp or isRaining == False:
    print('It is a clear day today!')

if isSunny != True:
    print('It is not sunny. The != operator in the if statement means not.')
    
# Class Exercise: create a program that takes in the id number of the user and prints "1st" if the id is less than 100 and 2nd if its greater than 100 but less than 250. If the id is greater than 250 then print "all reservations taken".
# In order to complete this exercise, you will need to use int() to tell the computer that it needs to listen for the input of an integer. 

try:
    id = int(input("Type in your reservation number: "))
    if id <= 100 and id > 0:
        print("1st")
    elif id > 100 and id < 250:
        print("2nd")
    elif id > 250:
        print("All reservations have been filled. Please try again later.")
    else:
        print("This is not a number in our system. Please check your reservation number and try again.")
except ValueError:
    print("The input was not a valid integer. Please check your reservation number and try again.")


# Lists

GeorgiaPeeps = ['Dez', 'Matt', 'Dre']

# Print the entire list
print(GeorgiaPeeps)

# Print the first individual. It is important to remember that the index for any list begins with the number 0, not 1. So to access the first name in this list, we need to do the following:
print(GeorgiaPeeps[0])

# For Loop Examples Below

# Example 1, will print all names
for name in GeorgiaPeeps:
    print(name)
    
# Example 2, will change the names. Dez will now show up as TA in the printed list, Dre as Instructor, and Matt as Student as opposed to their names.
for name in GeorgiaPeeps:
    if name == 'Dre':
        print("Instructor")
    elif name == 'Dez':
        print('TA')
    else:
        print("Student")

# Example 3, will print the numbers 0-9
for number in range(10):
    print(number)

# Example 4, print numbers 5-10
for number in range(5,11):
    print(number)
    
# Print the first letter of Atlanta 
city = 'Atlanta'
print(city[0])

# How to delete the last item from an array:
GeorgiaPeeps.pop()
print(GeorgiaPeeps)

