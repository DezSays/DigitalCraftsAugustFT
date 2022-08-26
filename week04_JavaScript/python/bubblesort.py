def bubblesort(nums: list) -> list:
    for i in range(len(nums)): # Iterating from front to back of the list
        # Since the last index traversed in the previous iteration will always be the largest value, decrease the number of indices traversed by 1
        # With a list length 5, in the 1st iteration we traverse 5 indices, then in the 2nd iter, 4 indices, 3rd iter we will traverse 3 indices, etc.
        for currentIndex in range(0, len(nums) - i - 1): 
            # Checking if the next index is greater than the current index
            if nums[currentIndex] > nums[currentIndex + 1]:
                # Swap the values if true
                nums[currentIndex], nums[currentIndex + 1] = nums[currentIndex + 1], nums[currentIndex]
    return nums

numbers = [678, 7890, 456, 23345, 6789, 5623]
print(bubblesort(numbers))