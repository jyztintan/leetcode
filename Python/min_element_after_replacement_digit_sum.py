class Solution:
    def minElement(self, nums: List[int]) -> int:
        lowest = inf
        for num in nums:
            curr = 0
            for c in str(num):
                curr += int(c)
            lowest = min(lowest, curr)
        return lowest
