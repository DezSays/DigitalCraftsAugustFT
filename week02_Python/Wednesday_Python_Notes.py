# When given two strings from the user, write a function that checks if each string is an anagram of the other. If yes, return true, otherwise return false. 

# Get the users input so we know which two strings we will be comparing. **Note, this function will also work with numbers.
# str1 = input("Please enter the first word you would like to compare: ")
# str2 = input("Please enter the second word you would like to compare: ")

# Setup our function with two parameters
# def anagram(str1, str2):

# Set the strings to a list so that we will be able to sort them later, and set the user input to be lower case so capitalization shouldn't matter.
#   str1 = list(str1.lower())
#   str2 = list(str2.lower())

# Sort the lists we created above, so it will put the words in alphabetical order and be able to compare them easier
#   str1.sort()
#   str2.sort()

# Return the strings so they are directly compared against each other, which will result in a true/false result
#   return str1 == str2

# Print and call the function
# print(anagram(str1, str2))




# How would you sort two strings without using the sort method?

# solution 1

# str1 = input("Please enter the first word you would like to compare: ")
# str2 = input("Please enter the second word you would like to compare: ")

# def anagramNoSortMethod(str1, str2):
#     if len(str1) != len(str2):
#         return "False"
        
#     dict_str1 = {}
#     dict_str2 = {}
    
#     return "True" if dict_str1 == dict_str2 else "False"

# print(anagramNoSortMethod(str1, str2))







# solution 2

# word1 = input("Type a word: ")
# word2 = input("Type a word: ")
# def isAnagram(word1,word2):
#     dict1 = {}
#     dict2 = {}

#     for letter in word1:
#         if letter in dict1.keys():
#             dict1[letter] = dict1.get(letter) + 1
#         else:
#             dict1[letter] = 1
            

#     for letter in word2:
#         if letter in dict2.keys():
#             dict2[letter] = dict2.get(letter) + 1
#         else:
#             dict2[letter] = 1
            
#     return dict1 == dict2

# print(isAnagram(word1,word2))





# solution 3

# usersChoice1 = input("Type a word: ")
# usersChoice2 = input("Type a word: ")

# # Iterating through the first word
# def isAnagram(word1, word2):
#     # NEW: you can declare multiple variables on the same line using a comma
#     dict1 = {}
#     dict2 = {}
#     # Checking if the letter matches any of the keys in our dictionary, if so increment the count by 1
#     for letter in word1:
#         if letter in dict1.keys():
#             dict1[letter] = dict1.get(letter) + 1
#         # The letter is not in our dictionary, set count to 1
#         else:
#             dict1[letter] = 1
            
# # Building the dictionary of the second word
#     for letter in word2:
#         if letter in dict2.keys():
#             dict2[letter] = dict2.get(letter) + 1
#         else:
#             dict2[letter] = 1

#     return dict1 == dict2


# print(isAnagram(usersChoice1, usersChoice2))






# Create a list that holds the first name of everyone in this class, return any name that is duplicated



# Solution 1 

# students = ["Matt", "Wes", "Jorge", "Fiona", "Carlos", "An", "Jonathan", "Jordan", "Khanh", "Jordan"]

# def findDuplicateNames(students: list) -> list:
#     duplicateNames=[]
#     for name in students:
#         if name not in duplicateNames:
#             duplicateNames.append(name)
#         else:
#             print(name)

# findDuplicateNames(students)





# Solution 2

# def duplicateNames(students: list) -> list:
#     studentDict = {}
#     duplicateNames = []
#     # Iterate through the list of students 
#     for name in students:
#         # check if that students first name already appears in the list 
#         if name in studentDict.keys():
#             # Increment the number of times it appears in the dictionary if it is found
#             duplicateNames.append(name)
#         else:
#             # No duplicate names were fount, create a new key and set its value to one
#             studentDict[name] = 1
#     return duplicateNames
# print(duplicateNames(["Matt", "Wes", "Jorge", "Fiona", "Carlos", "An", "Jonathan", "Jordan", "Khanh", "Jordan"]))

