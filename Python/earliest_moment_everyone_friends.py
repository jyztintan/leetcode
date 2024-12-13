class Friendship:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.connections = 0

    def find(self, a):
        if self.parents[a] != a:
            self.parents[a] = self.find(self.parents[a])
        return self.parents[a]

    def acquaint(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a == parent_b:
            return

        self.connections += 1
        if self.ranks[parent_a] > self.ranks[parent_b]:
            self.parents[parent_b] = parent_a
        elif self.ranks[parent_b] > self.ranks[parent_a]:
            self.parents[parent_a] = parent_b
        else:
            self.parents[parent_b] = parent_a
            self.ranks[parent_a] += 1


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        friendship = Friendship(n)
        logs.sort()
        for time, a, b in logs:
            friendship.acquaint(a, b)
            if friendship.connections == n - 1:
                return time
        return - 1
