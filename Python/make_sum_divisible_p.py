class Solution:
    def minSubarray(self, nums, p: int) -> int:
        total = sum(nums)
        if total < p:
            return -1
        if total % p == 0:
            return 0

        target = total % p
        best = float('inf')
        prefix_sum = 0
        seen = {0: -1}

        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            complement = (prefix_sum - target) % p

            if complement in seen:
                best = min(best, i - seen[complement])
            seen[prefix_sum] = i

        if best == len(nums):
            return -1
        return best


nums = [3, 1, 4, 2]
print(Solution().minSubarray(nums, 6))

