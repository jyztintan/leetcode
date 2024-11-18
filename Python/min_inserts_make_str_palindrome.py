class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)

        dp = [[0] * n for _ in range(n)]

        # Try different string lengths until finally get the whole string
        for length in range(2, n + 1):
            # Sliding window for strings of length
            for left in range(n - length + 1):
                right = left + length - 1
                # If match first and last, no need to do modify so just take prev ans
                if s[left] == s[right]:
                    # For example: the number of modifications for 'xABCx' = number of modifications for 'ABC'
                    dp[left][right] = dp[left + 1][right - 1]
                else:
                    # Either add a character to the left, or add a character to the right
                    # For example: the number of modifications for 'ABC'
                    # = number of modifications for 'BC' + 1 OR number of modifications for 'AB' + 1
                    dp[left][right] = min(dp[left + 1][right], dp[left][right - 1]) + 1

        return dp[0][n - 1]


print(Solution().minInsertions('zjveiiwvc'))