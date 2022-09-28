# You ask one of your developers to write a code that will give you the area of a circle. The code the developer writes for you is listed below. Write unit tests to test the following criteria:
# * Test area when radius is >= 0
# * Test that value errors are raised when necessary
# * Test that type errors are raised when necessary
# * Once you have completed the above steps, edit the code below to correct any errors that might occur. 

#  import math 
#  pi = math.pi

#  def area_circle(radius):
#      return pi*(radius**2)

#  print(area_circle(10))



import unittest                                 # bring in the unit test library
import math                                     # bring in the math library

pi = math.pi                                    # assign the variable pi to math.pi so we don't have to write math.pi every time

def area_circle(radius: int):                   # set up function to take in one int as a parameter
    if type(radius) not in [int,float]:         # if what was passed in was not a number
        raise TypeError("Radius must be a positive, whole number.") # raise a type error to let them know what we are expecting
    elif radius < 0:                            # if a negative number is entered as the radius
        raise ValueError("The radius cannot be negative.")  # then raise a value error to let them know that the radius cannot be negative
    return pi*(radius**2)                       # return the radius

print(area_circle(-8))                          # print out your function

class TestAreaCircle(unittest.TestCase):
    def test_area(self):
        # Test the areas where the radius is >= 0
        self.assertAlmostEqual(area_circle(1), pi)
        self.assertAlmostEqual(area_circle(0), 0)
        self.assertAlmostEqual(area_circle(2.1), pi * 2.1**2)
    def test_values(self):
        # Make sure that the value errors are raised when necessary
        self.assertRaises(ValueError,area_circle,-2)
    def test_types(self):
        # Make sure type errors are raised when necessary
        self.assertRaises(TypeError, area_circle, 3+5j) 
        self.assertRaises(TypeError, area_circle, True)
        self.assertRaises(TypeError, area_circle, "radius")
    

unittest.main()
