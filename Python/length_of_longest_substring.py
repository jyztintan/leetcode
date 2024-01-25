def length_of_longest_substring(s):
    chars = set()
    left = 0
    res = 0

    for i in range(len(s)):
        while s[i] in chars:
            chars.remove(s[left])
            left += 1
        chars.add(s[i])
        res = max(res, len(chars))
    return res

s = "abcabcbb"
print(length_of_longest_substring(s))
s = "bbbbb"
print(length_of_longest_substring(s))
s = "pwwkew"
print(length_of_longest_substring(s))
s = "abcabcbb"
print(length_of_longest_substring(s))
