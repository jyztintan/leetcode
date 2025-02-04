class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        curr = [1, 1]
        best = 0
        prev = nums[0]
        for num in nums[1:]:
            if num == prev:
                best = max(best, curr[0], curr[1])
                curr = [0, 0]
            if num < prev:
                best = max(best, curr[0])
                curr[0] = 0
            else:
                best = max(best, curr[1])
                curr[1] = 0
            curr[0] += 1
            curr[1] += 1
            prev = num
        best = max(best, curr[0], curr[1])
        return best
