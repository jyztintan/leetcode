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
    # There are 3 scenarios to this problem
    # 1) THe redundant edge causes a cycle
    # 2) The redundant edge causes a node to have 2 parents instead of only 1
    # 3) Both of the above
    # We need to be able to detect and handle all 3 scenarios in our programme
    def findRedundantDirectedConnection(self, edges):

        n = len(edges)

        # Create an adjacency list to keep track of edges
        # Note that we cannot use [[]] * n because this will initialise all empty lists with the same reference
        parent_adj_list = [[] for _ in range(n + 1)]
        ufds = UFDS(n + 1)
        edge_multiple_parents = [None, None]

        # For each edge, we add to our adjacency list and increment the respective child's in-degree
        for parent, child in edges:

            # If this node already had a parent
            if parent_adj_list[child]:

                # In a rooted tree, every node has exactly one parent
                # We can break the loop for efficiency as we can be sure that the answer is one of these 2 edges
                edge_multiple_parents[0] = (parent_adj_list[child], child)
                edge_multiple_parents[1] = (parent, child)
                break

            # Otherwise, mark this node as "parented"
            parent_adj_list[child] = parent

        for parent, child in edges:

            # We skip the edge that causes the multiple parents
            if (parent, child) == edge_multiple_parents[1]:
                continue

            # Now we check for existing cycles in the graph
            if ufds.union(child, parent):

                # Since we already skip the edge with multiple parents, but a cycle still exists,
                # Then, we should remove the other edge with the first parent.
                # That edge is the cause of both, the cycle as well as multiple parents.
                if edge_multiple_parents[0]:
                    return edge_multiple_parents[0]

                # If this node is part of a cycle but every node only has 1 parent
                # We remove this edge since it is the cause of a cycle
                return (parent, child)

        # If there is no cycle detected then the second edge must have been the cause of the multiple parents
        # and also the cause of the cycle (if any).
        return edge_multiple_parents[1]


# print(Solution().findRedundantDirectedConnection([[2, 3], [3, 4], [4, 2], [1, 2]]))
