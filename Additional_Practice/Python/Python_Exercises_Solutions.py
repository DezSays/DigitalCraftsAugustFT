
# *Exercise 1 Solution and Explanation*

# def add_multiply(num1: int, num2: int) -> int: # Create a function that takes in two parameters, our two numbers we want to either add or multiply.
    
#     product = num1 * num2       # multiply your numbers and assign them to a variable
    
#     if product <= 1000:         # Using an if statement, see if the product of your two numbers is equal to or less than 1000. 
#         return product          # If the product is 1000 or lower, then we return the number. 
#     else:                       # If the product is 1001 or greater: 
#         return num1 + num2      # We need to return the sum of these numbers instead.


# result = add_multiply(20, 30)   # Using Part 1 values
# print("The result is", result)

# result = add_multiply(40, 30)   # Using Part 2 values
# print("The result is", result)




# *Exercise 2 Solution and Explanation*

# previous_num = 0                            # Set up the initial value of the previous number globally. 

# for current_num in range(1, 11):            # Set up your for loop from 1 to 10
#     sum_value = previous_num + current_num  # Assign the previous number plus the current number to the variable sum_value
#     print("Current Number:", current_num, "Previous Number:", previous_num, " Sum:", previous_num + current_num) 
#     # Modify the previous number variable by setting it to the current number variable each time it iterates through the loop
#     previous_num = current_num
    
    
    
    
# *Exercise 3 PART 1 Solution and Explanation*

# name = input("What is your name: ")                                 # Have the user enter their name
# age = int(input("How old will you be by the end of this year: "))   # Have the user enter how old they will be by the end of this year
# current_year = int(input("What is the current year: "))             # Have the user input the current year
# year = current_year - age + 100                                     # Take the current year, subtract the users age, and add 100 then assign this to a variable labeled year. 
# print(name + " will be 100 years old in " + str(year))              #Print out the users name and convert the year to a string so that you can concatenate everything as a string. 
    
    
    
    
# *Exercise 3 PART 2 Solution and Explanation*

# name = input("What is your name: ")                                 # Have the user enter their name
# age = int(input("How old will you be by the end of this year: "))   # Have the user enter how old they will be by the end of this year
# current_year = int(input("What is the current year: "))             # Have the user input the current year
# year = current_year - age + 100                                     # Take the current year, subtract the users age, and add 100 then assign this to a variable labeled year. 
# print(f'{name} will be 100 years old in {year}')              #Print out the users name and year they will turn one hundred by using an f string, which allows you to combine different data types.




# *Exercise 4 Solution and Explanation*

# num = int(input("What number would you like to enter: ")) # Get the user to input a number, and use the int function to convert their input into an integer instead of a string.

# def even_or_odd(number: int) -> int:        # Create a function that takes in one parameter, an integer
#     if number % 2 == 0:                     # Set up if statement to see if the number entered could be divided by two with a remainder of 0.
#         print('Even number')                # If the remainder is 0, print even number. 
#     else:                                   # If there is a remainder,
#         print('Odd number')                 # Print out odd number 
        
# even_or_odd(num)                            # Call the function and pass in the variable used for the number given to us by the user.




# *Exercise 5 Solution and Explanation*

# sample_list = [5, 10, 15, 20, 25]   # Create a generic sample list


# def newList(old_list: list) -> list:    # Create a function that takes in one parameter, a list. 
#     new_list = [old_list[0], old_list[len(old_list)-1]] # Set up variable, new list, which will hold the values of what is in the first and last index of the sample list. We need to take the first number in sample list, which can be found and index 0, and the last number in sample list, which we get by taking the sample list, and inside the index take the length of sample list - 1, which will give us the number found in the last index of sample list.
#     print(new_list)     # Print out the numbers we found in the first and last index of the sample list 
    

# newList(sample_list)    # Call our function and pass in the sample_list




# *Exercise 6 Solution and Explanation*

# word = input("Please enter a word: ")       # Get the users input and assign it to the variable word

# length_of_word = len(word)      # Get the length of the word entered by the user, and assign it to the variable length_of_word

