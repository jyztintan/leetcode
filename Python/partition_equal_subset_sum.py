# Using sets to avoid recomputation O(N * M) since the possible set may calculate all possible M = sum(nums)/2
class Solution:
    def canPartition(self, nums) -> bool:
        total = sum(nums)

        # If the total is not divisible by 2, then it obviously can't be partitioned
        if total % 2:
            return False

        target = total // 2
        possible = {target}
        for num in nums:
            if num in possible:
                return True
            # Choose to include or exclude in the new subset
            for subset in possible.copy():
                possible.add(subset - num)
        return False


# Brute Force O(2 ^ n): test for every possible combination of nums
# But after memoizing it becomes O(N * M), where n = len(nums) and m = sum(nums)//2
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        n = len(nums)

        def dfs(n, subset_sum):
            if subset_sum == 0:
                return True
            if not n or subset_sum < 0:
                return False
            return dfs(n - 1, subset_sum - nums[n - 1]) or dfs(n - 1, subset_sum)

        return dfs(n - 1, target)

