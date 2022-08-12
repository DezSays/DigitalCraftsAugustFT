# Without using the built in python library, sort an array of integers from least to greatest. To see a list of what not to use, see here: https://docs.python.org/3/library/functions.html

sample = [423, 53123, 5, 892, 94, 23453, 75, 2725, 64, 904] # Unsorted list
new_order = []                                              # Empty list where we will place our sorted numbers

def number_order(list: list) -> list: # Set up our function
    while sample:                     # This states that as long as something is in our sample list, it will keep looping through the values
        min_number = sample[0]        # We are going to assign the value of what is in index 0 from our sample list to the variable min_number
        for num in sample:            # Setting up a for loop to run through each number in the sample list 
            if num <= min_number:     # If the number in sample is less than or equal to the number in the first position of our sample list, 
                min_number = num      # The min_number variable is reassigned to the number that was found to be smaller in the previous line. 
        new_order.append(min_number)  # We add the new found minimum number to our new list
        sample.remove(min_number)     # We have to remove the minimum number from our sample list, else we will find ourselves in an endless loop.
    print(new_order)                  # Print out your new list

number_order(sample)                  # Call our function and pass in the unsorted list.