# for letter in range(0, length_of_word, 2):   # For each letter that is within the range of the first index position (which is why we have the 0) to however long the users word was (which is why we have length_of_word), we want each letter that falls on an even index (which is why we have the 2). 
#     print(word[letter])     # Print out the letters that are on even indices of the given word. 



# *Exercise 7 Solution and Explanation*

# def remove_characters(word: str, x: int) -> str: # Set up a function to take in a string and an integer
#     i = word[x:] # Set the variable i = the string sliced by a given number
#     print(i) # print out the string after it has been sliced 

# specified_word = "dezbryan" # Set up a variable to equal the string we want to slice

# remove_characters(specified_word, 4) # Our function takes our string and slices off the first 4 letters, giving us the output of ryan. 
# remove_characters(specified_word, 2) # Our function takes our string and slices off the first 2 letters, giving us the output of zbryan. 



# *Exercise 8 Solution and Explanation*

# def compare_nums(nums:list) -> bool: #Set up our function to take in a list and return a boolean.
    
#     first_num = nums[0]         #Assign first_num variable = first number in the nums list
#     last_num = nums[-1]         #Assign last_num variable = last number in the nums list
    
#     if first_num == last_num:   #If the first number in the list is the same as the last number in the list
#         print(True)             #then we want it to return true
#     else:                       #if the two numbers are not the same
#         print(False)            #then we want it to return false

# x = [10, 20, 30, 40, 10]        #list we are comparing the first and last indices of
# compare_nums(x)                 #pass in our list to our function

# y = [75, 65, 35, 75, 30]        #list we are comparing the first and last indices of
# compare_nums(y)                 #pass in our list to our function



# *Exercise 9 Solution and Explanation*

# list =  [10, 20, 33, 46, 55]            #Setting up a list we want to pull all multiples of five.
# newList = []                            #Setting up an empty list that we will later append our multiples of five to.

# def multiples_of_5(nums: list) -> list: #Setting up our function with one parameter, a list, with the expectation of this function producing us another list. 
#     for numbers in nums:                #For each number in the list that we pass in to our function
#         if numbers % 5 == 0:            #If that number can be divided by 5 with a remainder of 0,
#             newList.append(numbers)     #Append the numbers that are multiples of 5 to the new list
#     print(newList)                      #Print off our new list

# multiples_of_5(list)                    #Call our function and pass in our list



# *Exercise 10 Solution and Explanation*

# x = "Dez is good developer. Dez is a turkey." #Here is the string we are going to use the count method on.

# word_repeats = x.count("Dez") # Use count method of a str class to count how many occurances of Dez are in the string.

# print(word_repeats) #Print out the number of times Dez is found in the string.



# *Exercise 11 Solution and Explanation*

# for nums in range(6): # This for loop sets up the loop to ranges to 6
#     for numbers in range(nums): # This for loop takes each number within the range above and runs this through each number
#         print (nums, end=" ") # This prints the numbers and adds the appropriate spacing
#     print("\n") # This is needed to print each row of numbers on a new line to display pattern correctly.



# *Exercise 12 Solution and Explanation*

# firstList = [10, 20, 25, 30, 35]                      # set up first list to pull out odd numbers
# secondList = [40, 45, 60, 75, 90]                     # set up second list to pull out even numbers
# newList = []                                          # set up an empty new list 

# def specified_list(list1: list, list2: list) -> list: # set up function that takes in two lists and we expect it to return a new list
#     for num in list1:                                 # iterate through the first list
#         if num % 2 != 0:                              # check if current number is odd
#             newList.append(num)                       # add odd number to result list
    
#     for num in list2:                                 # iterate through the second list
#         if num % 2 == 0:                              # check if current number is even
#             newList.append(num)                       # add even number to result list
#     print(newList)                                    # print out our new list

# specified_list(firstList, secondList)                 # call our function and pass in our first and second lists



# *Exercise 13 Solution 1 and Explanation*

# num = 7536              # Set up a number you would like to see reversed

# reversed_num = 0        # Set up variable that our new int will be

