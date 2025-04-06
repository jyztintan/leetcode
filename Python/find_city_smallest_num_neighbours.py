# This solution seems like it can be better optimised. Time complexity: O(V^2logV)?

from heapq import *
from collections import defaultdict
from typing import List


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj_list = defaultdict(set)
        for u, v, w in edges:
            adj_list[u].add((v, w))
            adj_list[v].add((u, w))

        def dijkstra(node):
            distances = [float('inf')] * n
            distances[node] = 0
            pq = [(0, node)]
            while pq:
                dist, u = heappop(pq)
                if dist > distanceThreshold:
                    break
                for neighbour, weight in adj_list[u]:
                    if distances[neighbour] > dist + weight:
                        distances[neighbour] = dist + weight
                        heappush(pq, (dist + weight, neighbour))
            return distances

        neighbours, city = float('inf'), -1
        for node in range(n):
            distances = dijkstra(node)
            count = sum(int(distance <= distanceThreshold) for distance in distances)
            if count <= neighbours:
                neighbours, city = count, node
        return city
