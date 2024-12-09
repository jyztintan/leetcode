class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(n - 1, -1, -1):
            coin = coins[i]
            for j in range(coin, amount + 1):
                dp[j] += dp[j - coin]
        return dp[amount]

# Solution 2: Memoization
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}

        def make_change(num_coins, amt):
            if amt < 0 or not num_coins:
                return 0
            if amt == 0:
                return 1
            if (num_coins, amt) in memo:
                return memo[(num_coins, amt)]

            coin = coins[num_coins - 1]
            memo[(num_coins, amt)] = make_change(num_coins, amt - coin) + make_change(num_coins - 1, amt)
            return memo[(num_coins, amt)]

        return make_change(len(coins), amount)


coins = [1, 2, 5]
print(Solution().change(5, coins))
