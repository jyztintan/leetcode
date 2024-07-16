import heapq

class Solution:
    def minInterval(self, intervals, queries):
        intervals.sort()

        # Min heap, sorting intervals by increasing length and limit
        heap = []
        ans = {}
        ptr = 0

        for query in sorted(queries):

            # For each query, we push all valid intervals into the minheap
            while ptr < len(intervals) and intervals[ptr][0] <= query:
                low, high = intervals[ptr]
                heapq.heappush(heap, (high - low + 1, high))
                ptr += 1

            # If the smallest interval is not valid for the current query, then we pop it off
            while heap and query > heap[0][1]:
                heapq.heappop(heap)

            # Now, we can be sure that the interval on the top of the min heap is the smallest valid interval
            ans[query] = heap[0][0] if heap else -1

        return [ans[query] for query in queries]
