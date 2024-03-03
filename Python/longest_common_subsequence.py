class Solution:
    memoize = {"" : 0}
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2:
            return 0
        if text1[-1] == text2[-1]:
            if (text1[:-1], text2[:-1]) not in self.memoize:
                self.memoize[(text1[:-1], text2[:-1])] = self.longestCommonSubsequence(text1[:-1], text2[:-1])
            return self.memoize[(text1[:-1], text2[:-1])] + 1
        if (text1[:-1], text2) not in self.memoize:
            self.memoize[(text1[:-1], text2)] = self.longestCommonSubsequence(text1[:-1], text2)
        possible = self.memoize[(text1[:-1], text2)]
        if (text1, text2[:-1]) not in self.memoize:
            self.memoize[(text1, text2[:-1])] = self.longestCommonSubsequence(text1, text2[:-1])
        other_possible = self.memoize[(text1, text2[:-1])]
        return possible if possible > other_possible else other_possible

test = Solution()
print(test.longestCommonSubsequence("abcde", "ace"))
