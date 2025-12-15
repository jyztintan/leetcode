class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        curr = 0
        prev = prices[0] + 1
        count = 0
        for price in prices:
            if price == prev - 1:
                curr += 1
            else:
                curr = 1
            count += curr
            prev = price
        return count
