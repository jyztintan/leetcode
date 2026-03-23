class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        extremes = [[[inf, -inf] for _ in range(n)] for _ in range(m)]
        extremes[0][0] = (grid[0][0], grid[0][0])
        for row in range(m):
            for col in range(n):
                low, high = extremes[row][col]
                # Go right
                if col + 1 < n:
                    curr = grid[row][col + 1]
                    if curr >= 0:
                        extremes[row][col + 1][0] = min(extremes[row][col + 1][0], low * curr)
                        extremes[row][col + 1][1] = max(extremes[row][col + 1][1], high * curr)
                    if curr <= 0:
                        extremes[row][col + 1][0] = min(extremes[row][col + 1][0], high * curr)
                        extremes[row][col + 1][1] = max(extremes[row][col + 1][1], low * curr)
                # Go down
                if row + 1 < m:
                    curr = grid[row + 1][col]
                    if curr >= 0:
                        extremes[row + 1][col][0] = min(extremes[row + 1][col][0], low * curr)
                        extremes[row + 1][col][1] = max(extremes[row + 1][col][1], high * curr)
                    if curr <= 0:
                        extremes[row + 1][col][0] = min(extremes[row + 1][col][0], high * curr)
                        extremes[row + 1][col][1] = max(extremes[row + 1][col][1], low * curr)

        if extremes[m - 1][n - 1][1] < 0:
            return -1
        return extremes[m - 1][n - 1][1] % (10 ** 9 + 7)