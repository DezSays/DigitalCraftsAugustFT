# Given a file, write a function that swap all cases. All uppercase letters should become lower case and vice versa. Write unit tests to confirm 

import unittest

def swap():                                 #Set up our function
    file = open("stillIRise.txt","r")       #Set file = open('name-of-file.filetype', and here we have r to assign the read command)
    data = file.read()                      #Assign the variable data = reading our file
    words = data.split()                    #Assign the variable words = the reading of our file and 'split' the sentences so we can count the words instead of the letters
    for word in words:                      #For every word in our file
        newWord = word.swapcase()           #Use swapcase to change upper/lower case values in text
        print(newWord)                      #Print out the new upper and lower case words 
    file.close()                            #Always remember to close your files so you don't have a data leak!

swap()                                      #Call our function

# class Tests(unittest.TestCase):

#     def testSwap(self):
#         self.assertIsNot(,)
# unittest.main()