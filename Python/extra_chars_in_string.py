class Solution:
    def minExtraChar(self, s: str, dictionary) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dictionary = set(dictionary)

        for start in range(n - 1, -1, -1):
            dp[start] = 1 + dp[start + 1]
            for end in range(start, n):
                curr = s[start: end + 1]
                if curr in dictionary:
                    dp[start] = min(dp[start], dp[end + 1])

        return dp[0]

# s = "leetleetscode"
# dictionary = ["leet","code","leetcode"]
# print(Solution().minExtraChar(s, dictionary))
