# Solution 1: 2D Dynamic Programming
class Solution:
    def change(self, amount: int, coins) -> int:
        # We use the index number to represent number of combinations from amount 0 to target amount
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for sub_amt in range(coin, amount + 1):
                dp[sub_amt] += dp[sub_amt - coin]
        return dp[amount + 1]


# Solution 2: Memoization
class Solution:
    def __init__(self):
        self.coins = None
        self.memoize = {}

    def change(self, amount: int, coins) -> int:
        self.coins = coins

        def count(amount, num_coins):
            if not num_coins or amount < 0:
                return 0
            if amount == 0:
                return 1
            if (amount, num_coins) in self.memoize:
                return self.memoize[(amount, num_coins)]
            x = self.memoize[(amount, num_coins - 1)] = count(amount, num_coins - 1)
            y = self.memoize[(amount - self.coins[num_coins - 1], num_coins)] = count(
                amount - self.coins[num_coins - 1], num_coins)
            return x + y

        return count(amount, len(coins))


coins = [1, 2, 5]
print(Solution().change(5, coins))
