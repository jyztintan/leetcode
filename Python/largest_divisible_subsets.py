# DP Solution
# Time: O(N^2) since we only need to iterate 2 nested for loops
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [[num] for num in nums]

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]

        return max(dp, key=len)


# TLE Backtracking solution
# Time:O(2^N) where we explore all possible subsets :(
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        curr_subset = []
        n = len(nums)
        longest = [1] * n

        def backtrack(ptr):
            if ptr == n:
                nonlocal longest
                if len(longest) < len(curr_subset):
                    longest = curr_subset[:]
                return

            num = nums[ptr]
            if not curr_subset or num % curr_subset[-1] == 0:
                curr_subset.append(num)
                backtrack(ptr + 1)
                curr_subset.pop()
            backtrack(ptr + 1)

        backtrack(0)
        return longest
