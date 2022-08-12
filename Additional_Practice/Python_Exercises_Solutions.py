
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




# *Exercise 2 Solution*

# previous_num = 0                            # Set up the initial value of the previous number globally. 

# for current_num in range(1, 11):            # Set up your for loop from 1 to 10
#     sum_value = previous_num + current_num  # Assign the previous number plus the current number to the variable sum_value
#     print("Current Number:", current_num, "Previous Number:", previous_num, " Sum:", previous_num + current_num) 
#     # Modify the previous number variable by setting it to the current number variable each time it iterates through the loop
#     previous_num = current_num
    
    
    
    
# *Exercise 3 PART 1 Solution*

# name = input("What is your name: ")                                 # Have the user enter their name
# age = int(input("How old will you be by the end of this year: "))   # Have the user enter how old they will be by the end of this year
# current_year = int(input("What is the current year: "))             # Have the user input the current year
# year = current_year - age + 100                                     # Take the current year, subtract the users age, and add 100 then assign this to a variable labeled year. 
# print(name + " will be 100 years old in " + str(year))              #Print out the users name and convert the year to a string so that you can concatenate everything as a string. 
    
    
    
    
# *Exercise 3 PART 2 Solution*

# name = input("What is your name: ")                                 # Have the user enter their name
# age = int(input("How old will you be by the end of this year: "))   # Have the user enter how old they will be by the end of this year
# current_year = int(input("What is the current year: "))             # Have the user input the current year
# year = current_year - age + 100                                     # Take the current year, subtract the users age, and add 100 then assign this to a variable labeled year. 
# print(f'{name} will be 100 years old in {year}')              #Print out the users name and year they will turn one hundred by using an f string, which allows you to combine different data types.





# *Exercise 4 Solution*
num = int(input("What number would you like to enter: ")) # Get the user to input a number, and use the int function to convert their input into an integer instead of a string.

def even_or_odd(number: int) -> int:        # Create a function that takes in one parameter, an integer
    if number % 2 == 0:                     # Set up if statement to see if the number entered could be divided by two with a remainder of 0.
        print('Even number')                # If the remainder is 0, print even number. 
    else:                                   # If there is a remainder,
        print('Odd number')                 # Print out odd number 
        
even_or_odd(num)                            # Call the function and pass in the variable used for the number given to us by the user.