# while num != 0:         # Set up your while loop to run as long as the number is not 0.
#     digit = num % 10    # the remainder of the num divided by 10 is stored in the variable digit. Now, the digit contains the last digit of num
#     reversed_num = reversed_num * 10 + digit # digit is then added to the variable reversed after multiplying it by 10. Multiplication by 10 adds a new place in the reversed number.
#     num //= 10          # num is then divided by 10 so that now it only contains the first three digits

# print(reversed_num)     # print out our new number




# *Exercise 13 Solution 2 and Explanation*

# num = 7536              # Set up number we want reversed

# print(str(num)[::-1])   # Turn our integer into a string, slice that bad boy, then print it out




# *Exercise 14 Solution and Explanation*

# for num1 in range(1, 11):           #Set up a for loop for the first number with a range of 10
#     for num2 in range(1, 11):       #Set up a for loop for the second number with a range of 10
#         print(num1 * num2, end=" ") #Multiply the first number and the second number, and add a space at the end
#     print("\t")                     #Gives us even space between so they stack nicely




# *Exercise 15 Solution and Explanation*

# for space in range(6, 0, -1):           #for each space in range starting with 6 and decrementing
#     for star in range(0, space - 1):    #for each star in range of 0 to 5
#         print("*", end=' ')             #this prints the star on each line and ends it with a space
#     print(" ")                          #this prints the stars vertically instead of horizontally




# *Exercise 16 Solution and Explanation*

# def exponent(base: int, exponent:int) -> int:   #set up function to take in two parameters
#     num = exponent                              #assign variable num = the exponent parameter
#     result = 1                                  #Let the result equal to one, not zero. Anything multiplied by 0 will always be 0.
#     while num > 0:                              #set up while loop so that as long as the exponent is larger than 0
#         result = result * base                  #set the result equal to the answer of our equation
#         num = num - 1                           #decrement our exponent so we aren't in an infinite loop
#     print(f"{base} raised to the power of {exponent} is: {result}") #using an f string, print our results

# exponent(5, 4)                                  #call our function and pass in the base and the exponent.




# *Exercise 17 Solution and Explanation*

# def count_words():                          #Set up our function
#     file = open("newFile.txt","r")          #Set file = open('name-of-file.filetype', and here we have r to assign the read command)
#     count = 0                               #Set the initial count value to zero
#     data = file.read()                      #Assign the variable data = reading our file
#     words = data.split()                    #Assign the variable words = the reading of our file and 'split' the sentences so we can count the words instead of the letters
#     for word in words:                      #For every word in our file 
#         count += 1                          #Increment the count by 1
#     print(f"Total words are: {count}")      #Print out the amount of words by printing our count variable
#     file.close()                            #Always remember to close your files so you don't have a data leak!

# count_words()                               #Call our function




# *Exercise 18 Solution and Explanation*

# def count_words():                          #Set up our function
#     file = open("newFile.txt","r")          #Set file = open('name-of-file.filetype', and here we have r to assign the read command)
#     count = 0                               #Set the initial count value to zero
#     data = file.read()                      #Assign the variable data = reading our file
#     words = data.split()                    #Assign the variable words = the reading of our file and 'split' the sentences so we can count the words instead of the letters
#     for word in words:                      #For every word in our file
#         if word =="the" or word =="The":    #If the word is either lower case or upper case 'The'
#             count += 1                      #Then we increment our count by 1
#     print(count)                            #Print out the amount of words by printing our count variable
#     file.close()                            #Always remember to close your files so you don't have a data leak!

# count_words()                               #Call our function




# # *Exercise 19 Solution and Explanation*

# def display_words():                        #Set up our function
#     file = open("newFile.txt","r")          #Set file = open('name-of-file.filetype', and here we have r to assign the read command)
#     data = file.read()                      #Assign the variable data = reading our file
#     words = data.split()                    #Assign the variable words = the reading of our file and 'split' the sentences so we can count the words instead of the letters
#     for word in words:                      #For every word in our file
#         if len(word) < 4:                   #If the length of the word is less than 4
#             print(word, end=" ")            #This prints out our words less than four, the end=" " allows us to print them horizontally like a sentence instead of vertically.
#     file.close()                            #Always remember to close your files so you don't have a data leak!

