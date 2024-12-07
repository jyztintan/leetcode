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

    def subsets(self, nums):
        ans = []
        subset = []
        def backtrack(idx):
            if idx >= len(nums):
                ans.append(subset[:])
                return

            subset.append(nums[idx])
            backtrack(idx + 1)
            subset.pop()
            backtrack(idx + 1)

        backtrack(0)
        return ans

# print(Solution().subsets([1,2,3]))
