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

isSunny = True


if currentTemp < freezingTemp and isRaining == True:
    print('It is freezing and raining. Snow/hail time yall.')
elif currentTemp > freezingTemp and isRaining == False:
    print('What a lovely day!')
else:
    print('It is not a lovely day.')
    
