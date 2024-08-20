class Solution:
    def stoneGameII(self, piles) -> int:
        n = len(piles)
        if n <= 3:
            return sum(piles[:2])

        dp = [[0] * (n + 1) for i in range(n + 1)]

        sum_to_end = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            sum_to_end[i] = sum_to_end[i + 1] + piles[i]

        for i in range(n + 1):
            dp[i][n] = sum_to_end[i]

        for i in range(n - 1, -1, -1):
            for M in range(n - 1, 0, -1):
                for X in range(1, min(2 * M, n - i) + 1):
                    dp[i][M] = max(dp[i][M], sum_to_end[i] - dp[i + X][max(M, X)])

        return dp[0][1]

piles = [1]
print(Solution().stoneGameII(piles))
