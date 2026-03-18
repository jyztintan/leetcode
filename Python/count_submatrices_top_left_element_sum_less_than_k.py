# Optimised space solution of below - just store most recent row
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        prefix_sums = [0] * n
        if grid[0][0] > k:
            return 0

        count = 0
        for row in range(m):
            curr = 0
            for col in range(n):
                curr += grid[row][col]
                if curr + prefix_sums[col] <= k:
                    count += 1
                prefix_sums[col] = prefix_sums[col] + curr
        return count

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        prefix_sums = [[0] * n for _ in range(m)]
        prefix_sums[0][0] = grid[0][0]

        # Precompute first row
        if grid[0][0] > k:
            return 0
        count = 1
        for col in range(1, n):
            prefix_sums[0][col] = prefix_sums[0][col - 1] + grid[0][col]
            if prefix_sums[0][col] <= k:
                count += 1

        # Keep track of current row value as we iterate through columns
        # Then add the rectangle directly above
        for row in range(1, m):
            curr = 0
            for col in range(n):
                curr += grid[row][col]
                if curr + prefix_sums[row - 1][col] <= k:
                    count += 1
                prefix_sums[row][col] = prefix_sums[row - 1][col] + curr
        return count


