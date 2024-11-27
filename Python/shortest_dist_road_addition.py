import queue
from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj_list = {}
        for u in range(n - 1):
            adj_list[u] = set([u + 1])

        def bfs():
            count = 1
            q = adj_list[0]
            # Put all possible next nodes
            while True:
                next_level = set()
                for v in q:
                    if v == n - 1:
                        return count
                    next_level.update(adj_list[v])

                q = next_level
                count += 1

        ans = []
        for u, v in queries:
            adj_list[u].add(v)
            ans.append(bfs())

        return ans


print(Solution().shortestDistanceAfterQueries(5, [[2,4],[0,2],[0,4]]))
