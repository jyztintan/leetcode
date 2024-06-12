class Solution:
    def maxProfit(self, prices) -> int:
        buy = float('inf')
        profit = 0
        for price in prices:
            if price < buy:
                buy = price
            elif price - buy > profit:
                profit = price - buy
        return profit

# test = Solution()
# print(test.maxProfit([7,1,5,3,6,4]))
# print(test.maxProfit([7,6,4,3,1]))