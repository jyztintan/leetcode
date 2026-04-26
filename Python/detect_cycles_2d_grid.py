class UFDS:
    def __init__(self, n):
        self.size = [1] * n
        self.parent = list(range(n))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def unite(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.size[y] > self.size[x]:
            self.size[y] += self.size[x]
            self.parent[x] = y
        else:
            self.size[x] += self.size[y]
            self.parent[y] = x
        return True


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        ufds = UFDS(m * n)
        for row in range(m):
            for col in range(n):
                if row + 1 < m and grid[row][col] == grid[row + 1][col]:
                    if not ufds.unite(row * n + col, (row + 1) * n + col):
                        return True
                if col + 1 < n and grid[row][col] == grid[row][col + 1]:
                    if not ufds.unite(row * n + col, row * n + col + 1):
                        return True
        return False
