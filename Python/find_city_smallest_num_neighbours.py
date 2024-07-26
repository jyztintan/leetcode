# This solution seems like it can be better optimised. Time complexity: O(V^2logV)?

import heapq
from collections import defaultdict
from typing import List
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        # Instantiate the adjacency list for easy access to edges
        adj_list = defaultdict(set)
        for u, v, w in edges:
            adj_list[u].add((v, w))
            adj_list[v].add((u, w))

        # We perform a modified version of Dijkstra's algorithm that terminates when the distanceThreshold is reached
        def dijkstra(src):
            neighbours = [float('inf')] * n
            pq = []
            heapq.heappush(pq, (0, src))
            # We exclude (negate) the source node itself
            ans = -1
            while pq:
                dist, u = heapq.heappop(pq)
                # If this node has been visited, we skip processing it again
                if neighbours[u] != float('inf'):
                    continue
                # Since our pq processes distances increasingly, all subsequent edges from here on would exceed
                # the distance threshold, and hence would be irrelevant
                if dist > distanceThreshold:
                    break
                neighbours[u] = dist
                ans += 1
                # Add edges of the newly visited vertex into the pq
                for v, w in adj_list[u]:
                    heapq.heappush(pq, (dist + w, v))

            return ans

        # We perform Dijkstra's algorithm for each node as source, and keep track of the city with the least neighbours
        least_neighbours = float('inf')
        city = -1
        for src in range(n):
            neighbours = dijkstra(src)
            if neighbours <= least_neighbours:
                least_neighbours = neighbours
                city = src

        return city

# edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]]
# print(Solution().findTheCity(4, edges, 4))