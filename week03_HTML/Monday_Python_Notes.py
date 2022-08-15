# Given a list of numbers, write a function that tallies the number of even and add occurrences and returns the result. Write a unit test to prove your function works.

import unittest 

nums = [1,2,3,4,5,6,7,8,9,10]
def even_or_odd(nums:list) -> int:
    even_count = 0
    odd_count = 0
    for numbers in nums:
        if numbers % 2 == 0:
            even_count = even_count + 1
        elif numbers % 2 !=0:
            odd_count = odd_count + 1
    print(f"Even: {even_count}, Odd: {odd_count}")

    
even_or_odd(nums)
    


class TestNums(unittest.TestCase):

    def test_even_or_odd(self):
        self.assertEqual(even_or_odd(nums), None)

unittest.main()

    
