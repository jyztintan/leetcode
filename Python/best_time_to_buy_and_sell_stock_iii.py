class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # Get the profits from left to right
        lowest = prices[0]
        left_profits = [0] * n
        for left in range(1, n):
            left_profits[left] = max(left_profits[left - 1], prices[left] - lowest)
            lowest = min(lowest, prices[left])

        # Get the profits from right to left
        highest = prices[-1]
        right_profits = [0] * n
        for i in range(n - 2, -1, -1):
            right_profits[i] = max(right_profits[i + 1], highest - prices[i])
            highest = max(highest, prices[i])

        # The profits of non overlapping left and right can be combined since we can buy and sell twice
        max_profit = 0
        for i in range(n - 1):
            combined = left_profits[i] + right_profits[i + 1]
            max_profit = max(max_profit, combined)

        # In the chance that the best option is just to buy and sell once
        max_profit = max(max_profit, left_profits[-1])
        return max_profit
