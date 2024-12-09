# Bottom Up
class Solution:
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

# Top down
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amt):
            if amt < 0:
                return -1
            if amt == 0:
                return 0
            if amt in memo:
                return memo[amt]
            min_coins = float('inf')
            for coin in coins:
                subproblem = dfs(amt - coin)
                if subproblem != -1:
                    min_coins = min(min_coins, subproblem + 1)
            memo[amt] = min_coins if min_coins != float('inf') else -1
            return memo[amt]
        return dfs(amount)
