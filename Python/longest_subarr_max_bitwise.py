class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_and = max(nums)
        best = 0
        count = 0
        for num in nums:
            if num == max_and:
                count += 1
            else:
                best = max(count, best)
                count = 0
        best = max(count, best)
        return best
