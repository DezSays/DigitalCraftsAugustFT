# Given an array containing None values fill in the None values with most recent value
# Ex: [1,2, None] -> [1,2,2]
# In python, write a function that takes in an array and returns the new array

numsList = [1,2,None]

def newArr(numsList):
    val = 0
    newList = []
    for i in numsList:
        if i is not None:
            newList.append(i)
            val = i
        else:
            newList.append(val)
    return newList


print(newArr(numsList))


