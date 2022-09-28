# Given an array, write a function that sorts all names in reverse from Z-A. Write a unit test using the names of every student in this class to verify your solution.

import unittest

arr = ['Dezarea', 'Dre', 'Khanh', 'Jorge', 'Matt', 'Jordan', 'Jonathan', 'Carlos', 'Wes', 'Fiona', 'An']

def sortedNames(arr):
    for i in range(0, len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j].lower() < arr[j+1].lower():
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr 

print(sortedNames(arr))

class TestSortedNames(unittest.TestCase):
    def testSortClass(self):
        self.assertEqual(sortedNames(['Dezarea', 'Dre', 'Khanh', 'Jorge', 'Matt', 'Jordan', 'Jonathan', 'Carlos', 'Wes', 'Fiona', 'An']), ['Wes', 'Matt', 'Khanh', 'Jorge', 'Jordan', 'Jonathan', 'Fiona', 'Dre', 'Dezarea', 'Carlos', 'An'])
    def testSameFirstLetter(self):
        self.assertEqual(sortedNames(['Dez', 'Dre', 'Dan']),['Dre', 'Dez', 'Dan'])
    def testUpperAndLowerCase(self):
        self.assertEqual(sortedNames(['DEZ', 'dre', 'dAN']), ['dre', 'DEZ', 'dAN'])
    def testSimilarNames(self):
        self.assertEqual(sortedNames(['Dez', 'Dezi', 'Dezarea']), ['Dezi', 'Dezarea', 'Dez'])




unittest.main()