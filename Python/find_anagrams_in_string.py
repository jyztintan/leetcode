class Solution:
    def findAnagrams(self, s: str, p: str):

        # If the length of substring is greater than the target string then it is impossible to find a matching substring anagram
        if len(p) > len(s):
            return []

        # Keep track of letters we are accounting for
        original = [0] * 26
        window = [0] * 26
        letter_order = ord('a')
        length = len(p)

        # Increment the relevant letter buckets of s
        for c in p:
            original[ord(c) - letter_order] += 1

        # The first window is the first letters of s
        for i in range(length):
            window[ord(s[i]) - letter_order] += 1

        ans = []

        # We incrementally slide the window and add the starting index if there is a match
        for i in range(length, len(s)):
            if window == original:
                ans.append(i - length)
            window[ord(s[i - length]) - letter_order] -= 1
            window[ord(s[i]) - letter_order] += 1

        # If the final window matches then also add starting index to ans
        if window == original:
            ans.append(len(s) - length)
        return ans

# print(Solution().findAnagrams('cbaebabacb', 'abc'))
# print(Solution().findAnagrams('abab', 'ab'))
