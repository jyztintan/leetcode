class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        complement = {}
        best = inf
        for i, num in enumerate(nums):
            if num in complement:
                best = min(best, i - complement[num])
            reverse = int(str(num)[::-1])
            complement[reverse] = i
        if best == inf:
            return -1
        return best
