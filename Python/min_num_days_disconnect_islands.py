class Solution:
    def minDays(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        def check_disconnected(grid):
            count = 0
            def dfs(row, col):
                if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0:
                    return
                grid[row][col] = 0
                dfs(row + 1, col)
                dfs(row, col + 1)
                dfs(row - 1, col)
                dfs(row, col - 1)

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        count += 1
                        dfs(i, j)
            return count

        copy = [row[:] for row in grid]
        if check_disconnected(copy) != 1:
            return 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    new_grid = [row[:] for row in grid]
                    new_grid[i][j] = 0
                    if check_disconnected(new_grid[:]) != 1:
                        return 1

        return 2

# grid = [[0,1,1,1],[0,0,0,0],[0,0,0,0]]
# print(Solution().minDays(grid))
