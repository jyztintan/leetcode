class Solution:
    def findTargetSumWays(self, nums, target: int) -> int:
        memoize = {}

        def dfs(pointer, check_sum):
            if (pointer, check_sum) in memoize:
                return memoize[(pointer, check_sum)]
            if pointer == len(nums):
                if check_sum == target:
                    memoize[(pointer, check_sum)] = 1
                    return 1
                else:
                    memoize[(pointer, check_sum)] = 0
                    return 0

            memoize[(pointer, check_sum)] = dfs(pointer + 1, check_sum + nums[pointer]) + dfs(pointer + 1, check_sum - nums[pointer])
            return memoize[(pointer, check_sum)]

        return dfs(0, 0)

# nums = [1,1,1,1,1]
# print(Solution().findTargetSumWays(nums, 3))
