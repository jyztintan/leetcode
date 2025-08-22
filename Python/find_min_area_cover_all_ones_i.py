class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_row, min_col = float('inf'), float('inf')
        max_row, max_col = 0, 0
        m, n = len(grid), len(grid[0])

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    min_row = min(min_row, row)
                    max_row = max(max_row, row)
                    min_col = min(min_col, col)
                    max_col = max(max_col, col)
        return (max_row - min_row + 1) * (max_col - min_col + 1)
