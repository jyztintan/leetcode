class Solution:
    def __init__(self):
        self.memoize = {}
    def coinChange(self, coins, amount: int) -> int:
        dp = [float('inf')] * (amount + 1)

        # Base case: 0 coins to make up $0
        dp[0] = 0

        # We try using a different coin everytime
        for coin in coins:
            for i in range(coin, amount + 1):
                # If we use the coin, then we add 1, plus the min number of coins needed to make the remaining amount
                dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == float('inf'):
            return -1
        return dp[amount]