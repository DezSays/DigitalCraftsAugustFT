
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

previous_num = 0        # Set up the initial value of the previous number globally. 

for current_num in range(1, 11):  # Set up your for loop from 1 to 10
    sum_value = previous_num + current_num
    print("Current Number:", current_num, "Previous Number:", previous_num, " Sum:", previous_num + current_num)
    # modify previous number
    # set it to the current number
    previous_num = current_num