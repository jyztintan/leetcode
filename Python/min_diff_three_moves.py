class Solution:
    def minDifference(self, nums) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        diff = float('inf')
        for i in range(4):
            diff = min(diff, abs(nums[i-4] - nums[i]))
        return diff

# nums = [5,3,2,4]
# print(Solution().minDifference(nums))
# nums = [1,5,0,10,14]
# print(Solution().minDifference(nums))
# nums = [1,3,6,10,15,21]
# print(Solution().minDifference(nums))
