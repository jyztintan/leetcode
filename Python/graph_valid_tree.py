# Thank you Prof Halim for teaching UFDS during my time in CS2040S AY23/24 Semester 1
# Source: https://github.com/stevenhalim/cpbook-code/blob/master/ch2/ourown/unionfind_ds.py
# Modified variable naming for code readability
class UFDS:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.sizes = [1] * n
        self.num_disjoint_sets = n

    def find(self, element):
        children = []
        while element != self.parents[element]:
            children.append(element)
            element = self.parents[element]
        for child in children:
            self.parents[child] = element
        return element

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        # If they already have the same parent, then this union is "redundant"
        if root_a == root_b:
            return True

        if self.ranks[root_a] < self.ranks[root_b]:
            self.parents[root_a] = root_b
            self.sizes[root_b] += self.sizes[root_a]
        elif self.ranks[root_b] < self.ranks[root_a]:
            self.parents[root_b] = root_a
            self.sizes[root_a] += self.sizes[root_b]
        else:
            self.parents[root_b] = root_a
            self.ranks[root_a] += 1
            self.sizes[root_a] += self.sizes[root_b]

        self.num_disjoint_sets -= 1

    def size(self, x):
        return self.sizes[self.find(x)]

class Solution:
    def validTree(self, n: int, edges) -> bool:
        ufds = UFDS(n)
        for u, v in edges:
            if ufds.union(u, v):
                return False

        return ufds.num_disjoint_sets == 1
