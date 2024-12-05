import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)

        def can_eat(k):
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            return time <= h

        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if can_eat(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans
