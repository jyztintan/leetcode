# Kadane's Algorithm -> O(n) time

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        mid = len(nums)//2
        left_sum = self.maxSubArray(nums[:mid])
        right_sum = self.maxSubArray(nums[mid:])
        mid_sum = self.findSum(nums)
        return max(left_sum, right_sum, mid_sum)

    def findSum(self, nums):
        if len(nums) == 1:
            return nums[0]
        max_l = -float("inf")
        i = len(nums)//2 - 1
        sum = 0
        while i >= 0:
            sum += nums[i]
            if sum > max_l:
                max_l = sum
            i -= 1
        max_r = -float("inf")
        i = len(nums)//2
        sum = 0
        while i < len(nums):
            sum += nums[i]
            if sum > max_r:
                max_r = sum
            i += 1
        return max_l + max_r