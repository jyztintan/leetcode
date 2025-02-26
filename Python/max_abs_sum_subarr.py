# O(N) Kadane's algorithm similar to Max Subarray
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_subarr = - float('inf')
        largest_sum = - float('inf')

        curr_subarr_neg = float('inf')
        largest_sum_neg = float('inf')

        for num in nums:
            curr_subarr = max(curr_subarr + num, num)
            largest_sum = max(largest_sum, curr_subarr)
            curr_subarr_neg = min(curr_subarr_neg + num, num)
            largest_sum_neg = min(curr_subarr_neg, largest_sum_neg)

        return max(abs(largest_sum_neg), largest_sum)

# O(N) Prefix Sum Greedy solution
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_presum = 0
        min_presum = 0
        curr = 0

        for num in nums:
            curr += num
            max_presum = max(max_presum, curr)
            min_presum = min(min_presum, curr)

        return max_presum - min_presum
