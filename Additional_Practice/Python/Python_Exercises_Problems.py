
#*Exercise 1: Calculate the multiplication and sum of two numbers. Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.*

# Part 1 Values:

# number1 = 20
# number2 = 30
# Expected Output: The result is 600

# Part 2 Values:
    
# number1 = 40
# number2 = 30
# Expected Output: The result is 70




#*Exercise 2: Print the sum of the current number and the previous number. Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.*

# Expected Output:

# Current Number 1 Previous Number  0  Sum:  1
# Current Number 2 Previous Number  1  Sum:  3
# Current Number 3 Previous Number  2  Sum:  5
# Current Number 4 Previous Number  3  Sum:  7
# Current Number 5 Previous Number  4  Sum:  9
# Current Number 6 Previous Number  5  Sum:  11
# Current Number 7 Previous Number  6  Sum:  13
# Current Number 8 Previous Number  7  Sum:  15
# Current Number 9 Previous Number  8  Sum:  17





#*Exercise 3 PART 1: Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Concatenate strings to print the resulting output message. *

# Expected Output:

# Dezarea will be 100 years old in 2095.





#*Exercise 3 PART 2: Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old, except use f-strings instead of the + operator to print the resulting output message. *

# Expected Output:

# Dezarea will be 100 years old in 2095.






# *Exercise 4: Ask the user for a number. Depending on whether the number is even or odd, print out an even or odd message to the user. *

# Expected Output (if even number):

# Even Number



# Expected Output (if odd number):

# Odd Number





# *Exercise 5: Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function. *

# Expected Output

# [5, 25]





# *Exercise 6: Print characters from a string that are present at an even index number. Write a program to accept a string from the user and display characters that are present at an even index number. *


# Expected Output if the original string was dezarea:
# d
# z
# r
# a



# *Exercise 7: Write a program to remove characters from a string starting from zero up to x and return a new string. 

# For example:

# remove_chars("dezbryan", 4) so output must be ryan. Here we need to remove first four characters from a string.
# remove_chars("dezbryan", 2) so output must be zbryan. Here we need to remove first two characters from a string.
# Note: x must be less than the length of the string.



# * Exercise 8: Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.*

# For example:

# x: [10, 20, 30, 40, 10]
# True

# y = [75, 65, 35, 75, 30]
# False



#  * Exercise 9: Iterate the given list of numbers and return to a new list only those numbers which are divisible by 5 *

# For example: 

# list =  [10, 20, 33, 46, 55]
# Divisible by 5, output will be
# [10, 20, 55]



#  * Exercise 10: Write a program to find how many times substring “Dez” appears in the given string. *

# x = "Dez is good developer. Dez is a turkey."

# Expected Output:

# 2



#  * Exercise 11: Print the following pattern *

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 



#  * Exercise 12: Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list. *

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]

# Expected Output:

# [25, 35, 40, 60, 90]



#  * Exercise 13: Write a Program to extract each digit from an integer in the reverse order. *

# For example: 
    
# If the given int is 7536, the output is “6357“.



#  * Exercise 14: Print multiplication table from 1 to 10. *

# Expected Output:

# 1  2 3 4 5 6 7 8 9 10 		
# 2  4 6 8 10 12 14 16 18 20 		
# 3  6 9 12 15 18 21 24 27 30 		
# 4  8 12 16 20 24 28 32 36 40 		
# 5  10 15 20 25 30 35 40 45 50 		
# 6  12 18 24 30 36 42 48 54 60 		
# 7  14 21 28 35 42 49 56 63 70 		
# 8  16 24 32 40 48 56 64 72 80 		
# 9  18 27 36 45 54 63 72 81 90 		
# 10 20 30 40 50 60 70 80 90 100 



#  * Exercise 15: Print downward Half-Pyramid Pattern with Star (asterisk) *

# Expected Output:

# * * * * *  
# * * * *  
# * * *  
# * *  
# *



#  * Exercise 16: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exponent. *

# Expected output

# Example 1:

# base = 2
# exponent = 5

# 2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

# Example 2:

# base = 5
# exponent = 4

# 5 raises to the power of 4 is: 625 
# i.e. (5 *5 * 5 *5 = 625)



#  * Exercise 17: Using file handling, write a function in Python to count and display the total number of words in a text file. *

# Expected output if your document had 7 words:

# Total words are: 7



#  * Exercise 18: Using file handling, write a function in Python to read lines from a text file. Your function should find and display the occurrence of the word "the", both upper and lower case! *