# display_words()                             #Call our function




# # *Exercise 20 Solution and Explanation*

# def count_words():                          #Set up our function
#     file = open("newFile.txt","r")          #Set file = open('name-of-file.filetype', and here we have r to assign the read command)
#     count = 0                               #Set the initial count value to zero
#     data = file.read()                      #Assign the variable data = reading our file
#     words = data.split()                    #Assign the variable words = the reading of our file and 'split' the sentences so we can count the words instead of the letters
#     for word in words:                      #For every word in our file
#         word = word.lower()                 #Turn all words into lower case so that our if statement will count upper and lower case words.
#         if word == 'this' or word =='that': #If the word is either this or that
#             count+=1                        #Then we need to increment the count by 1
#     print(count)                            #Print out our new count variable
#     file.close()                            #Always remember to close your files so you don't have a data leak!

# count_words()                               #Call our function




# # *Exercise 21 Solution and Explanation*

# def count_words():                          #Set up our function
#     file = open("newFile.txt","r")          #Set file = open('name-of-file.filetype', and here we have r to assign the read command)
#     count = 0                               #Set the initial count value to zero
#     data = file.read()                      #Assign the variable data = reading our file
#     words = data.split()                    #Assign the variable words = the reading of our file and 'split' the sentences so we can count the words instead of the letters
#     for word in words:                      #For every word in our file
#         if word[-1] == 'e':                 #If the last index of our word is an 'e'
#             count+=1                        #Then we need to increment the count by 1
#     print(count)                            #Print out our new count variable
#     file.close()                            #Always remember to close your files so you don't have a data leak!

# count_words()                               #Call our function




# # *Exercise 22 Solution and Explanation*

# def count_letter():                          #Set up our function
#     file = open("newFile.txt","r")           #Set file = open('name-of-file.filetype', and here we have r to assign the read command)
#     data = file.read()                       #Assign the variable data = reading our file
#     count = 0                                #Set the initial count value to zero
#     for letter in data:                      #For each letter in the words within our designated file
#         if letter.isupper():                 #If the letter is upper case
#             count+=1                         #Then we increment the count
#     print(count)                             #Print out the new count
#     file.close()                             #Always remember to close your files so you don't have a data leak!            

# count_letter()                               #Call our function!




# # *Exercise 23 Solution and Explanation*

# def sleep_in(weekday: bool, vacation: bool) -> bool:          #Set up our function to take in two parameters
#   if not weekday or vacation:                                 #If our first parameter is false or our second parameter is true
#     return True                                               #return true
#   else:                                                       #otherwise
#     return False                                              #return false

# print(sleep_in(False, False))                                 #print it out so we can see it, call our function, pass in parameters




# # *Exercise 24 Solution and Explanation*

# def monkey_trouble(a_smile: bool, b_smile: bool) -> bool:     #set up your function to take in two parameters
#   if not a_smile and not b_smile:                             # if neither of them are smiling
#     return True                                               # return true
#   if a_smile and b_smile:                                     # if they are both smiling
#     return True                                               # return true
#   else:                                                       # otherwise
#     return False                                              # return false

# print(monkey_trouble(True, True))                             # print it out so we can see it, call our function, pass in parameters




# # *Exercise 25 Solution and Explanation*

# def newStr3(str):                                     # set up a function to take in one parameter, a string
#     if len(str) >= 3:                                 # if the string has a length of 3 or more
#       wordAdd = str[0] + str[1] + str[2]              # assign a variable that will hold the values of the first three indices in the string
#       result = wordAdd*3                              # assign a variable to equal three of the variable above
#       return result                                   # return the variable above 
#     elif len(str) == 2:                               # if the string has a length of exactly 2
#       wordAdd = str[0] + str[1]                       # assign a variable that will hold the values of the first two indices in the string
#       result = wordAdd*3                              # assign a variable to equal three of the variable above
#       return result                                   # return the variable above 
#     elif len(str) == 1:                               # if the string has a length of exactly 1
#       wordAdd = str[0]                                # assign a variable that will hold the value of the first index in the string
#       result = wordAdd*3                              # assign a variable to equal three of the variable above
#       return result                                   # return the variable above 
#     else:                                             # if none of the above are true
#       return ''                                       # return an empty string


