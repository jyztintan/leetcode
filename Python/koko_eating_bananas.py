import math
class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:

        # Note that h must always be at least = number of piles
        # In that case, our upper limit for k would be max(piles)
        low = 1
        high = max(piles)

        def count(k):
            ans = 0
            for pile in piles:
                ans += math.ceil(pile/k)
            return ans

        while low < high:
            mid = (low + high) // 2

            # If time taken to eat exceeds h,
            # Then we need to eat faster
            if count(mid) > h:
                low = mid + 1
            else:
                high = mid
        return low

# piles = [3,6,7,11]
# print(Solution().minEatingSpeed(piles, 8))
# piles = [30,11,23,4,20]
# print(Solution().minEatingSpeed(piles, 5))
# piles = [30,11,23,4,20]
# print(Solution().minEatingSpeed(piles, 6))
# piles = [312884470]
# print(Solution().minEatingSpeed(piles, 312884469))
# piles = [332484035,524908576,855865114,632922376,222257295,690155293,112677673,679580077,337406589,290818316,877337160,901728858,679284947,688210097,692137887,718203285,629455728,941802184]
# print(Solution().minEatingSpeed(piles, 823855818))
