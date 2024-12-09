class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Keep track of left, right pointer instead of doing the string slicing in the loop which
        # may get quite expensive if there are many long palindromes
        best = [0, 0]
        n = len(s)
        for i in range(n):
            left = right = i
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left > best[1] - best[0]:
                    best = [left, right]
                left -= 1
                right += 1

            left = i - 1
            right = i
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left > best[1] - best[0]:
                    best = [left, right]
                left -= 1
                right += 1

        return s[best[0]:best[1] + 1]