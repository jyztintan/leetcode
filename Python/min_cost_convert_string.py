import heapq
from collections import defaultdict
from typing import List


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj_list = defaultdict(dict)
        for x, y, z in zip(original, changed, cost):
            adj_list[x][y] = min(adj_list[x].get(y, float("inf")), z)

        # SSSP from each node
        def get_lowest_cost(start):
            pq = [(0, start)]
            visited = {start: 0}
            while pq:
                cost, curr = heappop(pq)
                if cost > visited[curr]:
                    continue
                for nxt in adj_list[curr]:
                    new_cost = cost + adj_list[curr][nxt]
                    if new_cost < visited.get(nxt, float("inf")):
                        visited[nxt] = new_cost
                        heappush(pq, (new_cost, nxt))
            return visited

        # Pre-compute all possible costs from each starting char
        mapping = [[float('inf')] * 26 for _ in range(26)]
        for start in range(26):
            distances = get_lowest_cost(chr(ord('a') + start))
            for node, cost in distances.items():
                mapping[start][ord(node) - ord('a')] = cost

        # Accumulate actual cost
        total = 0
        for i in range(len(source)):
            start, end = source[i], target[i]
            cost = mapping[ord(start) - ord('a')][ord(end) - ord('a')]
            if cost == float('inf'):
                return -1
            total += cost

        return total

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Create an adjacency list for transformations
        adj_list = defaultdict(list)
        for orig, chgd, cst in zip(original, changed, cost):
            adj_list[orig].append((chgd, cst))

        def floyd_warshall(chars, adj_list):
            # Initialize distances
            dist = {c: {d: float('inf') for d in chars} for c in chars}
            for c in chars:
                dist[c][c] = 0

            # Set initial direct transformation costs
            for c in chars:
                for d, cost in adj_list[c]:
                    dist[c][d] = min(dist[c][d], cost)

            # Floyd-Warshall update
            for k in chars:
                for i in chars:
                    for j in chars:
                        if dist[i][j] > dist[i][k] + dist[k][j]:
                            dist[i][j] = dist[i][k] + dist[k][j]

            return dist

        # Apply this function to precompute all costs
        min_costs = floyd_warshall(set(original + changed), adj_list)

        total_cost = 0
        for i in range(len(source)):
            transformation_cost = min_costs[source[i]][target[i]]
            if transformation_cost == float('inf'):  # Check if transformation is impossible
                return -1
            total_cost += transformation_cost

        return total_cost

