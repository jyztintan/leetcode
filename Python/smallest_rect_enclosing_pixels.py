class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        def searchRows(l, r, top):
            while l <= r:
                mid = (l+r)//2
                if ("1" in image[mid]) == top:
                    r = mid - 1
                else:
                    l = mid + 1

            return l

        def searchCols(l, r, left):
            while l <= r:
                mid = (l+r)//2
                if any(image[x][mid] == "1" for x in range(top, bottom)) == left:
                    r = mid - 1
                else:
                    l = mid + 1

            return l

        m, n = len(image), len(image[0])

        top = searchRows(0, x, True)
        bottom = searchRows(x, m-1, False)
        left = searchCols(0, y, True)
        right = searchCols(y, n-1, False)

        return (right - left) * (bottom - top)

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
