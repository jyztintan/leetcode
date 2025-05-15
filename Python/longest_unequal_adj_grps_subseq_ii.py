class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def valid(w1, w2):
            n = len(w1)
            if n != len(w2):
                return False
            diff = 0
            for i in range(n):
                if w1[i] != w2[i]:
                    diff += 1
            return diff == 1

        n = len(words)
        dp = [[i] for i in range(n)]
        for i in range(n):
            for j in range(i):
                if groups[i] != groups[j] and valid(words[i], words[j]) and len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j].copy()
                        dp[i].append(i)
        longest = max(dp, key=len)
        return [words[i] for i in longest]
