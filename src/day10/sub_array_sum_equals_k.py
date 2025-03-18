# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

# time 7:10

# Example 1:

# Input: nums = [1,1,1], k = 1

# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 1
# Output: 2

# nums = [1,2,3,4,5,6,7,8,9]
#               ^     ^


# Constraints:

# 1 <= nums.length <= 2 * 104
# -1000 <= nums[i] <= 1000
# -107 <= k <= 107


# more than, increment left pointer
# less than, increment right pointer
# [10, 10, -10, -10] k = 0


from collections import defaultdict


def contiguou_sub(nums, k):

    # declaring a dictionary of prefix sum frequencies

    # for ind in range(len(nums)):
    #     total += nums[ind]
    #     prefix_sum.append(total)

    total = 0
    res = 0
    seen = defaultdict(int)
    seen[0] += 1

    # track the prefix sums as we iterate over the array
    # at our new prefix sum, if we subtract out k, does that give us a previously appeared prefix sum
    # when you subtract two prefix sums, you generate a subarray
    # store new prefix sum in hashmap

    for ind in len(nums):
        total += nums[ind]
        check = total - k
        if check in seen:
            res += seen[check]

        seen[total] += 1

    return res


# [1,1,1], k = 1
# [-2,0,1,-1,1,-1,1,-1,3], k = 1
#  ^^^
