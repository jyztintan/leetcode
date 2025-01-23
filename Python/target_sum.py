from collections import defaultdict
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        n = len(nums)

        def dfs(ptr, curr):
            if (ptr, curr) in memo:
                return memo[(ptr, curr)]

            if ptr == n:
                return 1 if curr == target else 0

            future = dfs(ptr + 1, curr + nums[ptr]) + dfs(ptr + 1, curr - nums[ptr])
            memo[(ptr, curr)] = future
            return future

        return dfs(0, 0)


# Brute force O(2^n) but i think its pretty elegant
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        possible = defaultdict(int)
        possible[0] = 1
        for num in nums:
            new_possible = defaultdict(int)
            for prev in possible:
                new_possible[prev + num] += possible[prev]
                new_possible[prev - num] += possible[prev]
            possible = new_possible
        return possible[target]
# nums = [1,1,1,1,1]
# print(Solution().findTargetSumWays(nums, 3))
