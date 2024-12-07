class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbour in adj_list[node]:
                dfs(neighbour)

        count = 0
        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)
        return count


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
    def countComponents(self, n: int, edges) -> int:
        ufds = UFDS(n)
        for u, v in edges:
            ufds.union(u, v)

        return ufds.num_disjoint_sets
