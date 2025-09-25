# Bottom Up
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0] * (n + 1)
        for row in triangle[::-1]:
            for col, num in enumerate(row):
                dp[col] = min(dp[col], dp[col + 1]) + num
        return dp[0]

# Top down
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        @lru_cache
        def traverse(row, i):
            if row == n:
                return 0
            curr = triangle[row][i]
            best = min(traverse(row + 1, i), traverse(row + 1, i + 1))
            return curr + best

        return traverse(0, 0)