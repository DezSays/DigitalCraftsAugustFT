# This method is known as bubble sort. It works good with small sets of data, but would not be good with large sets of data.

def sortList(sample: list) -> list:
    for num1 in range(0, len(sample)-1):
        for val in range(num1, len(sample)):
            if sample[val] < sample[num1]:
                temp = sample[val]
                sample[val] = sample[num1]
                sample[num1] = temp 
    print(sample)
    
sample = [23, 4, 12, 5, 64, 7, 89, 24, 14, 28, 17, 3, 2, 1]
sortList(sample)