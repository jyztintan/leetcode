class Solution:
    def maxSum(self, nums: List[int]) -> int:
        positive = set([num for num in nums if num > 0])
        if len(positive) == 0:
            return max(nums)
        return sum(positive)
