# Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.
# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1
# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0


def minSubArrayLen(target, nums):
    # increase window until meet or exceed target
    l = 0
    total = 0
    minLen = float("inf")
    for r in range(len(nums)):
        total += nums[r]
        while total - target >= nums[l]:
            total -= nums[l]
            l += 1
        if total >= target:
            minLen = min(minLen, r - l + 1)
    return minLen if minLen != float("inf") else 0


# print(minSubArrayLen(7, [2,3,1,2,4,3]))
print(minSubArrayLen(4, [1, 4, 4]))
# print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
# print(minSubArrayLen(7, []))

# if exceed target by more than or equal to nums[l]
# move left pointer

# move left pointer
