class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0

        left = 0
        subsum = 0

        for right in range(n):
            subsum += nums[right]
            while left <= right and subsum * (right - left + 1) >= k:
                subsum -= nums[left]
                left += 1
            count += (right - left + 1)
        return count
