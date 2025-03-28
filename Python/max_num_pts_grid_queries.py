class UFDS:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [1] * n
        self.sizes = [1] * n

    def find(self, u):
        if u != self.parents[u]:
            self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self, u, v):
        parent_u = self.find(u)
        parent_v = self.find(v)
        if parent_u == parent_v:
            return
        if self.ranks[parent_u] > self.ranks[parent_v]:
            self.parents[parent_v] = parent_u
            self.sizes[parent_u] += self.sizes[parent_v]
        elif self.ranks[parent_v] > self.ranks[parent_u]:
            self.parents[parent_u] = parent_v
            self.sizes[parent_v] += self.sizes[parent_u]
        else:
            self.parents[parent_v] = parent_u
            self.ranks[parent_u] += 1
            self.sizes[parent_u] += self.sizes[parent_v]

    def get_size(self, u):
        return self.sizes[self.find(u)]


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sorted_queries = sorted([query, idx] for idx, query in enumerate(queries))
        sorted_cells = sorted([grid[row][col], row, col] for row in range(m) for col in range(n))

        ufds = UFDS(m * n)
        activated = [False] * (m * n)
        ptr = 0

        ans = [0] * len(queries)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for query, idx in sorted_queries:
            while ptr < m * n and sorted_cells[ptr][0] < query:
                val, row, col = sorted_cells[ptr]
                cell = row * n + col
                activated[cell] = True

                for x, y in directions:
                    nrow, ncol = row + x, col + y
                    if 0 <= nrow < m and 0 <= ncol < n:
                        neighbour_cell = nrow * n + ncol
                        if activated[neighbour_cell]:
                            ufds.union(cell, neighbour_cell)
                ptr += 1

            if not activated[0]:
                ans[idx] = 0
            else:
                ans[idx] = ufds.get_size(0)
        return ans
