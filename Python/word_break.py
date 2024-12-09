class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for idx in range(n):
            if not dp[idx]:
                continue
            for word in wordDict:
                end = idx + len(word)
                if end <= n and s[idx:end] == word:
                    dp[end] = True
        return dp[n]

class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1):
            for word in wordDict:
                # We search for the next valid word backwards
                if (i + len(word) <= len(s)) and s[i:i + len(word)] == word:
                    dp[i] = dp[i + len(word)]

                    if dp[i]:
                        # If there is a valid word, we set it as the next checkpoint to check for a next valid word
                        break
        # The word break is valid if the last character fits
        return dp[0]

# wordDict = ["leet","code"]
# print(Solution().wordBreak("leetcode", wordDict))
