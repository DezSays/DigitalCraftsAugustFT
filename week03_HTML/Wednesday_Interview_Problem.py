import unittest
 
# To solve this, we will follow these steps −

# alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# setFunction = a new set
# for each word in words, do
# blankString:= blank string
# for each letter in word, do
# blankString := blankString + alphabet[order of letter - 97]
# add blankString into setFunction
# return size of setFunction



testList = ["gin", "zen", "gig", "msg"]

def theEnigma(words:list) -> int:
    alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."];
    setFunction=set();
    for word in words:
        blankString = ''
        for letter in word:
            blankString += alphabet[ord(letter)-97]
        setFunction.add(blankString)
    return len(setFunction)

print(theEnigma(testList))



class TestEnigma(unittest.TestCase):

    def testTheEnigma(self):
        self.assertEqual(theEnigma(testList), 2)

unittest.main()
