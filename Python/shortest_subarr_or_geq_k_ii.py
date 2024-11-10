class Solution:
    def minimumSubarrayLength(self, nums, k: int) -> int:
        best = float('inf')
        left = 0
        bits = [0] * 32

        for right, num in enumerate(nums):

            for pos in range(32):
                if num & (1 << pos):
                    bits[pos] += 1

            res = 0
            for pos in range(32):
                if bits[pos]:
                    res |= 1 << pos

            while left <= right and res >= k:
                best = min(best, right - left + 1)

                for pos in range(32):
                    if nums[left] & (1 << pos):
                        bits[pos] -= 1
                left += 1

                res = 0
                for pos in range(32):
                    if bits[pos]:
                        res |= 1 << pos

        if best == float('inf'):
            return -1
        return best
