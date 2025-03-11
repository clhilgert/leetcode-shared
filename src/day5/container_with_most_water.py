# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:
# https://leetcode.com/problems/container-with-most-water/description/

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1


def most_water(heights):
    max_water = 0
    left = 0
    right = len(heights) - 1
    while left < right:
        width = min(heights[left], heights[right])
        length = right - left
        area = width * length
        max_water = max(max_water, area)
        if heights[left] < heights[right]:
            left += 1
        elif heights[right] < heights[left]:
            right -= 1
        else:
            left += 1
    return max_water


print(most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))
