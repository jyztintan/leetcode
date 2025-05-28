from collections import defaultdict
from typing import List


class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def make_adj_list(edges):
            adj_list = defaultdict(set)
            for u, v in edges:
                adj_list[u].add(v)
                adj_list[v].add(u)
            return adj_list

        adj_list1 = make_adj_list(edges1)
        adj_list2 = make_adj_list(edges2)

        def count_neighbours(node, adj_list, limit):
            visited = set()
            visited.add(node)
            curr = adj_list[node]
            for _ in range(limit):
                nxt = set()
                for node in curr:
                    if node not in visited:
                        nxt.update(adj_list[node])
                visited.update(curr)
                curr = nxt
            return len(visited)

        count_neighbours_n, count_neighbours_m = [], []
        n, m = len(edges1) + 1, len(edges2) + 1

        for node in range(n):
            count_neighbours_n.append(count_neighbours(node, adj_list1, k))

        for node in range(m):
            count_neighbours_m.append(count_neighbours(node, adj_list2, k - 1))

        if k == 0:
            return count_neighbours_n

        responses = []
        best = max(count_neighbours_m)
        for query in range(n):
            responses.append(count_neighbours_n[query] + best)
        return responses

# edges1 = [[0,1],[0,2],[2,3],[2,4]]
# edges2 = [[0,1],[0,2],[0,3],[2,7],[1,4],[4,5],[4,6]]
# print(Solution().maxTargetNodes(edges1, edges2, 2))