# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications: Mat size must be X. ( is an odd natural number, and is times .) The design should have 'WELCOME' written in the center. The design pattern should only use |, . and - characters. Constraints 5 < N < 101 15 < M < 303

def make_pattern(n,m):

    count = int(n/2)
    top_text = ""
    pattern = '|..'
    full_line = ""
    half_line = "."
    
    if n < 5 or n > 101 or m < 15 or m > 303:
        return (f'Your first value must be between 5 and 101, and your second value must be between 15 and 303. You entered {n} as your first value and {m} as your second value.')

    for i in range(count):
            
        if i == 0:
            full_line = ".|.".center(m,'-') + "\n"
            
        else:
            half_line = '.'+(i * pattern)
            text = half_line + "|" + (half_line[::-1])
            full_line = text.center(m,'-')  + "\n"
            
        top_text += full_line
        
    result = top_text + 'WELCOME'.center(m,'-') + (top_text[::-1])
    
    return result

print(make_pattern(9,27))