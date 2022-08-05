# Given a height and width, input by the user, print a box consisting of * characters as its border. 




# There are multiple ways to solve this problem. This is my solution. 


# def print_square(first_param, second_param) :
	
# 	for row in range(1, first_param+1) :
# 		for col in range(1, second_param+1) :
# 			if (row == 1 or row == first_param or
# 				col == 1 or col == second_param) :
# 				print("*", end="")		
# 			else :
# 				print(" ", end="")		
		
# 		print()


# rows = int(input("How many stars would you like in a row? "))
# columns = int(input("How many stars would you like in a column? "))
# print_square(rows, columns)




# Below is Carlos's solution, the community favorite:


# widthInput = int(input('Width? '))
# heightInput = int(input('Height? '))
# lineSequence = ''
# i = 0
# while i < heightInput:
#     j = 0
#     while j < widthInput:
#         if i == 0 or i == heightInput-1:
#             lineSequence = lineSequence + '*'
#         elif j == 0 or j == widthInput-1:
#             lineSequence = lineSequence + '*'
#         else:
#             lineSequence = lineSequence + ' '
#         j = j+1
#     i = i+1
#     print(lineSequence)
#     lineSequence = ''
    
    
    
    
# Below is Matt's solution, which allows for error catching:


#starts loop
# while True:
#     #attempt to retrieve integer
#     try:
#         #prompts user for width and passes to integer
#         width = int(input('Width: '))
#     #catches invalid entries
#     except ValueError:
#         #error message
#         print('Invalid. Please enter a number.')
#         #continues loop
#         continue
#     #checks that there is a positive value that caps at 15
#     if width <= 15 and width > 1:
#         #ends loop
#         break
#     elif width <= 1:
#         print('Invalid (MIN 2)')
#         continue
#     else:
#         print('Invalid (MAX 15)')
#         continue
   
# #starts loop
# while True:
#     #attempt to retrieve integer
#     try:
#         #prompts user for height and passes to integer
#         height = int(input('Height: '))
#     #catches invalid entries
#     except ValueError:
#         #error message
#         print('Invalid. Please enter a number.')
#         #continues loop
#         continue
#     if height <= 15 and height > 1:
#         #ends loop
#         break
#     elif height <= 1:
#         print('Invalid (MIN 2)')
#         continue
#     else:
#         print('Invalid (MAX 15)')
#         continue

# #sets a counting variable
# count = 0
# #sets row as an empty string
# row = ''
# #sets * to variable to fill in borders
# dot = '* '

# #creates top and bottom rows
# while count < width:
#     row = row + dot
#     count += 1

# #sets first count variable
# count1 = 0
# #prints top row
# print(row)
# #uses count to determine amount of middle rows
# while count1 < height - 2:
#     #resets second count with each row
#     count2 = 0
#     #adds a * to first index in string
#     middleRows = dot
#     #adds empty spaces for each row
#     while count2 < width - 2:
#         middleRows = middleRows + '  '
#         count2 += 1
#     #adds closing *
#     middleRows = middleRows + dot
#     #prints the new string
#     print(middleRows)
#     count1 += 1
# #prints bottom row
# print(row)