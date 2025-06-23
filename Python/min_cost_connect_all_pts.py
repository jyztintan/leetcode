class UFDS:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n

    def find(self, n):
        if self.parents[n] != n:
            self.parents[n] = self.find(self.parents[n])
        return self.parents[n]

    def join(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x == parent_y:
            return False

        if self.ranks[parent_x] > self.ranks[parent_y]:
            self.parents[parent_y] = parent_x
        elif self.ranks[parent_y] > self.ranks[parent_x]:
            self.parents[parent_x] = parent_y
        else:
            self.parents[parent_y] = parent_x
            self.ranks[parent_x] += 1
        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        n = len(points)
        ufds = UFDS(n)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                manhattan = abs(y2 - y1) + abs(x2 - x1)
                edges.append((manhattan, i, j))

        edges.sort()

        cost = 0
        for manhattan, p1, p2 in edges:
            if ufds.join(p1, p2):
                cost += manhattan
        return cost
