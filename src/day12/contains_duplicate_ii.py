# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:

# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:

# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

 
def two_distinct_vals(nums, k): 
    locs = {}
    for i, v in enumerate(nums):
        if v in locs and i - locs[v] <= k:
            return True
        locs[v] = i
    return False

nums1 = [1,2,3,1.........1] 
k1 = 3
print(two_distinct_vals(nums1, k1))

nums1 =  [1,0,1,1]
k1 = 1
print(two_distinct_vals(nums1, k1))

nums1 = [1,2,3,1,2,3]
k1 = 2
print(two_distinct_vals(nums1, k1))
