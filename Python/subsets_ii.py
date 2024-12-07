class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()

        ans = []
        subset = []

        def backtrack(idx):
            if idx >= len(nums):
                ans.append(subset[:])
                return

            subset.append(nums[idx])
            backtrack(idx + 1)
            subset.pop()

            # If we are skipping the element, then we also skip all duplicates :)
            while idx + 1 < len(nums) and nums[idx + 1] == nums[idx]:
                idx += 1
            backtrack(idx + 1)

        backtrack(0)
        return ans


print(Solution().subsetsWithDup([1,2,2,3]))
