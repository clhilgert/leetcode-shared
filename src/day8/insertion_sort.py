# Given an array of integers nums, sort the array in ascending order and return it.


# Example 1:

# Input: nums = [5,2,3,1]
# Output: [1,2,3,5]
# Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
# Example 2:

# Input: nums = [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# Explanation: Note that the values of nums are not necessairly unique.


# nums = [2,3,1]


def sort_array(nums):
    sorted_array = []  # [1,2,4] 0
    for num in nums:  # 2
        i = 0
        while i < len(sorted_array) and num > sorted_array[i]:
            i += 1
        # .insert(index, value)
        sorted_array.insert(i, num)

    return sorted_array


print(sort_array([5, 1, 1, 2, 0, 0]))
