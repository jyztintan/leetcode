
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        vals = {}
        bad = 0
        for idx, num in enumerate(nums):
            val = idx - num
            good = vals.get(val, 0)
            bad += idx - good
            vals[val] = good + 1
        return bad
