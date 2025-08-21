class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [0] * n

        best = 0
        for row in range(m):
            new_dp = [0] * n
            for col in range(n):
                if matrix[row][col] != "1":
                    continue
                if row == 0 or col == 0:
                    new_dp[col] = 1
                else:
                    new_dp[col] = 1 + min(dp[col - 1], dp[col], new_dp[col - 1])
                best = max(best, new_dp[col])
            dp = new_dp
        return best * best
