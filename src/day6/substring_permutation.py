# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidabooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
#-----> SLIDING WINDOW!!!!!! <----- THIS LIAM!!!!

from collections import defaultdict



def permutation(s1: str, s2: str) -> bool:
    # edge case
    if len(s2) < len(s1):
        return False
    # examine the sliding window of length s1 across s2
    s1_map = defaultdict(int)
    
    for char in s1: # character freq representation
        s1_map[char] -= 1

    # iterate over s2
    l, r = 0, 0

    while r < len(s2):
        # need a condition to continue iterating
        if r - l + 1 > len(s1):
            s1_map[s2[l]] -= 1
            l += 1

        s1_map[s2[r]] += 1 # adding the frequency back to the s1_map
        if areAnyFrequenciesNegative(s1_map):
            return True
        
        r += 1
    
    return False

def areAnyFrequenciesNegative(dictionary):
    for char, freq in dictionary.items():
        if freq < 0:
            return False
    return True

s1 = "ab"
s2 = "eidabooo"
# s1 = "ab"
# s2 = "eidboaoo"

print(permutation(s1, s2))