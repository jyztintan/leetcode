class Solution:
    def countFairPairs(self, nums, lower: int, upper: int) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        nums.sort()

        left, right = 0, n - 1
        count = 0
        while left < right:
            curr = nums[left] + nums[right]
            if curr <= upper:
                count += right - left
                left += 1
            else:
                right -= 1

        left, right = 0, n - 1
        while left < right:
            curr = nums[left] + nums[right]
            if curr < lower:
                count -= right - left
                left += 1
            else:
                right -= 1
        return count