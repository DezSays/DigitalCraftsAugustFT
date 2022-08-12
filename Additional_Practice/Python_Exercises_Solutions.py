
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

