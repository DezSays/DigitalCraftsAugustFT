# What is a function? A function is a reusable block of code that can be called at any time. In order to call a function in python, we have to start with def. def just stands for definition. The user will need to pass in a parameter. See example below:

# The parameter is a variable that a function takes in.
name = input("What is your name? ")

# userName in thie case is a parameter. The computer takes the arguement that is passed in by the functino caller and stores the value that is saved within the variable userName in this case. 
def sayHowdy(userName):
    print('Howdy', userName)

# Any time you write a function, you must call it and pass in the argument (in this case, name) as shown below. 
sayHowdy(name)


# Example 2 of a function is below. If a function only takes one parameter, you cannot pass more than one parameter to it. The function above could not accept two arguments, but the below function can:

firstName = input("What is your first name? ")
lastName = input("What is your last name? ")


def secondFunction(parameter1, parameter2):
    #print("Hey there", parameter1 + ' ' + parameter2) #This is one way to write it, where you are concatinating strings.
    print("Hey there", parameter1, parameter2) #This is another way to achieve printing your first and last name. 
    
secondFunction(firstName, lastName)

# Want your function to be printed more than one time? See the below example:
secondFunction(firstName, lastName)
secondFunction(firstName, lastName)
secondFunction(firstName, lastName)


# Calculate the area of a rectangle using a function and a variable:

# Function where we define that we expect an integer to be passed in
def area(length: int, width: int) -> int:
    return length * width
    
# Variable
area_of_rectangle = area(5,6)

# Print your results
print(area_of_rectangle)


# How to get the area of a circle:

def area_of_circle(radius):
    PI = 3.14
    return PI * radius**2 #this line could aso be written: return PI * pow(radius, 2)

circle_area = area_of_circle(10)
print(circle_area)


# Function example:

def wearSweater() -> None:
    
    temp = int(input("What is the temp outside? "))
    humidity = int(input("What is the humidity? "))
    windSpeed = int(input("What is the wind speed? "))
    
    wearSweater = False
    
    if temp < 55:
        wearSweater = True
    elif temp >= 55 and temp < 65 and humidity <30:
        wearSweater = True
    elif temp < 60 and windSpeed > 10:
        wearSweater = True 
    return wearSweater

print(wearSweater())


# When to use a function within a function. See below:

def orderFlooring(orderNumber: int, length: int, width: int) -> int:
    if orderNumber <= 0:
        print("Invalid order number")
    amount_of_flooring = area(length, width) #this area function is the one we used above to find the area of a rectangle.
    return amount_of_flooring

print("You ordered", orderFlooring(101, 20, 15), "sqft of flooring")


# Dictionaries

students = {
    "id": 12345,
    "name": "Dez",
    "class" : "Senior",
    "GPA" : 3.65
}

print(students["name"])

pet1 = {
    "id": 47000,
    "name": "Mister Meseeks",
    "pet" : "rabbit",
    "status" : "alive"
}

pet2 = {
    "id": 50000,
    "name": "Toru",
    "pet" : "cat",
    "status" : "deceased"
}

pet3 = {
    "id": 53000,
    "name": "Doug",
    "pet" : "dog",
    "status" : "alive"
}

pet_list = [pet1,pet2,pet3]
print(pet_list)

# What if you wanted to print the name of pet2? See example below 
print(pet_list[1]["name"])




def listReturn(dcList: list) -> list:
    newList = []
    for x in dcList:
        y = int(x["id"])
        if(y <= 50000):
            newList.append(x)
    return newList

print(listReturn(pet_list))

