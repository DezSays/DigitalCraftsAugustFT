# Class Review

# * PROMPT 1 - Week 2

# Write a short program that prints each number from 1 to 100 on a new line. 
#  For each multiple of 3, print "Fizz" instead of the number. 
# For each multiple of 5, print "Buzz" instead of the number. 
# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
# Write a unit test to ensure your solution works


# * SOLUTION 1

# import unittest

# def fizz(number):

#         if number % 15 == 0:
#             return 'FizzBuzz' 
#         elif number % 5 == 0:
#             return 'Buzz' 
#         elif number % 3 == 0:
#             return 'Fizz' 
#         else:
#             return number 
    
# for number in range(1,101):
#     print(fizz(number))
        
# class TestFizz(unittest.TestCase):
#     def testFizz(self):
#         self.assertEqual(fizz(3), 'Fizz')
#     def testFizzBuzz(self):
#         self.assertEqual(fizz(15), 'FizzBuzz')
#     def testBuzz(self):
#         self.assertEqual(fizz(5), 'Buzz')
        
# unittest.main()

# * PROMPT 2 - Week 3

# https://flexboxfroggy.com/

# * PROMPT 3 - Week 3

# http://www.flexboxdefense.com/