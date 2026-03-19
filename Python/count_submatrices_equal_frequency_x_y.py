class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        prev = [[0, 0] for _ in range(n)]

        x, y = 0, 0
        count = 0
        for row in range(m):
            x, y = 0, 0
            for col in range(n):
                prev_x, prev_y = prev[col]
                match grid[row][col]:
                    case "X":
                        x += 1
                    case "Y":
                        y += 1
                new_x, new_y = x + prev_x, y + prev_y
                prev[col] = [new_x, new_y]
                if new_x > 0 and new_x == new_y:
                    count += 1
        return count
