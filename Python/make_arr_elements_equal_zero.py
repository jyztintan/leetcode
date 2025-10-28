class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        total = sum(nums)
        left = 0
        ans = 0
        for num in nums:
            left += num
            if num != 0:
                continue
            # Go right first
            right = total - left
            if 0 <= right - left <= 1:
                ans += 1
            if 0 <= left - right <= 1:
                ans += 1
        return ans
