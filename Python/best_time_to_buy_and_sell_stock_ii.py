# Greedy solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        # Greedily check if there is an increase and take it
        for day in range(1, len(prices)):
            profit += max(0, prices[day] - prices[day - 1])
        return profit

# Peak and valley solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        day = 0
        total_days = len(prices)
        valley = peak = prices[0]

        while day < total_days:
            # While it is decreasing
            while day + 1 < total_days and prices[day] >= prices[day + 1]:
                day += 1
            valley = prices[day]
            # While it is increasing
            while day + 1 < total_days and prices[day] <= prices[day + 1]:
                day += 1
            peak = prices[day]
            profit += peak - valley
        return profit
