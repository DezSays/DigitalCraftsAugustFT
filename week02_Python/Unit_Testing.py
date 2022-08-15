import unittest

def rectangleArea(length: int, width: int) -> int:
        # Returns the value back to the caller
        return length * width


# Calculates the area of a circle
def circleArea(radius: int) -> int:
    PI = 3.14
    return PI * pow(radius, 2)

class TestAreas(unittest.TestCase):

    # Test a 3 x 3 rectangle
    def testRectangleArea(self):
        self.assertEqual(rectangleArea(3, 3), 9)

    # Test a circle with a radius a 5
    def testCircleArea(self):
        self.assertEqual(circleArea(5), 78.5)


unittest.main()
