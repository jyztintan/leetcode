class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        best = inf
        for i, num in enumerate(nums):
            if num == target:
                best = min(best, abs(start - i))
        return best
