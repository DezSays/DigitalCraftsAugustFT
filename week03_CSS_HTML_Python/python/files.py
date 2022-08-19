# How to create a file via Python
# W creates a file if the file doesn't already exist
file = open('newFile.txt', 'w')


# To write to a file:
file.write("Good morning, it's Friday!\n")

# Make sure to close it
file.close()

# Reopen the file so we can read it
# r means to read the file
file = open('newFile.txt', 'r')

# To read a file and show it on the screen:
print(file.read())

# Make sure to always close out before moving on
file.close()

# Modify a file after you have created it
# a means that we are going to append the new data to the end of the file
file = open('newFile.txt', 'a')

# Write your new message
file.write('Hope yall enjoy your weekend!\n')

# Never forget to close it out when you're done!
file.close()

# Read our changes
file = open('newFile.txt', 'r')
print(file.read())

# As always, remember to close when done
file.close()


# What if you wanted to overwrite a file? Notice that using w will delete previous contents of the file.
file = open('newFile.txt', 'w')
file.write('We will be learning about bootstrap today')
file.close()

file = open('newFile.txt', 'r')
print(file.read())
file.close()