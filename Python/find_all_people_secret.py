class UFDS:
    def __init__(self, n):
        self.rank = [0] * n
        self.parent = list(range(n))

    def find(self, u):
        parent = self.parent[u]
        if u != parent:
            self.parent[u] = self.find(parent)
        return self.parent[u]

    def union(self, u, v):
        u, v = self.find(u), self.find(v)
        if self.is_connected(u, v):
            return
        if self.rank[u] == self.rank[v]:
            self.parent[v] = u
            self.rank[u] += 1
        elif self.rank[u] > self.rank[v]:
            self.parent[v] = u
        else:
            self.parent[u] = v

    def is_connected(self, u, v):
        return self.find(u) == self.find(v)

    def reset(self, u):
        self.rank[u] = 0
        self.parent[u] = u


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key=lambda x: x[2])
        same_time = defaultdict(set)
        for p1, p2, time in meetings:
            same_time[time].add((p1, p2))

        ufds = UFDS(n)
        ufds.union(0, firstPerson)
        for time in sorted(same_time):
            for u, v in same_time[time]:
                ufds.union(u, v)

            for u, v in same_time[time]:
                if not ufds.is_connected(u, 0):
                    ufds.reset(u)
                    ufds.reset(v)
        return [u for u in range(n) if ufds.is_connected(u, 0)]
