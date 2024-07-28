class Solution:
    def maxProfit(self, prices) -> int:
        days = len(prices)
        # 0th index represents if we buy
        # 1st index if we sell
        # 2nd index represents if we do not hold the stock and don't do anything
        states = [-float("inf"), 0, 0]
        for day in range(days):
            new_states = [0, 0, 0]

            # The new "buy" state would be the max of
            # if we continue holding the stock or we buy the stock today (after a cooldown)
            new_states[0] = max(states[2] - prices[day], states[0])
            # The new "sell" state would be we sell the stock we currently hold at today's price
            new_states[1] = states[0] + prices[day]
            # The new "cooldown" state would be if we continue not holding the stock from yesterday's cooldown
            # Or starting a new cooldown after selling the stock yesterday
            new_states[2] = max(states[1], states[2])

            states = new_states

        # Return the best current state
        return max(states)

# prices = [7, 1, 5, 3, 6, 4]
# print(Solution().maxProfit(prices))