# str1 = 'Chocolate'                                    # test string
# str2 = 'ab'                                           # test string

# print(newStr3(str2))                                  # print out the results of your function




# # *Exercise 26 Solution and Explanation*


# def makes10(a, b):                                # set up a function to take in two integers as parameters
#   if (a == 10 or b == 10) or (a + b == 10):       # if the first or second value is ten, or if added together they make ten
#     return True                                   # return true
#   else:                                           # otherwise 
#     return False                                  # return false

# print(makes10(10,2))                              # print out your function




# # *Exercise 27 Solution and Explanation*


# def sum_double(a, b):                 # set up a function to take in two integers as parameters
#   if a != b:                          # if the numbers are different
#     return (a + b)                    # return their sum
#   else:                               # if the numbers are the same
#     result = a + b                    # set a variable equal to their sum
#     return (result + result)          # return double the sum
# print(sum_double(5,5))                # print out your function




# # *Exercise 28 Solution and Explanation*


# def pos_neg(a, b, negative):                                              # set up a function to take in two integers and a boolean
#   if ((a < 0 and b > 0) or (a > 0 and b < 0)) and negative == False:      # if one of the parameters is negative while the other is postive and the final parameter is false
#     return True                                                           # return true
#   elif (a < 0 and b < 0) and negative == True:                            # if both parameters are negative and the final parameter is true
#     return True                                                           # return true
#   else:                                                                   # otherwise
#     return False                                                          # return false
# print(pos_neg(1,-2,False))                                                # print out the function




# # *Exercise 29 Solution and Explanation*


# def parrot_trouble(talking, hour):                    # set up function to take in one integer and one boolean as parameters
#   if (hour < 7 or hour > 20) and talking == True:     # if the hour is less than 7 or greater than 20, and the last parameter is true                       
#     return True                                       # return true
#   else:                                               # otherwise
#     return False                                      # return false
# print(parrot_trouble(True, 6))                        # print out function




# # *Exercise 30 Solution and Explanation*


# def near_hundred(n):                                      # set up a function to take in one integer as a parameter
#   if (n > 89 and n < 111) or (n > 189 and n < 211):       # if our parameter is greater than 89 and less than 111, or our parameter is greater than 189 and less than 211
#     return True                                           # return true
#   else:                                                   # otherwise
#     return False                                          # return false
# print(near_hundred(50))                                   # print out your function




# # *Exercise 31 Solution and Explanation*


# def diff21(n):            # set up a function to take in one integer as a parameter
#   if n < 21:              # if the parameter is less than 21
#     val = 21 - n          # assign a variable to hold the value of 21 minus the parameter
#     return val            # return the variable above
#   else:                   # otherwise
#     val = n - 21          # assign a variable to hold the value of the parameter minus 21
#     result = val * 2      # multiply the above variable by 2
#     return result         # return the value of the variable above
# print(diff21(5))          # print out the function




# # *Exercise 32 Solution and Explanation*


# def build_house(small, big, result):                          # set up a function to take in three integers as parameters
#     if result % 5 <= small and result-(big*5) <= small:       # if the value in the final parameter can be divided by five with a remainder of 0 and it is the same size or smaller than the first parameter, and the final parameter minus (second parameter multiplied by 5) is equal to or smaller than the first parameter
#         return True                                           # return true
#     else:                                                     # otherwise
#         return False                                          # return false
    
# print(build_house(3,2,10))                                    # print out the function




# # *Exercise 33 Solution and Explanation*


# def roundMe(num):                                         # set up function to take in one integer as a parameter
#     if num % 10 < 5:                                      # if the parameter divided by 10 has a remainder that is less than 5
#         total = num - (num % 10)                          # assign a variable to hold the value of the parameter minus (parameter modulos 10)
#         return total                                      # return the variable directly above
#     else:                                                 # otherwise
#         total = num + (10 - num % 10)                     # assign a variable to hold the value of the parameter plus (10 minus parameter modulos 10)
#         return total                                      # return the variable above
    
