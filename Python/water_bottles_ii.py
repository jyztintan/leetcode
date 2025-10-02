class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total = 0
        empty = 0
        while numBottles:
            total += numBottles
            empty += numBottles
            numBottles = 0
            while empty >= numExchange:
                numBottles += 1
                empty -= numExchange
                numExchange += 1
        return total