# For example: If the content of the file is:

# "We will be learning about bootstrap today! This file will also be the file that is used for our additional practices. The individuals that do the extra practice are certainly going to benefit from putting in the extra work."

# The output should be 4. 




#  * Exercise 19: Using file handling, write a function to read lines from a text file and display those words which are less than 4 characters. *

# For example: If the content of the file is:

# "We will be learning about bootstrap today! This file will also be the file that is used for our additional practices. The individuals that do the extra practice are certainly going to benefit from putting in the extra work."

# The expected output should be: We be be the is for our The do the are to in the 




#  * Exercise 20: Using file handling, write a function to count the words "this" and "that" present in a text file. *

# For example: If the content of the file is:

# "We will be learning about bootstrap today! This file will also be the file that is used for our additional practices. The individuals that do the extra practice are certainly going to benefit from putting in the extra work."

# The expected output should be: 8




#  * Exercise 21: Using file handling, write a function to count words in a text file those are ending with letter "e". *

# For example: If the content of the file is:

# "We will be learning about bootstrap today! This file will also be the file that is used for our additional practices. The individuals that do the extra practice are certainly going to benefit from putting in the extra work."

# The expected output should be: 11




#  * Exercise 22: Using file handling, write a function to count uppercase character in a text file. *

# For example: If the content of the file is:

# "We will be learning about bootstrap today! This file will also be the file that is used for our additional practices. The individuals that do the extra practice are certainly going to benefit from putting in the extra work."

# The expected output should be: 3




#  * Exercise 23: The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in. *

# For example:

# sleep_in(False, False) → True
# sleep_in(True, False) → False
# sleep_in(False, True) → True




#  * Exercise 24: Imagine that we have two monkeys, and the parameters a_smile and b_smile indicate if each monkey is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble and False if we are in the clear. *

# For example:

# monkey_trouble(True, True) → True
# monkey_trouble(False, False) → True
# monkey_trouble(True, False) → False




#  * Exercise 25: Given a string, if the string length is less than 3, repeat the letters that are present three times. If the string length is more than three, return a new string whith the first three letters repeated. See the example below. *

# newStr3('Java') → 'JavJavJav'
# newStr3('Chocolate') → 'ChoChoCho'
# newStr3('ab') → 'ababab'




#  * Exercise 26: Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10. *

# makes10(9, 10) → True
# makes10(9, 9) → False
# makes10(1, 9) → True




#  * Exercise 27: Given two int values, return their sum. Unless the two values are the same, then return double their sum. *

# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8




#  * Exercise 28: Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative. See example below. *

# pos_neg(1, -1, False) → True
# pos_neg(-1, 1, False) → True
# pos_neg(-1, 1, True) → False
# pos_neg(-4, -5, True) → True




#  * Exercise 29: We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0 to 23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

# parrot_trouble(True, 6) → True
# parrot_trouble(True, 7) → False
# parrot_trouble(False, 6) → False




#  * Exercise 30: Given an int n, return True if it is within 10 of 100 or 200. *

# near_hundred(93) → True
# near_hundred(90) → True
# near_hundred(89) → False




#  * Exercise 31: Given an int n, return the difference between n and 21, except return double the difference if n is over 21.


# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0




#  * Exercise 32: Write a function that takes in three parameters (small, big, result). You have a number of small bricks, each having a length of 1 inch. You have a number of big bricks, each having a length of 5 inches. Result is the number of inches that we need to complete our project. Return True if it is possible to make the result by choosing from the given bricks. *


# build_house(3,1,8) -> True
# build_house(3,2,9) -> False
# build_house(3,2,10) -> True



# * Exercise 33: For this problem, round an integer up to the next multiple of 10 if the rightmost digit is 5 or more (so 15 would round up to 20). Alternatively, round down to the previous multiple of 10 if the rightmost digit is less than 5, so 14 rounds down to 10. Given three integers, (x,y,z), return the sum of their rounded values. * HINT * This problem is easier to solve if you have two functions: one function to round your numbers, one to produce your sum. *


# numSum(16,17,18) -> 60
# numSum(12,13,14) -> 30
# numSum(6,4,4) -> 10



# * Exercise 34: Write a function that asks the user to enter an integer and returns up to that number the fibonacci sequence. If the user enters unwanted characters (letters, symbols, etc.), return Invalid Entry. *

# Example:
# User input: 5
# Expected output:
# 0
# 1
# 1
# 2
# 3



