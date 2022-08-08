# Why do we use functions? Functions are used to make your modular. 
# Whenever we call a function, we type in the name exampleFunction(...)
# Parameters are valuse that a function recieves. These parameters are variables that are created and can only be used within the scope of the function. 

# The scope of this function is only lines 5-6, therefor date cannot be called on line 10, see below:
# def whatsTheDate(date: int) -> str:
#     print("Today's date is: ", date)
    
# whatsTheDate(8)
# print(date)


# Another way to write the above function. See below:
date = 12
def whatsTheDate(date: str) -> str:
    return "Today's date is: %s" % date
    
whatsTheDate(8)
print(date)


# Example 1 of a function that calls another function:
# def whatsTheMonth(month: str) -> str:
#     print('We are in the month of: %s' % month)
#     # Below you can see we are calling the previous function within our new function.
#     print(whatsTheDate(8))
# whatsTheMonth('August')

# Example 2 of a finction that calls another function:
def whatsTheMonth(month: str) -> str:
    return 'We are in the month of: %s' % month
    # Below you can see we are calling the previous function within our new function.
    print(whatsTheDate(8))
whatsTheMonth('August')


def dateTeller(month: str, date: str, year: str) -> str:
    print(whatsTheMonth(month), whatsTheDate(date), year)
    
dateTeller('August', '8', '2022')


# Tuples 
# Tuples can store several values to one variable, and these variables do not need to be the same type. Not mutable, meaning values cannot be changed after instantiation.

my_favorite_colors = ('blue', 'green', 17, 28, 'best friends')
print(type(my_favorite_colors)) #this will show you that we are working with a tuple
print(my_favorite_colors[0]) #this will print blue 
print(my_favorite_colors[2]) #this will print 17
 

# Has a few aplications like dice games, etc. It is important to remember the differences between arrays and tuples. Arrays are mutable, meaning you can change them as you see below in arrayDiceRoll. Tuples are rarely used outside of python. Anything you can do with a tuple you can do with another type. The most common thing tuples are used for are GPS coordinates. 

# Example of how to change an array
arrayDiceRoll = [3,5]
arrayDiceRoll[0] = 1


# How to reverse a string using a for loop

def reverse_string(oldString:str) -> str:  
    newString = ""   
    for i in oldString:  
        newString = i + newString  
    return newString     
     
oldString = "Howdy Yall"    
print("The original string is: ",oldString, ". While the reverse of this string is:", reverse_string(oldString))  


