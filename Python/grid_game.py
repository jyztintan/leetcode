class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        top_sum = sum(grid[0])
        bottom_sum = 0
        min_sum = float('inf')

        for idx in range(n):
            top_sum -= grid[0][idx]
            min_sum = min(min_sum, max(top_sum, bottom_sum))
            bottom_sum += grid[1][idx]

        return min_sum
