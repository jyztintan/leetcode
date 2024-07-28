# Solution 1: 2D-Dynamic Programming
# Sort of 2D but every time we iterate the new row we write over the previous row data
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        dp = [0] * (cols + 1)

        for row in range(1, rows + 1):
            template_row = [0] * (cols + 1)
            for column in range(1, cols + 1):
                if text1[row - 1] == text2[column - 1]:
                    template_row[column] = dp[column - 1] + 1
                else:
                    template_row[column] = max(template_row[column - 1], dp[column])
            dp = template_row
        return dp[cols]

# Solution 2: Memoization
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