# def numSum(a,b,c):                                        # set up your second function to take in three integers as parameters
#     result = roundMe(a) + roundMe(b) + roundMe(c)         # assign a variable to the sum of the rounded parameters. We use the first function to help us here. 
#     return result                                         # return the variable above

# print(numSum(12,13,14))                                   # print out the function


# *--------------------------- Solutions available below. Explanation and hints coming soon. -------------------------------------------

# # *Exercise 34 Solution and Explanation*

# def fibonacci(num):
#     if num == 0:
#         return 0
#     elif num == 1:
#         return 1
#     elif num < 0:
#         print('Please enter a positive value')
#     else:
#         result = fibonacci(num-1)+fibonacci(num-2)
#         return result 


# def finalSequence():
#     try:
#         value = int(input('Please enter a positive number: '))
#         fibonacci(value)
#         for numbers in range(value):
#             print(fibonacci(numbers))
#     except ValueError:
#         print("Invalid entry.")

# finalSequence()




# # *Exercise 35 Solution and Explanation*

# import unittest
# import math 

# pi = math.pi

# def area_circle(radius):
#     if type(radius) not in [int,float]:
#         raise TypeError("Radius must be a positive, whole number.")
#     elif radius < 0:
#         raise ValueError("The radius cannot be negative.")
#     return pi*(radius**2)

# print(area_circle(10))

# class TestAreaCircle(unittest.TestCase):
#     def test_area(self):
#         # Test the areas where the radius is >= 0
#         self.assertAlmostEqual(area_circle(1), pi)
#         self.assertAlmostEqual(area_circle(0), 0)
#         self.assertAlmostEqual(area_circle(2.1), pi * 2.1**2)
#     def test_values(self):
#         # Make sure that the value errors are raised when necessary
#         self.assertRaises(ValueError,area_circle,-2)
#     def test_types(self):
#         # Make sure type errors are raised when necessary
#         self.assertRaises(TypeError, area_circle, 3+5j) 
#         self.assertRaises(TypeError, area_circle, True)
#         self.assertRaises(TypeError, area_circle, "radius")





# # *Exercise 36 Solution and Explanation*


# def createSequence():
    
#     try:
#         MIN = int(input('What number would you like to start the sequence? '))
#         MAX = int(input('What number would you like to end the sequence? This number must be larger than the number previously entered. '))
#         while MIN <= MAX:
#             print(MIN)
#             MIN += 1
#     except ValueError:
#         print("Invalid entry.")

# createSequence()






# # *Exercise 37 Solution and Explanation*

# numList = [-15, 1, 5, 9, 8, -78, 86, -4, -1, 0]
# posnum = [num for num in numList if num > 0]

# print(posnum)




# # *Exercise 38 Solution and Explanation*

# numList = [1, 2, 3, 4, 5]
# result = [num * 3 for num in numList]

# print(result)




# # *Exercise 39 Solution and Explanation*

# txt = "This is the final small problem for the sequence homework "
# reverse = ""
# for char in txt:
#     reverse = char + reverse
# print(reverse)





# # *Exercise 40 Solution and Explanation*
# Multiply Vectors

# a_vector = [2, 4, 5] 
# b_vector = [2, 3, 6]
# c_vector = []

# for i in range(0, len(b_vector)):
#     c_vector.append(a_vector[i] * b_vector[i])
# print(c_vector)




# # *Exercise 41 Solution and Explanation*

# a = [[1, 2], [3, 4]]
# b = [[5, 6], [7, 8]]
# c = []
# for i in range(0, 2):
#     for x in range(0, 2):
#         c.append(a[i][x] + b[i][x])
# print(c)




# # *Exercise 42 Solution and Explanation*


# a = [[1, 2, 3], [9, 10, 11], [16, 17, 18]]
# b = [[5, 6, 7], [13, 14, 15], [19, 20, 21]]
# c = []
# for i in range(0, len(a)):
#     for x in range(0, len(b)):
#         c.append(a[i][x] + b[i][x])
        
# print(c)




