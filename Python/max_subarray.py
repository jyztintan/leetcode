# Kadane's Algorithm -> O(n) time

class Solution:
    def maxSubArray(self, nums) -> int:
        curr_subarr = -float('inf')
        max_subarr = -float('inf')

        for num in nums:
            curr_subarr = max(num, curr_subarr + num)
            max_subarr = max(max_subarr, curr_subarr)

        return max_subarr