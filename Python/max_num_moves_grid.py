class Solution:
    def maxMoves(self, grid) -> int:
        m, n = len(grid), len(grid[0])

        possible_rows = set(range(m))
        for col in range(n - 1):
            next_possible = set()
            for row in possible_rows:
                curr = grid[row][col]
                if row - 1 >= 0 and grid[row - 1][col + 1] > curr:
                    next_possible.add(row - 1)
                if grid[row][col + 1] > curr:
                    next_possible.add(row)
                if row + 1 < m and grid[row + 1][col + 1] > curr:
                    next_possible.add(row + 1)
                if len(next_possible) == m:
                    break
            if not next_possible:
                return col
            possible_rows = next_possible

        return col + 1
