# Top down (need to use array to store ans cuz dictionary will MLE LOL
class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        m, n = len(source), len(pattern)
        targetIndices = set(targetIndices)
        memo = [[None] * (n + 1) for _ in range(m + 1)]

        def dfs(src, ptrn):
            if src == m:
                if ptrn == n:
                    return 0
                return -float('inf')

            if memo[src][ptrn] is not None:
                return memo[src][ptrn]

            if ptrn == n:
                ans = int(src in targetIndices) + dfs(src + 1, ptrn)
            else:
                skip = int(src in targetIndices) + dfs(src + 1, ptrn)
                ans = skip

                if source[src] == pattern[ptrn]:
                    match = dfs(src + 1, ptrn + 1)
                    ans = max(ans, match)

            memo[src][ptrn] = ans
            return ans

        return dfs(0, 0)

# Bottom up
class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        m, n = len(source), len(pattern)
        targetIndices = set(targetIndices)
        dp = [[-float("inf")] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = 0
        for src in range(m - 1, -1, -1):
            for ptrn in range(n, -1, -1):
                if ptrn == n:
                    dp[src][ptrn] = int(src in targetIndices) + dp[src + 1][ptrn]
                else:
                    dp[src][ptrn] = int(src in targetIndices) + dp[src + 1][ptrn]
                    if source[src] == pattern[ptrn]:
                        dp[src][ptrn] = max(dp[src][ptrn], dp[src + 1][ptrn + 1])
        if dp[0][0] == -float("inf"):
            return 0
        return dp[0][0]
