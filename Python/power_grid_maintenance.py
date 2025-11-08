# Solution 1 : DFS

# Solution 2 : MLE, TLE
class UFDS:
    def __init__(self, n):
        self.online = [True] * n
        self.parent = list(range(n))
        self.rank = [0] * n
        self.grid = [{i} for i in range(n)]

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        parent_u, parent_v = self.find(u), self.find(v)
        if self.rank[parent_u] > self.rank[parent_v]:
            self.parent[parent_v] = parent_u
        elif self.rank[parent_v] > self.rank[parent_u]:
            self.parent[parent_u] = parent_v
        else:
            self.rank[parent_u] += 1
            self.parent[parent_v] = parent_u
        new = self.grid[parent_u].union(self.grid[parent_v])
        self.grid[parent_u] = new
        self.grid[parent_v] = new

    def shutdown(self, u):
        if not self.online[u]:
            return
        self.online[u] = False
        parent = self.find(u)
        self.grid[parent].remove(u)


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        ufds = UFDS(c)
        for u, v in connections:
            u, v = u - 1, v - 1
            ufds.union(u, v)

        output = []
        for q, s in queries:
            s -= 1
            if q == 1:
                if ufds.online[s]:
                    output.append(s + 1)
                    continue
                grid = ufds.grid[ufds.find(s)]
                best = float('inf')
                for station in grid:
                    if ufds.online[station]:
                        best = min(best, station)
                if best == float('inf'):
                    best = -2
                output.append(best + 1)
            elif q == 2:
                ufds.shutdown(s)
        return output

