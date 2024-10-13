import heapq
from typing import List


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)

        left = float('inf')
        right = -1
        min_heap = []

        for i, lst in enumerate(nums):
            left = min(left, lst[0])
            right = max(right, lst[0])
            heapq.heappush(min_heap, (lst[0], i, 0))

        best = [left, right]
        gap = right - left
        while True:
            lowest, lst_idx, idx = heapq.heappop(min_heap)
            if idx + 1 == len(nums[lst_idx]):
                return best

            nxt = nums[lst_idx][idx + 1]
            heapq.heappush(min_heap, (nxt, lst_idx, idx + 1))
            right = max(right, nxt)
            left = min_heap[0][0]
            if right - left < gap:
                best = [left, right]
                gap = right - left
