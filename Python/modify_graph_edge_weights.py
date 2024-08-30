import heapq
from typing import List


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[
        List[int]]:

        adj_list = {i: [] for i in range(n)}
        for u, v, weight in edges:
            if weight != -1:
                adj_list[u].append((v, weight))
                adj_list[v].append((u, weight))

        def dijkstra():
            min_dist = [float('inf')] * n
            min_dist[source] = 0
            min_heap = [(0, source)]

            while min_heap:
                dist, node = heapq.heappop(min_heap)
                if dist > min_dist[node]:
                    continue
                for neighbour, weight in adj_list[node]:
                    new_dist = dist + weight
                    if new_dist < min_dist[neighbour]:
                        min_dist[neighbour] = new_dist
                        heapq.heappush(min_heap, (new_dist, neighbour))

            return min_dist[destination]

        shortest = dijkstra()
        # If the shortest distance without using any edges with -1 weights is already less than target,
        # This path will always be the shortest distance no matter what we assign those -1 edges.
        # Since this path will always be the shortest distance and < target, return empty list.
        if shortest < target:
            return []

        # If the shortest distance without using any edges with -1 weights already equals target
        # We just need to make sure the -1 edges don't give us another shortest path
        # Assign some insane high weight value to those edges
        if shortest == target:
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = int(2e9)
            return edges

        for i, (u, v, w) in enumerate(edges):
            if w != -1:
                continue

            edges[i][2] = 1
            adj_list[u].append((v, 1))
            adj_list[v].append((u, 1))

            new_shortest = dijkstra()
            if new_shortest <= target:
                edges[i][2] += target - new_shortest

                for j in range(i + 1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = int(2e9)
                return edges
        return []


# Test the solution
# edges = [[4, 1, -1], [2, 0, -1], [0, 3, -1], [4, 3, -1]]
# print(Solution().modifiedGraphEdges(5, edges, 0, 1, 5))
# edges = [[0,1,-1],[0,2,5]]
# print(Solution().modifiedGraphEdges(3, edges, 0, 2, 6))
# edges = [[1,4,1],[2,4,-1],[3,0,2],[0,4,-1],[1,3,10],[1,0,10]]
# print(Solution().modifiedGraphEdges(5, edges, 0, 2, 15))

