class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)
        quota = [1] * n
        quota[n - 1] += 1
        for num in nums:
            quota[num - 1] -= 1
        return all(q == 0 for q in quota)
