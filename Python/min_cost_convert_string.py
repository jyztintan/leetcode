import heapq
from collections import defaultdict
from typing import List


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

