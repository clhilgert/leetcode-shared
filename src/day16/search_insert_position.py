# 35. Search Insert Position
# Solved
# Easy
# Topics
# Companies
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.


# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4


# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104
# Find the leftmost val that is >=target
# if u use List you need import yeah, can do this too


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        index = None

        while l < r:
            m = (l + r) // 2
            if nums[m] >= target:
                index = m
                r = m
            else:
                l = m + 1

        if l == len(nums) - 1:
            return len(nums)

        return index


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                r = m

            elif nums[m] < target:
                l = m + 1

            elif nums[m] > target:
                r = m

        return l


s = Solution()
print(s.searchInsert([1, 3, 5, 6], 5))
print(s.searchInsert([1, 3, 5, 6], 2))
print(s.searchInsert([1, 3, 5, 6], 7))
print(s.searchInsert([1, 3, 5, 6], -1))
