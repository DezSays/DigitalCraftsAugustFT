# Write a short program that prints each number from 1 to 100 on a new line. 
# For each multiple of 3, print "Fizz" instead of the number. 
# For each multiple of 5, print "Buzz" instead of the number. 
# For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.

for number in range(1,101):
    if number % 15 == 0:
        print('FizzBuzz')
    elif number % 5 == 0:
        print('Buzz')
    elif number % 3 == 0:
        print('Fizz')
    else:
        print(number)

# Reversing a simple string:
sample = 'Hello world'
print(sample[::-1])

# Reversing a list:
sampleList = ['first', 'second', 'third']

print(sampleList[::-1]) #this is how you print using slice. This is exclusive to Python, but is by far the simplest way to reverse.

# Below is how you would reverse the list using a while loop:
newList=[]
# While loop example 1

words = len(sampleList) - 1
while words >= 0:
    newList.append(sampleList[words])
    words = words - 1
print(newList)

# While loop example 2
while len(sampleList) > 0:
    number = sampleList.pop()
    newList.append(number)
print(newList)