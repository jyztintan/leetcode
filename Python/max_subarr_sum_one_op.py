class Solution:
    def maxSumAfterOperation(self, nums: List[int]) -> int:
        squared = 0
        unsquared = 0
        max_subarr = 0

        for num in nums:
            squared = max(squared + num, unsquared + num ** 2, num ** 2)
            unsquared = max(unsquared + num, num)
            max_subarr = max(max_subarr, squared)

        return max_subarr
