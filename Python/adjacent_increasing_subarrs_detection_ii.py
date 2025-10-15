class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        curr = 1
        prev = 0
        ans = 0
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                prev = curr
                curr = 1
            ans = max(ans, min(curr, prev), curr // 2)
        return ans