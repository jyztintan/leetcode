class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return sum(1 if num % 3 else 0 for num in nums)
