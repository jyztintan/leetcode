class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ways = [[0] * n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                # If it is a corner tile, then there is only one way to get there
                if row == 0 or col == 0:
                    ways[row][col] = 1
                else:
                    ways[row][col] = ways[row][col - 1] + ways[row - 1][col]

        return ways[m - 1][n - 1]
