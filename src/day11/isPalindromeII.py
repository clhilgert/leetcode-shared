# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
 

# s = "aabbada"

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.

# Start time: 1825


def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

def isPalindromeII(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # remove the left char
            s1 = s[left + 1:right + 1]
            s2 = s[left:right]
            return isPalindrome(s1) or isPalindrome(s2)
        
        left += 1
        right -= 1
    
    return True

s = "aabbada"
print(isPalindromeII(s))

s2 = "abc"
print(isPalindromeII(s2))




## Some Optimization for isPalindrome. Removing the slice and using parameter and default values instead. 
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.


# def isPalindrome(s):
#     left = 0
#     right = len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left += 1
#         right -= 1
    
#     return True

# def isPalindromeII(s, left=0, right=-1, failures=0):
#     left = 0
#     right = len(s) - 1 if right == -1 else right
#     while left < right:
#         if s[left] != s[right]:
#             if failures:
#                 return False
#             # remove the left char
#             # s1 = s[left + 1:right + 1]
#             # s2 = s[left:right]
#             return isPalindromeII(s, left + 1, right, 1) or isPalindromeII(s, left, right - 1, 1)
#         left += 1
#         right -= 1
    
#     return True

# s = "aabbada"
# print(isPalindromeII(s))

# s2 = "abc"
# print(isPalindromeII(s2))