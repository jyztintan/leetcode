from heapq import *


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapify(stones)
        while len(stones) > 1:
            heaviest = heappop(stones)
            second_heaviest = heappop(stones)
            heappush(stones, heaviest - second_heaviest)
        return - stones[0]