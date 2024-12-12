from heapq import *
from typing import List

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = []
        for gift in gifts:
            heappush(max_heap, -gift)

        for _ in range(k):
            gift = - heappop(max_heap)
            left_behind = int(gift ** 0.5)
            heappush(max_heap, -left_behind)

        return - sum(max_heap)
