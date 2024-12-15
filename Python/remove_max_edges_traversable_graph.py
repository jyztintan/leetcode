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
            return True

        if self.ranks[root_a] < self.ranks[root_b]:
            self.parents[root_a] = root_b
        elif self.ranks[root_b] < self.ranks[root_a]:
            self.parents[root_b] = root_a
        else:
            self.parents[root_b] = root_a
            self.ranks[root_a] += 1

        self.num_disjoint_sets -= 1



class Solution:
    def maxNumEdgesToRemove(self, n: int, edges) -> int:
        alice = UFDS(n)
        bob = UFDS(n)
        ans = 0

        # We want to process the edges of type 3 first, we can either sort the edges (potentially (3n)log(3n), or exclusively process the type 3 edges first O(n)
        # Method 1 - Sort edges: edges.sort(key=lambda x:x[0], reverse = True)

        # Method 2 - Exclusively process Type 3 Edges
        for type, u, v in edges:
            if type != 3:
                continue

            # We check if are unioning 2 already connected vertices
            alice.union(u - 1, v - 1)

            # If we are connecting 2 already connected vertices, this edge is "redundant" and can be removed
            # Note that we can just take either the union function for alice UFDS or bob UFDS since both should still be identical
            if bob.union(u - 1, v - 1):
                ans += 1

        # Process Type 1 and Type 2 edges
        for type, u, v in edges:
            if type == 1:
                # If we are connecting 2 already connected vertices, this edge is "redundant" and can be removed
                if alice.union(u - 1, v - 1):
                    ans += 1
            elif type == 2:
                # If we are connecting 2 already connected vertices, this edge is "redundant" and can be removed
                if bob.union(u - 1, v - 1):
                    ans += 1

        # If the number of disjoint sets does not equal 1, it means there are unconnected vertices in either UFDS
        if alice.num_disjoint_sets != 1 or bob.num_disjoint_sets != 1:
            return -1

        return ans

# edges = [[1,1,2],[2,1,2],[3,1,2]]
# print(Solution().maxNumEdgesToRemove(2, edges))