# * Exercise 35: You ask one of your developers to write a code that will give you the area of a circle. The code the developer writes for you is listed below. Write unit tests to test the following criteria:
# * Test area when radius is >= 0
# * Test that value errors are raised when necessary
# * Test that type errors are raised when necessary
# * Once you have completed the above steps, edit the code below to correct any errors that might occur. 

# import math 
# pi = math.pi

# def area_circle(radius):
#     return pi*(radius**2)

# print(area_circle(10))



# * Exercise 36: Write a function that asks for the user to input two numbers, the first number is where the sequence will begin and the second number is where the sequence will end. The sequence must be in ascending order. 

# For example: 
# If the user give you the numbers 1, and 5, the expected output will be:
# 1
# 2
# 3
# 4
# 5 



# * Exercise 37: Create a list of numbers, create a new list which contains every number in the given list which is positive.



# * Exercise 38: Create a list of numbers, and a single factor (also a number), create a new list consisting of each of the numbers in the first list multiplied by the factor. Print this list.

# For example:
# numList = [1, 2, 3, 4, 5]

# Expected output:
# [3, 6, 9, 12, 15]



# * Exercise 39: Given a string, print the string reversed using a for loop.



# * Exercise 40: # Multiply Vectors

# For example:
# a_vector = [2, 4, 5] 
# b_vector = [2, 3, 6]

# Expected output:
# [4, 12, 30]
 


# * Exercise 41: Matrix Addition

# For example:
# a = [[1, 2], [3, 4]]
# b = [[5, 6], [7, 8]]

# Expected output:
# [6, 8, 10, 12]



# * Exercise 42: Multiple Matrix Addition. Add multiple matrices and combine them into one list. 

# For example:
# a = [[1, 2, 3], [9, 10, 11], [16, 17, 18]]
# b = [[5, 6, 7], [13, 14, 15], [19, 20, 21]]

# Expected output:
# [6, 8, 10, 22, 24, 26, 35, 37, 39]



# * Exercise 43: Given a non-negative number "num", return True if num is within 2 of a multiple of 10. 

# For example:
# near_ten(12) → True
# near_ten(17) → False
# near_ten(19) → True



# * Exercise 44: Given an array length 1 or more of integers, return the difference between the largest and smallest values in the array.  

# For example:
# big_diff([10,3,5,6]) → 7
# big_diff([10,7,2,9]) → 8
# big_diff([10,2,7,2]) → 8



# * Exercise 45: Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and the number that comes immediately after 13 does not count.

# For example:
# sum13([13,1,2,13,2,1,13]) → 3
# sum13([1,2,2,1,13]) → 6
# sum13([5,13,2]) → 5



# * Exercise 46: Return the number of even integers in the given array. Note: the % mod operator computes the remainder, e.g. 5 % 2 is 1.

# For example:
# count_evens([13,1,2,13,2,1,13]) → 3
# count_evens([1,2,2,1,13]) → 3
# count_evens([5,13,2]) → 0



# * Exercise 47: Return True if the string 'cat' and 'dog' appear the same number of times in the given string.

# For example:
# cat_dog("catdog") → True
# cat_dog("catcat") → False
# cat_dog("1cat1cadodog") → True
# *****************************************************************************************************



# * Exercise 48: Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper and lower case differences. 

# For example:
# ends('Testxyz', 'XyZ') → True
# ends('XyZ', 'TestxYZ') → True
# ends('XYZxyz', 'xyz') → True



# * Exercise 49: Given a string, return a string where every character is repeated.

# For example:
# doubleTrouble("Dez") → "DDeezz"
# doubleTrouble("DC-Students") → "DDCC--SSttuuddeennttss"
# doubleTrouble("YeeHaw") → "YYeeeeHHaaww"



# * Exercise 50: Given 2 strings, return a string of the form shortString + longString + shortString. 

# For example:
# tripleThreat("hey", "howdy") → "heyhowdyhey"
# tripleThreat("cat","x") → "xcatx"
# tripleThreat("wowza", "YEET") → "YEETwowzaYEET"



# * Exercise 51: Given a string, return a greeting in the form of "Hello given_string!"

# For example:
# howdy('Doug') → 'Hello Doug!'
# howdy('Toru') → 'Hello Toru!'
# howdy('Mister Meseeks') → 'Hello Mister Meseeks!'



