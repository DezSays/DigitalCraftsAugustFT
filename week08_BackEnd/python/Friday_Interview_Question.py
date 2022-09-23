# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications: Mat size must be X. ( is an odd natural number, and is 3x length .) The design should have 'WELCOME' written in the center. The design pattern should only use |, . and - characters. Constraints 5 < N < 101 15 < M < 303



def make_pattern(n,m):              # set up function to take in two integers as parameters


    count = int(n/2)                # set variable count to equal half of n, we want it split in half so that we can display the top and bottom of the pattern just using the slice method. 
    top = ""                        # set variable top to empty string
    pattern = '|..'                 # set variable pattern equal to the pattern we want repeated
    full_line = ""                  # set variable full line to an empty string
    half_line = "."                 # set variable half line to a period, this we will use in our pattern design
    
    if n < 5 or n > 101 or m < 15 or m > 303:           # if n or m is not within the given range
        return (f'Your first value must be between 5 and 101, and your second value must be between 15 and 303. You entered {n} as your first value and {m} as your second value.')           # return error message
    if m / n != 3:                                      # if n is not a third of m
        return(f'Your first value must be 1/3 of your second value. {n} is not 1/3 of {m}') # return error message
    for i in range(count):                              # for i in range of n/2
            
        if i == 0:                                      # if i is 0
            full_line = ".|.".center(m,'-') + "\n"      # change full line to hold ".|." pattern, and center(length being the second number passed in, '-' being the character that we need m amount of)
            
        else:
            half_line = '.'+(i * pattern)               # change half line to hold '.' plus the pattern reapeated i times
            text = half_line + "|" + (half_line[::-1])  # assign variable text to hold the half line pattern above, and add '|' to our pattern, then add the half-line split and get the end of the pattern added here. Essentially, adding '|' after our halfline plus the last character in half line.
            full_line = text.center(m,'-')  + "\n"      # change full line to hold the variable defined directly above, centered(length being the second number passed in, '-' being the character that we need m amount of)
            
        top += full_line                                # take the top variable, which was just an empty string, and add our full line variable which has been changed depending on if/else conditions.
        
    result = top + 'WELCOME'.center(m,'-') + (top[::-1])    # assign variable result to hold top, plus 'Welcome" which we want centered using our length, plus the top split. Basically, the top is repeated on top and on bottom and welcome is smack dab in the middle. 
    
    return result                                           # return the variable assigned above

print(make_pattern(9,27))                                   # print out function results









