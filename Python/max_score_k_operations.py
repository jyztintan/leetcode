import heapq
from math import ceil


class Solution:
    def maxKelements(self, nums, k: int) -> int:
        score = 0
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)

        for _ in range(k):
            score += -max_heap[0]
            heapq.heapreplace(max_heap, -ceil(-max_heap[0] / 3))
        return score


