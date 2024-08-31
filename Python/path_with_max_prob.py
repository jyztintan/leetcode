import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:

        adj_list = {i: [] for i in range(n)}
        for i, (u, v) in enumerate(edges):
            adj_list[u].append((v, succProb[i]))
            adj_list[v].append((u, succProb[i]))

        max_heap = [(-1, start_node)]

        visited = set()
        while max_heap:
            prob, node = heapq.heappop(max_heap)
            if node in visited:
                continue
            visited.add(node)
            if node == end_node:
                return -prob
            for neighbour, weight in adj_list[node]:
                heapq.heappush(max_heap, (weight * prob, neighbour))

        return 0


edges = [[0, 1], [1, 2], [0, 2]]
print(Solution().maxProbability(3, edges, [0.5, 0.5, 0.2], 0, 2))
