class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        directions = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
        m, n = len(grid), len(grid[0])

        dp = {}

        def traverse(row, col, direction, turned, target):
            if (row, col, direction, turned) in dp:
                return dp[(row, col, direction, turned)]
            dx, dy = directions[direction]
            new_row, new_col = row + dx, col + dy
            if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n or grid[new_row][new_col] != target:
                return 0

            best = traverse(new_row, new_col, direction, turned, 2 - target)
            if not turned:
                best = max(best, traverse(new_row, new_col, (direction + 1) % 4, True, 2 - target))

            dp[(row, col, direction, turned)] = best + 1
            return best + 1

        ans = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    for direction in range(4):
                        ans = max(ans, traverse(row, col, direction, False, 2) + 1)
        return ans
