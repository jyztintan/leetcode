class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(row, col):
            fishes = grid[row][col]
            grid[row][col] = 0
            for x, y in directions:
                new_row, new_col = row + x, col + y
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] != 0:
                    fishes += dfs(new_row, new_col)
            return fishes

        max_fishes = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] > 0:
                    max_fishes = max(max_fishes, dfs(row, col))
        return max_fishes
