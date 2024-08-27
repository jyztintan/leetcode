import heapq
from typing import List


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int,
                       end_node: int) -> float:

        adj_list = {}
        for i in range(len(edges)):
            u,v = edges[i]
            prob = succProb[i]
            if u not in adj_list:
                adj_list[u] = []
            adj_list[u].append((v, prob))
            if v not in adj_list:
                adj_list[v] = []
            adj_list[v].append((u, prob))

        max_heap = [(-1, start_node)]
        visited = set()

        while max_heap:
            prob, curr = heapq.heappop(max_heap)
            visited.add(curr)
            if curr == end_node:
                return -prob

            if curr not in adj_list:
                continue
            for neighbour, next_prob in adj_list[curr]:
                if neighbour in visited:
                    continue
                heapq.heappush(max_heap, (next_prob * prob, neighbour))

        return 0

# edges = [[0,1],[1,2],[0,2]]
# print(Solution().maxProbability(3, edges, [0.5,0.5,0.2], 0, 2))
