class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        left = 0
        zeroes = 0
        n = len(nums)
        for right in range(n):
            if nums[right] == 0:
                zeroes += 1
            while zeroes > 1:
                if nums[left] == 0:
                    zeroes -= 1
                left += 1
            best = max(best, right - left + 1)
        return best