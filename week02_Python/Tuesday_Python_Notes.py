# Palindrome exercise

# num = input('Enter a number : ')
# try:
#    inputNumber = int(num)
#    if num == str(num)[::-1]:
#       print('This number is a palindrome')
#    else:
#       print('This number is not a palindrome')
# except ValueError:
#    print("The character entered was not a valid number")
   
# Matrices
matrix = [[1,2,3], [4,5,6], [7,8,9]]

# Below will print the numbers in order, one on each line:
# for rows in range(len(matrix)):
#       for cols in range(len(matrix[rows])):
#             print(matrix[rows][cols])
        
# Lets print out the content of the matrix backwards using a for loop:
# for rows in range(len(matrix)-1,-1,-1):
#        for cols in range(len(matrix[rows])-1,-1,-1):
#               print(matrix[rows][cols])

# Lets print out the content of a matrix backwards using a while loop:
rows = len(matrix)-1
cols = len(matrix[rows])-1

while rows >= 0:
      # print('rows: %i' % rows)
      cols = len(matrix[rows])-1
      while cols >= 0:
            print(matrix[rows][cols])
            cols -= 1
      rows -= 1
          
