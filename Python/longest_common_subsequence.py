# Solution 1: 2D-Dynamic Programming with space optimisation
# Sort of 2D but every time we iterate the new row we write over the previous row data
# This makes our space O(min(M, N))
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

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

# Solution 2: 2D-Dynamic Programming
# Time and space: O(M * N)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for row in range(1, rows + 1):
            for column in range(1, cols + 1):
                if text1[row - 1] == text2[column - 1]:
                    dp[row][column] = dp[row - 1][column - 1] + 1
                else:
                    dp[row][column] = max(dp[row][column - 1], dp[row - 1][column])
        return dp[rows][cols]


# Solution 3: Memoization
# Time and space: O(M * N)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = {}

        def check(ptr1, ptr2):
            if ptr1 < 0 or ptr2 < 0:
                return 0

            if (ptr1, ptr2) in memo:
                return memo[(ptr1, ptr2)]

            if text1[ptr1] == text2[ptr2]:
                memo[(ptr1, ptr2)] = check(ptr1 - 1, ptr2 - 1) + 1
            else:
                memo[(ptr1, ptr2)] = max(check(ptr1 - 1, ptr2), check(ptr1, ptr2 - 1))
            return memo[(ptr1, ptr2)]

        return check(len(text1) - 1, len(text2) - 1)

# test = Solution()
# print(test.longestCommonSubsequence("abcde", "ace"))
