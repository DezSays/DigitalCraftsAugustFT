# *PROMPT*
# Write a function in python, that takes 2 files as parameters and returns a list of the numbers that exist in both files. Using the two files provided, write a unit test to verify your answer.

import unittest 

fileA = open("text1.txt","r")           # Set file = open('name-of-file.filetype', and here we have r to assign the read command)
fileB = open("text2.txt", "r")          # Set file = open('name-of-file.filetype', and here we have r to assign the read command)
    

firstText = fileA.read()
secondText = fileB.read()


def count_nums(fileA, fileB):               # Set up our function

    dupList = []                            # set up our empty list
    
    num1 = firstText.split()                # Assign the variable num1 = the reading of our file and 'split' the numbers so we can count the numbers (like 13) as 13 instead of 1 and 3.
    num2 = secondText.split()               # Assign the variable num2 = the reading of our file and 'split' the numbers so we can count the numbers (like 13) as 13 instead of 1 and 3.
    
    for num in num1:                        # for each number in the first list
        for val in num2:                    # for each number in the second list
            if num == val:                  # if the same number is found in both
                dupList.append(num)         # then append it to the list
            else:                           # otherwise
                continue                    # continue through the loop until all numbers have been checked
    print(f"Duplicate Numbers: {dupList}")  # Print out the amount of numbers that are duplicated by printing our dupList variable
    return dupList                          # returning the duplist, even if it is empty

    

count_nums(fileA, fileB)        # Call our function

fileA.close()                   # Always remember to close your files so you don't have a data leak!
fileB.close()                   # Always remember to close your files so you don't have a data leak!



class Tests(unittest.TestCase):

    def testCountNums(self):
        self.assertListEqual(count_nums("text1.txt", "text2.txt"), ['7', '13', '19', '23', '31', '79', '97', '103', '109', '139', '167', '193', '239', '263', '293', '313', '331', '367', '379', '383', '397', '409', '487', '563', '617', '653', '673', '683', '709', '739', '761', '863', '881', '907', '937'])

    


unittest.main()