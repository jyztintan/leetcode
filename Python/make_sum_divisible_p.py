class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        if total < p:
            return -1
        elif total % p == 0:
            return 0

        target = total % p
        best = float('inf')
        curr = 0
        seen = {0: -1}  # offset for start of array

        for i, num in enumerate(nums):
            curr = (curr + num) % p
            complement = (curr - target) % p
            if complement in seen:
                best = min(best, i - seen[complement])
            seen[curr] = i

        # not allowed to remove whole array
        if best == len(nums):
            return - 1
        return best
