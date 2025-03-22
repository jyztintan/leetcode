class UFDS:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [1] * n
        self.sizes = [1] * n

    def find(self, u):
        if self.parents[u] != u:
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
            self.ranks[parent_u] += 1
            self.parents[parent_v] = parent_u
            self.sizes[parent_u] += self.sizes[parent_v]


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        ufds = UFDS(n)
        for u, v in edges:
            ufds.union(u, v)

        edge_count = {}
        for u, v in edges:
            parent = ufds.find(u)
            if parent == ufds.find(v):
                edge_count[parent] = edge_count.get(parent, 0) + 1

        count = 0
        for node in range(n):
            if ufds.find(node) == node:
                edges = edge_count.get(node, 0)
                nodes = ufds.sizes[node]
                if edges == (nodes * (nodes - 1)) // 2:
                    count += 1
        return count
