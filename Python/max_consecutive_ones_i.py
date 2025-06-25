class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        curr = 0
        for num in nums:
            if num == 0:
                best = max(best, curr)
                curr = 0
            else:
                curr += 1
        best = max(best, curr)
        return best