#Problem: Find the missing number in an array of integers containing n-1 unique numbers in the range [1, n].
def findMissingNum(arr):
    n = len(arr) + 1   # add 1 to the length of the array to account for the missing number.
    expectedSum = n * (n + 1) / 2
    actualSum = sum(arr)
    return expectedSum - actualSum

print(findMissingNum([3, 4, -1, 1])) 


#Given an array of integers nums, return the first missing positive integer.
def firstMissingPositive(nums):
    n = len(nums)
    
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1
nums = [3, 4, -1, 1]
print(firstMissingPositive(nums)) 














