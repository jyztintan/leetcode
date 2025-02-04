class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr = 0
        best = 0
        prev = -1
        for num in nums:
            if num <= prev:
                best = max(best, curr)
                curr = num
            else:
                curr += num
            prev = num
        best = max(best, curr)
        return best
