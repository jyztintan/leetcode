class Solution:
    def getAncestors(self, n: int, edges):

        # Create an adjacency list to keep track of edges
        # Note that we cannot use [[]] * n because this will initialise all empty lists with the same reference
        adj_list = [[] for _ in range(n)]

        # Keep track of in-degrees of all nodes for topological sorting
        in_degree = [0] * n

        # For each edge, we add to our adjacency list and increment the respective child's in-degree
        for edge in edges:
            parent, child = edge
            adj_list[parent].append(child)
            in_degree[child] += 1

        # Keep track of elements with 0 in-degree for our topological sort
        zero_in_degree = []
        for i in range(n):

            # If the in-degree is 0, we can now add it as the next node in our topological sort
            if in_degree[i] == 0:
                zero_in_degree.append(i)

        topological_sort = []


        while zero_in_degree:
            # Get an element from the zero_in_degree
            # Note that pop() is O(1) but pop(0) is O(N)
            current_node = zero_in_degree.pop()
            topological_sort.append(current_node)

            for child in adj_list[current_node]:
                in_degree[child] -= 1
                # If the in-degree is 0, we can now add it as the next node in our topological sort
                if in_degree[child] == 0:
                    zero_in_degree.append(child)

        # Since we have sorted them topologically, we can be sure that we have added ALL ancestors of our ancestor
        ancestors = [set() for _ in range(n)]
        for node in topological_sort:
            for child in adj_list[node]:
                # Add the parent
                ancestors[child].add(node)
                # Add the ancestors of our parent
                ancestors[child].update(ancestors[node])

        # Leetcode wants the ancestor list to be sorted
        ans = [sorted(list(lst)) for lst in ancestors]
        return ans

# edgeList = [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]
# print(Solution().getAncestors(8, edgeList))