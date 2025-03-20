# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:
# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.
# [1,2,2,3,3,4,4] ->  [1,2,3,4,.....] return 4
# num1 = [1,3,3,3,3] -> num1 = [1,3,.....] return 2


def removeDuplicates(nums):
    if not nums:
        return 0
    left = 1
    for right in range(1, len(nums)):
        if nums[right] != nums[right - 1]:
            # nums[i] is leading, and nums[i] is gonna be the non dup
            nums[left] = nums[right]
            left += 1
    return left


# [1,2,2,3,3,4,4] ->  [1,2,3,4,.....]
nums1 = [1, 2, 2, 3, 3, 4, 4]

print(removeDuplicates(nums1))  # 4 ,[1,2,3,4,.....]

print(removeDuplicates([]))
