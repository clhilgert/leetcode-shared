# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: falsew

def valid_anagram(s, t):
    s_map = {}
    t_map = {}
    for char in s:
        s_map[char] = s_map.get(char, 0) + 1
    for char in t:
        t_map[char] = t_map.get(char, 0) + 1
    return s_map == t_map