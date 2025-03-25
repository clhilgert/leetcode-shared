"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.



Constraints:

    0 <= x <= 231 - 1

"""

# 4 -> 2, 2
# 16 -> sqrt4, sqrt4 -> 2, 2
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# [1, 2, 3, 4, 5, 6, 7, 8]
# [ 1  <->   n ]*  by itself = target


def square_root(x):
    left = 0
    right = x
    while left <= right:
        pivot = (left + right) // 2
        product = pivot * pivot
        if product == x:
            return pivot
        elif product > x:
            right = pivot - 1
        elif product < x:
            left = pivot + 1
    return right


print(square_root(15))
