# Delta Simulator

# Delta has not paid their pilots and are now experiencing delays nationwide. Due to this, they now need an algorithm to kick people off of planes while maintaining a passing happiness score. If a passing happiness score is not possible, maximize the happiness score the best you can. 

# First Class
    # 80% chance of leaving a negative review on Google
    # 50% chance of refusing to move
    # 1% chance of punching the flight attendant in the face
    
# Business Class
    # 70% chance of leaving a negative review on Google
    # 30% chance of refusing to move
    # 2% chance of punching the flight attendant in the face
    
# Comfort+ 
    # 50% chance of leaving a negative review on Google
    # 20% chance of refusing to move
    # 5% chance of punching the flight attendant in the face
    
# Economy
    # 10% chance of leaving a negative review on Google
    # 10% chance of refusing to move
    # 15% chance of punching the flight attendant in the face
        # Special Ability
            # If a passenger decides to Chuck Norris the flight attendant, 5% chance the attendant is KO'd, resulting in the entire flight being 


col = ['A', 'B', 'C', 'D']
row = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
  
string_row = [str(int) for int in row]
string_col = [str(int) for int in col]



str_of_row = ",".join(string_row)
str_of_col = ",".join(string_col)

newList = [f'{str_of_row}, {str_of_col}']


print(newList)