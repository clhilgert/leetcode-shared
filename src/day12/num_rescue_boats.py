# You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

# Return the minimum number of boats to carry every given person.


# Example 1:

# Input: people = [1,2], limit = 3
# Output: 1
# Explanation: 1 boat (1, 2)
# Example 2:

# Input: people = [3,2,2,1], limit = 3
# Output: 3
# Explanation: 3 boats (1, 2), (2) and (3)
# Example 3:

# Input: people = [3,5,3,4], limit = 5
# Output: 4
# Explanation: 4 boats (3), (3), (4), (5)
# [1,2,3,4,5,6,7] limit = 10
"""
#[1,3,6,7]
{
    1,
    2,
    4,
    5,
    6,
    7,
    8,
    10,
    10,
    10

}
"""


# [1,2,2,3], limit 3
def numRescueBoats(people: list[int], limit: int) -> int:
    people.sort()
    l, r = 0, len(people) - 1
    num_boats = 0

    while l < r:
        if (
            people[l] + people[r] > limit
        ):  # person on the right side gets their own boat
            num_boats += 1
            r -= 1
        else:  # matching pair found
            l += 1
            r -= 1
            num_boats += 1

    if l == r:
        num_boats += 1

    return num_boats


print(numRescueBoats([1, 2], 3))  # 1
print(numRescueBoats([3, 2, 2, 1], 3))  # 3
print(numRescueBoats([3, 5, 3, 4], 5))  # 4
