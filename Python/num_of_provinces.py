# Solution 1: DFS
class Solution:
    def findCircleNum(self, isConnected) -> int:
        visited = set()
        provinces = 0

        def dfs(node):
            for neighbor, connected in enumerate(isConnected[node]):
                if connected and neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor)

        for i in range(len(isConnected[0])):
            if i not in visited:
                dfs(i)
                provinces += 1

        return provinces

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(Solution().findCircleNum(isConnected))
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
print(Solution().findCircleNum(isConnected))


# Solution 2: UFDS Solution
# Thank you Prof Halim for teaching UFDS during my time in CS2040S AY23/24 Semester 1
# Source: https://github.com/stevenhalim/cpbook-code/blob/master/ch2/ourown/unionfind_ds.py
# Modified variable naming for code readability
class UFDS:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
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
            return

        if self.ranks[root_a] < self.ranks[root_b]:
            self.parents[root_a] = root_b
        elif self.ranks[root_b] < self.ranks[root_a]:
            self.parents[root_b] = root_a
        else:
            self.parents[root_b] = root_a
            self.ranks[root_a] += 1

        self.num_disjoint_sets -= 1

class Solution:
    def findCircleNum(self, isConnected) -> int:
        n = len(isConnected)
        cities = UFDS(n)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    cities.union(i, j)
        return cities.num_disjoint_sets

isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(Solution().findCircleNum(isConnected))
isConnected = [[1,0,0],[0,1,0],[0,0,1]]
print(Solution().findCircleNum(isConnected))
