class Solution:
    def subsets(self, nums):
        if not nums:
            return [[]]
        half = self.subsets(nums[1:])
        ans = []
        for subset in half:
            ans.append(subset[:])
            subset.append(nums[0])
            ans.append(subset)
        return ans

# print(Solution().subsets([1,2,3]))
