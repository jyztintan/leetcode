from heapq import *
from typing import List


class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)

        min_heap = []
        for idx, num in enumerate(nums):
            heappush(min_heap, (num, idx))

        marked_indices = set()
        score = 0

        while len(marked_indices) != n:
            smallest, idx = heappop(min_heap)
            if idx in marked_indices:
                continue
            score += smallest
            for marking_pos in range(idx - 1, idx + 2):
                if 0 <= marking_pos < n and nums[marking_pos]:
                    marked_indices.add(marking_pos)

        return score
