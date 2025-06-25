class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroes = 0
        best = 0
        curr = 0
        left, right = 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeroes += 1
            while zeroes > k:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
