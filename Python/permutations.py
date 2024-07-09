class Solution:
    def permute(self, nums):

        ans = []

        def backtrack(permutation, fixed: set):
            if len(fixed) == len(nums):
                ans.append(permutation[:])
                return

            for i in range(len(nums)):
                if i not in fixed:
                    fixed.add(i)
                    permutation.append(nums[i])
                    backtrack(permutation, fixed)
                    fixed.remove(i)
                    permutation.pop()

        backtrack([], set())
        return ans


nums = [1, 2, 3]
print(Solution().permute(nums))
