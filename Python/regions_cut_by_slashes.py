# Solution 1: Using UFDS for DFS
class UFDS:
    def __init__(self, n):
        self.rank = [1] * n
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)

        if parent_x == parent_y:
            return

        if self.rank[parent_x] > self.rank[parent_y]:
            self.parent[parent_y] = parent_x
        elif self.rank[parent_x] < self.rank[parent_y]:
            self.parent[parent_x] = parent_y
        else:
            self.parent[parent_x] = parent_y
            self.rank[parent_y] += 1

class Solution:
    def regionsBySlashes(self, grid) -> int:
        n = len(grid)
        new_grid = [[0] * (n * 3) for i in range(n * 3)]

        for row in range(n):
            for col in range(n):
                if grid[row][col] == "\\":
                    for i in range(3):
                        new_grid[row * 3 + i][col * 3 + i] = 1
                elif grid[row][col] == "/":
                    for i in range(3):
                        new_grid[row * 3 + 2 - i][col * 3 + i] = 1

        count = 0
        n *= 3
        ufds = UFDS(n * n)
        for row in range(n):
            for col in range(n):

                if new_grid[row][col] == 0:
                    if row + 1 < n and new_grid[row + 1][col] == 0:
                        ufds.union(row * n + col, (row + 1) * n + col)
                    if col + 1 < n and new_grid[row][col + 1] == 0:
                        ufds.union(row * n + col, row * n + col + 1)
                else:
                    count += 1

        unique = set()
        for i in range(n * n):
            unique.add(ufds.find(i))

        return len(unique) - count

# Solution 2: Using Recursive DFS
class Solution:
    def regionsBySlashes(self, grid) -> int:
        n = len(grid)
        new_grid = [[0] * (n * 3) for i in range(n * 3)]

        for row in range(n):
            for col in range(n):
                if grid[row][col] == "\\":
                    for i in range(3):
                        new_grid[row * 3 + i][col * 3 + i] = 1
                elif grid[row][col] == "/":
                    for i in range(3):
                        new_grid[row * 3 + 2 - i][col * 3 + i] = 1

        def dfs(x, y):
            if x < 0 or x >= n * 3 or y < 0 or y >= n * 3 or new_grid[x][y] == 1:
                return
            new_grid[x][y] = 1
            dfs(x, y + 1)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x - 1, y)

        count = 0
        for row in range(3 * n):
            for col in range(3 * n):
                if new_grid[row][col] == 0:
                    dfs(row, col)
                    count += 1

        return count
