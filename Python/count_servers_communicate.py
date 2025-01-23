class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        row_counts = [0] * m
        col_counts = [0] * n
        for row in range(m):
            for col in range(n):
                if grid[row][col]:
                    row_counts[row] += 1
                    col_counts[col] += 1

        count = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] and (row_counts[row] > 1 or col_counts[col] > 1):
                    count += 1

        return count
