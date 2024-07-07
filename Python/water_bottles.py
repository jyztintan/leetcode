class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = ans = numBottles

        while empty >= numExchange:
            new = empty // numExchange
            ans += new
            empty = empty % numExchange + new
        return ans

# print(Solution().numWaterBottles(17, 3))