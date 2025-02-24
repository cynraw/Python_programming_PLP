#Given a string s, return the longest substring without repeating characters.
def longestSubstring(s):
    char_set = set()
    left = max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    return max_length

s = "abcabcbb"
print(longestSubstring(s))  # Output: 3