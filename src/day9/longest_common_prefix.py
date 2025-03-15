# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# [f l ]


def longestCommonPrefix(strs):
    prefix = list(strs[0])
    for i in range(1, len(strs)):
        curr_str = strs[i]
        for j in range(len(curr_str)):
            if j > len(prefix) - 1:
                break
            if prefix[j] != curr_str[j]:
                prefix = prefix[:j]
                break
            if j == len(curr_str) - 1:
                prefix = prefix[: j + 1]
    return "".join(prefix)


print(longestCommonPrefix(["flower", "flow", "flight"]))
