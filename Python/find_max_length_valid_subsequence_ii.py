class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]
        ans = 0
        for num in nums:
            curr = num % k
            for congruent in range(k):
                dp[curr][congruent] = dp[congruent][curr] + 1
                ans = max(ans, dp[curr][congruent])
        return ans
