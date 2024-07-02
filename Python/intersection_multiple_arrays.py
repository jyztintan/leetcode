class Solution:
    def intersection(self, nums):
        ans = set(nums[0])
        for arr in nums:
            ans = ans & set(arr)
        return sorted(list(ans))

# nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
# print(Solution().intersection(nums))
# nums = [[1,2,3],[4,5,6]]
# print(Solution().intersection(nums))