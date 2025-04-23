
# DFS Solution
# Time complexity: O(M * N), where V = M * N
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        row = [float('inf'), -1]
        col = [float('inf'), -1]
        m, n = len(image), len(image[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            if image[r][c] == '1':
                row[0] = min(row[0], r)
                row[1] = max(row[1], r)
                col[0] = min(col[0], c)
                col[1] = max(col[1], c)

            image[r][c] = '2'

            for dx, dy in directions:
                new_row, new_col = r + dx, c + dy
                if 0 <= new_row < m and 0 <= new_col < n and image[new_row][new_col] == '1':
                    dfs(new_row, new_col)

        dfs(x, y)

        return (row[1] - row[0] + 1) * (col[1] - col[0] + 1)

# Naive explore all solution
# Time complexity: O(M * N), where V = M * N
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        row = [float('inf'), -1]
        col = [float('inf'), -1]
        m, n = len(image), len(image[0])
        for r in range(m):
            for c in range(n):
                if image[r][c] == '1':
                    row[0] = min(row[0], r)
                    row[1] = max(row[1], r)
                    col[0] = min(col[0], c)
                    col[1] = max(col[1], c)

        return (row[1] - row[0] + 1) * (col[1] - col[0] + 1)
