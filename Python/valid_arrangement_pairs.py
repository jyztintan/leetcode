from collections import defaultdict
from typing import List


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj_list = defaultdict(list)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)

        for u, v in pairs:
            adj_list[u].append(v)
            in_degree[v] += 1
            out_degree[u] += 1

        path = []
        def dfs(node):
            while adj_list[node]:
                nxt = adj_list[node].pop()
                dfs(nxt)
            path.append(node)

        # Essentially we need to find the starting node for our Euler path
        start = None
        for node in out_degree:
            if in_degree[node] < out_degree[node]:
                start = node
                break

        # If no starting node is found then it means that there is an Euler circuit so just pick any random node
        if not start:
            start = node

        dfs(start)

        res = []
        for i in range(1, len(path)):
            res.append([path[-i], path[-i-1]])
        return res
