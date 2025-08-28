class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for idx in range(n + n - 1):
            start_row = max(0, n - idx - 1)
            start_col = max(0, idx - n + 1)

            row, col = start_row, start_col
            curr = []
            while row < n and col < n:
                curr.append(grid[row][col])
                row += 1
                col += 1

            curr.sort(reverse=idx < n)
            row, col = start_row, start_col
            ptr = 0
            while row < n and col < n:
                grid[row][col] = curr[ptr]
                row += 1
                col += 1
                ptr += 1
        return grid
