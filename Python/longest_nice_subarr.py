class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        curr = 0
        best = 0

        for right in range(len(nums)):
            while curr & nums[right] != 0:
                # Remove from left of window
                curr ^= nums[left]
                left += 1

            # Add right of window
            curr |= nums[right]
            best = max(best, right - left + 1)
        return best
