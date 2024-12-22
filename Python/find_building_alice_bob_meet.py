# Time: O(N + QlogQ)
# This is because the scanning through the heights of the building and the heap operations are done 'concurrently'
# Depending on N and Q, the dominating variable will determine the time complexity of this algorithm
from heapq import *


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)

        # We group unanswered queries by their rightmost index
        grouped_queries = [[] * len(heights)]

        # Answer all queries that can be immediately answered
        for idx, (alice, bob) in enumerate(queries):

            # Let Alice always be the left building
            if alice > bob:
                alice, bob = bob, alice

            if heights[bob] >= heights[alice]:
                ans[idx] = bob
            else:
                # We can be sure that Alice is higher because if Bob was higher, this query would already be answered
                grouped_queries[bob].append((heights[alice], idx))

        unanswered_queries = []
        for idx, building in enumerate(heights):
            for q_height, q_idx in grouped_queries[idx]:
                heappush(unanswered_queries, (q_height, q_idx))

            while unanswered_queries and building > unanswered_queries[0][0]:
                q_height, q_idx = heappop(unanswered_queries)
                ans[q_idx] = idx

        return ans



# Brute Force: O(Q * N)
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        n = len(heights)
        for alice, bob in queries:
            if alice == bob:
                ans.append(alice)
                continue

            # Let Alice always be the left building
            if alice > bob:
                alice, bob = bob, alice

            ptr = bob
            while ptr < n:
                if heights[ptr] > heights[alice] and heights[ptr] >= heights[bob]:
                    break
                ptr += 1

            if ptr == n:
                ans.append(-1)
            else:
                ans.append(ptr)
        return ans