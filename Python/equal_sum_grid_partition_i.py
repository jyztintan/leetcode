class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total_sum = sum(sum(row) for row in grid)
        target = total_sum / 2

        curr = 0
        for row in range(m):
            for col in range(n):
                curr += grid[row][col]
            if curr == target:
                return True

        curr = 0
        for col in range(n):
            for row in range(m):
                curr += grid[row][col]
            if curr == target:
                return True

        return False
