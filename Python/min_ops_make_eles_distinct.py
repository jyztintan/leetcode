class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()
        for idx in range(n - 1, -1, -1):
            num = nums[idx]
            if num in seen:
                return (idx // 3) + 1
            seen.add(num)
        return 0
