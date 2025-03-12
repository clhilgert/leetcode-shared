def longest_substring(str):
    if len(str) == 1:
        return 1
    left = 0
    right = 0
    longest = 0
    chars = set()
    while right < len(str):
        if str[right] in chars:
            while str[right] in chars:
                chars.remove(str[left])
                left += 1
        chars.add(str[right])
        right += 1
        longest = max(longest, len(chars))
    return longest


print(longest_substring("abcabcbb"))
print(longest_substring("bbbbb"))
print(longest_substring("pwwkew"))
print(longest_substring("dvdf"))  # should be 3
print(longest_substring("zcbadce"))
print(longest_substring("ab"))
