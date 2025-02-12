import heapq
from typing import List


class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        curr = 0
        count = 0
        min_heap = []
        for num in nums:
            curr += num
            if num < 0:
                heapq.heappush(min_heap, num)
            if curr < 0:
                curr -= heapq.heappop(min_heap)
                count += 1
        return count
