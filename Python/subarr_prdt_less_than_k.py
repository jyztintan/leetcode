class Solution:
    def numSubarrayProductLessThanK(self, nums, k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        count = 0
        curr = 1
        for right, num in enumerate(nums):
            curr *= num

            while curr >= k:
                curr //= nums[left]
                left += 1
            count += right - left + 1
        return count