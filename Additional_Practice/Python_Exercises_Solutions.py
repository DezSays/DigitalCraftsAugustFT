
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

