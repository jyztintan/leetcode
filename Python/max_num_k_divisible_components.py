from collections import defaultdict, deque
from typing import List


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if not edges:
            return 1

        in_degrees = [0] * n
        adj_list = defaultdict(list)
        for u, v in edges:
            in_degrees[u] += 1
            in_degrees[v] += 1
            adj_list[u].append(v)
            adj_list[v].append(u)

        q = deque()
        for node in range(n):
            if in_degrees[node] == 1:
                q.append(node)

        count = 0
        while q:
            node = q.popleft()
            add_value = 0
            in_degrees[node] -= 1

            if values[node] % k == 0:
                count += 1
            else:
                add_value = values[node]

            for neighbour in adj_list[node]:
                if in_degrees[neighbour] == 0:
                    continue
                in_degrees[neighbour] -= 1
                values[neighbour] += add_value
                if in_degrees[neighbour] == 1:
                    q.append(neighbour)

        return count
