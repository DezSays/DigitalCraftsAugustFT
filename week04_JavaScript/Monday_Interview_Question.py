# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if: Open brackets must be closed by the same type of brackets. Open brackets must be closed in the correct order. Example 1: Input: s = "()" Output: true Example 2: Input: s = "()[]{}" Output: true Example 3: Input: s = "(]" Output: false

def isValid(text: str) -> bool:
    
    openingCharacter = []
    
    for value in text:                          # Loop for each character of the string
        
        if value in ['(', '{', '[']:            # If the opening symbol is encountered
            
            openingCharacter.append(value)      # If opening character is found, add it to our list
            
        elif value == ')' and len(openingCharacter) != 0 and openingCharacter[-1] == '(':       # If closing symbol is encountered and there is an opening character in the list and the last character in our openingCharacter list is the closing ')'
            
            openingCharacter.pop()              # If the above is true then remove them from the list, repeat this logic below but with curly braces and brackets
            
        elif value == '}' and len(openingCharacter) != 0 and openingCharacter[-1] == '{':
            
            openingCharacter.pop()
            
        elif value == ']' and len(openingCharacter) != 0 and openingCharacter[-1] == '[':
            
            openingCharacter.pop()
            
        else:                                   # If the list has something it has not removed, then we want to return false
            
            return False
        
    return openingCharacter == []               # We then return our openingCharacter list. If it is empty, then it will return true, if it has something in it then it will return false. 

print(isValid("(()[()]{})"))                    # Call our function and pass in our string