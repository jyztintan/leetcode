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