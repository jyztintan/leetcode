class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k // 2):
            for col in range(y, y + k):
                grid[x + i][col], grid[x + k - 1 - i][col] = grid[x + k - 1 - i][col], grid[x + i][col]
        return grid
