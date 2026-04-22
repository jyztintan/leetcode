class UFDS:
    def __init__(self, n):
        self.ranks = [0] * n
        self.parents = list(range(n))

    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x == parent_y:
            return
        if self.ranks[parent_x] > self.ranks[parent_y]:
            self.parents[parent_y] = parent_x
        elif self.ranks[parent_x] > self.ranks[parent_y]:
            self.parents[parent_x] = parent_y
        else:
            self.ranks[parent_x] += 1
            self.parents[parent_y] = parent_x


class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        ufds = UFDS(n)
        for x, y in allowedSwaps:
            ufds.union(x, y)

        components = defaultdict(lambda: defaultdict(int))  # key: parent_node, val: available quota
        for idx, num in enumerate(source):
            parent = ufds.find(idx)
            components[parent][num] += 1

        hamming = 0
        for idx, num in enumerate(target):
            parent = ufds.find(idx)
            if components[parent][num] == 0:
                hamming += 1
            else:
                components[parent][num] -= 1
        return hamming
