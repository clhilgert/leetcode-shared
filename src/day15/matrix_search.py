"""
You are given an m x n integer matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.



Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false


"""


# helper function for searching in a row
def binarySearch(arr, target):
    l, r = 0, len(arr) - 1

    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            return True
        elif arr[m] < target:
            l = m + 1
        elif arr[m] > target:
            r = m - 1

    return False


def matrixSearch(matrix, target):
    ROW = len(matrix)
    COL = len(matrix[0])

    t, b = 0, ROW - 1

    while t <= b:
        # check the actual values
        mid = (t + b) // 2
        middle_row = matrix[mid]  # gives us the row we are working with

        if middle_row[0] == target or middle_row[COL - 1] == target:
            return True
        else:
            if middle_row[0] < target < middle_row[COL - 1]:
                return binarySearch(middle_row, target)
            elif target > middle_row[COL - 1]:
                t = mid + 1
            else:
                b = mid - 1

    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 13
print(matrixSearch(matrix, target))
