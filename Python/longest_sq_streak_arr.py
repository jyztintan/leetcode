class Solution:
    def longestSquareStreak(self, nums) -> int:
        set_nums = sorted(set(nums))
        ans = 0
        for num in nums:
            curr = num
            trial = 0
            while curr in set_nums:
                set_nums.remove(curr)
                curr **= 2
                trial += 1
            ans = max(ans, trial)

        if ans == 1:
            return -1
        return ans



