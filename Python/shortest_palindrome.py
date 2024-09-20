class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans_left, ans_right = 0, 0
        highest = 0

        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > highest:
                    ans_left, ans_right = left, right
                    highest = right - left + 1
                left -= 1
                right += 1

            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > highest:
                    ans_left, ans_right = left, right
                    highest = right - left + 1
                left -= 1
                right += 1

        return ans_left, ans_right

    def shortestPalindrome(self, s: str) -> str:
        left, right = self.longestPalindrome(s)
        if left == 0:
            prefix = s[right + 1:][::-1]
        else:
            ptr = left - 1
            while ptr >= 0 and s[ptr] == s[left]:
                ptr -= 1
                left += 1
            prefix = s[left:][::-1]
        return prefix + s


# print(Solution().shortestPalindrome("ababbbabbaba"))
# print(Solution().shortestPalindrome("abcd"))






