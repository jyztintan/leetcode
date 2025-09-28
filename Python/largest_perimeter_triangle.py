class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        for i in range(n - 1, 1, -1):
            first, second, third = nums[i], nums[i - 1], nums[i - 2]
            if second + third > first:
                return first + second + third
        return 0
