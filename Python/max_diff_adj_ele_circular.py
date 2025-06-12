class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        best = 0
        for idx in range(len(nums) - 1):
            best = max(best, abs(nums[idx] - nums[idx + 1]))
        best = max(best, abs(nums[0] - nums[-1]))
        return best