# * Exercise 52: Given two strings, the first consisting of four characters, and the second consisting of a word, return a new string where the second string is in the middle of the first string.

# For example:
# new_word('<<>>', 'Sammich') → '<<Sammich>>'
# new_word('{{}}', 'Oh hi') → '{{Oh hi}}'
# new_word('*!!*', 'wowza') → '*!wowza!*'



# * Exercise 53: Given a string, return the string made of its first two characters. If the string is shorter than two characters, return whatever is there. 

# For example
# two('hello') → 'he'
# two('x') → 'x'
# two('') → ''



# * Exercise 54: The web is built with HTML strings like "<i>Dez</i>" which makes the word Dez italicized. Given a tag and a word , create the HTML string with tags around the word.

# For example
# tags('i', 'dez') → '<i>dez</i>'
# tags('a', 'link') → '<a>link</a>'
# tags('div', 'oh hi') → '<div>oh hi</div>'



# * Exercise 55: Given two strings, return the result of putting them together like this: first+second+second+first.

# For example
# wordSandwich('hey','howdy') → 'heyhowdyhowdyhey'
# wordSandwich('day','Night') → 'dayNightNightday'
# wordSandwich('Wowza','woohoo') → 'WowzawoohoowoohooWowza'



# * Exercise 56: Given three integer values, return their sum. However, if one of the values is 13 then it does not count toward the sum, and any values found to the right of the 13 do not count towards the sum either. 

# For example 
# unluckySum(1,2,3) → 6
# unluckySum(13,2,3) → 0
# unluckySum(1,13,3) → 1



# * Exercise 57: Given three integers, return their sum. However, if one of the values is the same as another value, then they do not count towards the sum.

# For example
# noDups(1,2,3) → 6
# noDups(3,2,3) → 2
# noDups(3,3,3) → 0



# * Exercise 58: Given an array of integers, return the number of 9's found in an array.

# For example
# be9([1,2,9]) → 1
# be9([1,9,9]) → 2
# be9([9,9,9,9,1,2,9]) → 5



# * Exercise 59: Given a string, return a new string made of every character that falls on an even index, starting at the beginning. 

# For example
# evenIndex('hello') → 'hlo'
# evenIndex('DougieDoo') → 'DuiDo'
# evenIndex('howdy') → 'h'



# * Exercise 60: Given a string and a positive integer (posNum), return the string posNum amount of times.

# For example
# stringMult('hello',3) → 'hellohellohello'
# stringMult('DougieDoo',2) → 'DougieDooDougieDoo'
# stringMult('howdy',1) → 'howdy'



# * Exercise 61: When squirrels get together for a party, they like to have nuts. A squirrel party is considered successfuly when the number of nuts is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of nuts. Return True if the party with the given values is successful, and return False otherwise. 

# For example
# squirrelParty(30,False) → False
# squirrelParty(50,False) → True
# squirrelParty(70,True) → True



# * Exercise 62: The number 7 is a lucky number. Given two integer values, a and b, return true if either one is seven, or if their sum or difference would equal 7. 

# For example
# lucky(3,4) → True
# lucky(5,4) → False
# lucky(7,1) → True



# * Exercise 63: You and your best friend are trying to find the right outfits for the fashion show. You are entering as a duo and will be receiving a final result of either 0, which means you do not get to be in the fashion show, 1, which means you will be an alternate should someone else drop out, or 2, which means you are in the fashion show! You and your best friend will each be scored on a scale from 0-10. If either of you recieves an 8, and the other has a score of at least 3, then you will both be going to the fashion show. If either of you recieves an 8, and the other has a score of 2 or less, then neither of you will be going to the fashion show. All other combinations will result in you being an alternate. Good luck! 

# For example
# fashionShow(5,10) → 2
# fashionShow(10,2) → 0
# fashionShow(5,5) → 1



# * Exercise 64: The squirrels spend most of the day playing. They will play as long as the temperature is between 60 and 90 degrees all year. If it is summer, they can play in 60-100 degree weather. Given an integer as the temperature, and boolean value on if it is summer or not, return True if the squirrels can go outside to play and False otherwise. 

# For example
# squirrelWeather(70, False) → True
# squirrelWeather(95, False) → False
# squirrelWeather(95, True) → True



# * Exercise 65: Given two integers, return their sum. However, if the sum would equal a number between 10-19, then just return the number 20. 

# For example
# sum20(3, 4) → 7
# sum20(9, 4) → 20
# sum20(10, 11) → 21
