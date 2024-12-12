from heapq import *


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        # Sorts queries by latest end time then by later start time
        queries = deque(sorted(queries))
        available = []
        in_use = []

        for idx in range(len(nums)):
            # Get all available queries
            while queries and queries[0][0] <= idx:
                heappush(available, -queries.popleft()[1])

            # Get rid of deprecated queries
            while in_use and in_use[0] < idx:
                heappop(in_use)

            # Use as many available queries as needed
            while nums[idx] > len(in_use):
                # If no new query available to make the curr num 0, then invalid
                if not available or - available[0] < idx:
                    return -1
                # Otherwise, we use it
                heappush(in_use, -heappop(available))

        return len(available)