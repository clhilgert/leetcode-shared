# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all 
# the elements of nums except nums[i].

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
#for every number result is left * right
# for a number left is prev res * number befor

def productExceptSelf(nums):
    left, right, res = [0] * len(nums), [0] * len(nums), [0] * len(nums)
    total = 1
    for i in range(len(nums) - 1, -1, -1):
        right[i] = total
        total *= nums[i]
    total = 1
    for i in range(len(nums)):
        left[i] *= total
        total *= nums[i]
    for i in range(len(nums)):
        res[i] = left[i] * right[i]
    return res
