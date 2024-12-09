# Using sets to avoid recomputation O(N * M) since the possible set may calculate all possible M = sum(nums)/2
class Solution:
    def canPartition(self, nums) -> bool:

        # If the total is not divisible by 2, then it obviously can't be partitioned
        total = sum(nums)
        if total % 2:
            return False

        # The target sum should be the total divided by 2
        target = total / 2

        # The idea is that we use sets so that we don't have to compute same values
        possible = set()
        possible.add(0)
        for num in nums:
            # If the negation of this number is inside, we can confidently say we found the partition
            if target - num in possible:
                return True
            # For each number, we can either choose to include or exclude in the component of the partition
            to_add = set()
            for prev in possible:
                to_add.add(num + prev)
            possible.update(to_add)
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

