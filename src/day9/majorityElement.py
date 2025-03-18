# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


# Example 1:


# Input: nums = [3,2,3]
#                    ^
# Output: 3
# Example 2:
# [2,2,1,1,1,2,2,1,1,1,1,1,1,1,1]
# Input: nums = [2,2,1,1,1,2,2]
#                            ^
# Output: 2
def majorityElement(nums):
    # we track whether an candidate number could be majority through negative / positive appearances
    # track candidates and counts
    # when the appearneces because negative, swap out the new potential majority element

    candidate = nums[0]
    counts = 1

    for num in nums[1:]:
        if num != candidate:  # we only care if it is the number or not
            counts -= 1
        else:
            counts += 1
        if counts < 0:
            candidate = num
            counts = 1

    print(candidate)


majorityElement([3, 2, 3])


majorityElement([2, 2, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1])
